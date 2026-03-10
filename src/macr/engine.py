import numpy as np
from scipy.interpolate import pchip
import pandas as pd
import glob
import re
from pathlib import Path

from typing import Literal

# Resolve the path to the root of the project
ROOT_DIR = Path(__file__).resolve().parents[0]  # Goes from engine.py -> database

# Now get path to the database directory
DATABASE_DIR = ROOT_DIR / "database"


class Engine:
    """
    Engine Class for pyNIST Library

    Handles the communication to the local database of elements for the pyNIST material classes
    Requires specifying the desired libray between NIST and ESTAR.

    This can be pre-loaded for efficient operation but is otherwise unnecessary for end users
    as Material class loads engine on demand.

    Series of helper functions handle the offset in energy require for non-unique values in database,
    parse formulas into elemental consituent parts and effectively handle the atomic weight calculations
    corresponding to fractional weights of materials.

    Warning: Lowercase element names are ignored in parse_formula function and will error the system

    Intialisation Parameters
    ----------
    name - str - ESTAR or NIST

    Functions
    ---------

    Automatic - Happens during Initialisation:
        _generate_atomic_table - loads atomic weights, atomic numbers from database file
        _generate_material_list - generates list of materials in the database
        skiprows, col values - pre-declared values to enable scraping of the database files
                             - can be varied by user via "_declare_new_columns" method

    Manual - Called by user:
        parse_forumla - seperates a given chemical composotion into constituent
                        elements and number
        db_scraper - for material loads/interpolates the cross-sections for given
                     energies, if energies are not declared it loads default values.
                     Non-unique values are nudged by 0.1 eV to enable interpolation but
                     preserve k-edge
        _declare_new_columns - by default the Engine returns the total cross-section for
                               each element, this method switches the column read by the
                               scraper. Call Engine._declare_new_columns? for more details

    """

    def __init__(self, name: Literal["NIST", "ESTAR", "PSTAR", "SRIM"]) -> None:
        assert (
            (name == "NIST")
            or (name == "ESTAR")
            or (name == "PSTAR")
            or (name == "SRIM")
        )

        # set Engine Version
        self.name = name
        self.db_path = f"{DATABASE_DIR}/{self.name}/"

        # set Interpolation Method - can be reconfigured if desired but pchip worked best under testing
        self._interpolation_method = pchip

        # Configure Elemental Database
        self.db = {
            "names": ["atomic", "material_list"],
            "formats": [pd.DataFrame, list],
        }
        self.db["atomic"] = self._generate_atomic_table()
        self.db["material_list"] = self._generate_material_list()

        # Set Engine Specific Lables
        if self.name == "NIST":
            self.skiprows = 3
            self.col = -1
        elif self.name == "ESTAR":
            self.skiprows = 8
            self.col = -1
            print("ESTAR database incomplete, please consider pushing update to repo")
        elif self.name == "PSTAR":
            self.skiprows = 8
            self.col = -1
            print("PSTAR database incomplete, please consider SRIM engine instead")
        elif self.name == "SRIM":
            self.skiprows = 25
            self.col = 3

    def _declare_new_columns(self, val):
        """
        NIST AND ESTAR databases include additional crosssections.
        For NIST:
        Col 0 - Energies
        Col 1 - Coherent Scatter (Thomson)
        Col 2 - Incoherent Scatter (Compton)
        Col 3 - Photoelectric Absorption
        Col 4 - Nuclear Pair Production
        Col 5 - Electronic Pair Production
        Col 6 - Total (All) [DEFAULT]

        For ESTAR:
        Col 0 - Energies
        Col 1 - Collisional (MeV cm2/g)
        Col 2 - Radiative (MeV cm2/g)
        Col 3 - Total (MeV cm2/g)  [DEFAULT]

        For PSTAR:
        Col 0 - Energies
        Col 1 - Collisional (MeV cm2/g)
        Col 2 - Radiative (MeV cm2/g)
        Col 3 - Total (MeV cm2/g)  [DEFAULT]

        For SRIM:
        Col 0 - Energies
        Col 2 - Electronic (MeV cm2/g)
        Col 3 - Nuclear (MeV cm2/g)
        Col 4 - Total (MeV cm2/g)  [DEFAULT]
        """
        self.col = val

    def _generate_atomic_table(self):
        """
        Return dataframe for atomic number and weight
        Includes symbol parsing frame as well
        """
        df = pd.read_csv(
            f"{DATABASE_DIR}/atomic_weight.db",
            delimiter="\t",
            header=0,
            usecols=[0, 1, 2, 3, 5],
            names=["Z", "Symbol", "Name", "Weight", "Density"],
            dtype={
                "Z": int,
                "Symbol": str,
                "Name": str,
                "Weight": str,
                "Density": float,
            },
        )
        df["Weight"] = df["Weight"].apply(self._parse_value)

        return df

    def _generate_material_list(self):
        """
        returns list of available elements in database to mitigate errors
        eventually redundant as the database is completed
        """
        self._fileslist = glob.glob(self.db_path + "*.txt")
        self._materials = set(Path(f).stem.split("_")[-1] for f in self._fileslist)
        return [f.split("_")[-1].split(".")[0] for f in self._fileslist]

    def _parse_value(self, val):
        """
        try/except function to correct the formatting on values in the database
        Weird bug work around
        """
        try:
            if "[" in val:
                return float(val[1:-1])
            else:
                f = val.split(".")
                # print(f)
                return float(".".join([f[0], f[1][0]]))
        except ValueError:
            return val

    def parse_formula(self, formula: str) -> dict:
        """
        Parses a chemical formula and returns a dictionary mapping elements to their respective counts in the formula.
        Args:
        formula: A string representing a chemical formula.
        Returns:
        A dictionary mapping elements to their respective counts in the formula.
        """
        # Initialize a dictionary to store the element counts
        element_counts = {}

        # Use a regular expression to match elements and counts in the formula
        elements = re.findall(r"([A-Z][a-z]*|[A-Z])([0-9]*\.?[0-9]*)", formula)

        # Iterate over the elements and counts in the formula
        for element, count in elements:
            # If the element is not in the element_counts dictionary, add it with a count of 0
            if element not in element_counts:
                element_counts[element] = 0

            # If the count is not empty, add it to the count for the element
            if count:
                element_counts[element] += float(count)
            # If the count is empty, increment the count for the element by 1
            else:
                element_counts[element] += float(1)

        # Return the element counts dictionary
        return element_counts

    def nonuniquer(self, arr, offset=1e-7):
        """
        Shifts the k-edge in material databases by 0.1 eV to enable interpolation at the edge
        """
        result = arr.copy()  # Create a copy of the input array to work with
        seen_values = {}  # A dictionary to store the count of each value

        for i in range(len(result)):
            if result[i] in seen_values:
                new_value = result[i] + offset
                while new_value in seen_values or new_value in result:
                    # Check for duplicates in both seen values and the new array
                    new_value += offset
                seen_values[new_value] = 1
                result[i] = new_value
            else:
                seen_values[result[i]] = 1
        assert np.all(np.diff(result) > 0), print(result)
        return result

    def _db_scraper(self, material, energies=None):
        """
        Main database scraping tool.
        Looks for each element in the database according to the material string and loads necessary cross-sections
        (Optional) Interpolates cross-sections over the desired energies.
        """

        if material.lower() == "vac":
            if energies is None:
                print("Energies must be defined for vacuum transmission")
            else:
                elist = energies
                clist = np.ones((1, len(energies)))
                return elist, clist[0]
        else:
            data = np.loadtxt(
                f"{self.db_path}{self.name}_{material}.txt", skiprows=self.skiprows
            )
            elist = np.array(data[:, 0])
            clist = np.array(data[:, self.col])
            if energies is None:
                return elist, clist
            else:
                ein2 = self.nonuniquer(elist)
                c3 = pchip(ein2, clist)
                cout = c3(energies)
                return energies, cout

    def _interpolation(self, e, sigma, method=pchip):
        return method(e, sigma)

    def db_scraper(self, material, energies=None):
        """
        Rewrite of the main db_scraper function using pandas
        More flexible for the SRIM database
        """
        assert material in self._materials, (
            f"{material} not present in {self.name} database consider updating repository"
        )

        if material.lower() == "vac":
            assert energies is not None, print(
                "Energies must be defined for vacuum transmission"
            )
            return energies, np.ones(len(energies))
        else:
            match self.name:
                case "SRIM":
                    # print('loading from SRIM')
                    # units conversion for SRIM
                    units = {
                        "eV": 1e-6,
                        "keV": 1e-3,
                        "MeV": 1,
                        "GeV": 1e3,
                    }
                    # by column operators
                    conv = {
                        0: lambda x: x,
                        1: lambda x: units[x[-4:]],
                        2: lambda x: float(x) * 1000,
                        3: lambda x: float(x) * 1000,
                    }

                    data = np.loadtxt(
                        f"{self.db_path}{self.name}_{material}.txt",
                        skiprows=25,
                        max_rows=150,
                        converters=conv,
                        usecols=[0, 1, 2, 3],
                    )

                    e_list = self.nonuniquer(
                        np.array(data[:, 0]) * np.array(data[:, 1])
                    )

                    match self.col:
                        case 1:
                            # Returns only electronic cross-section
                            c_list = np.array(data[:, 1])
                        case 2:
                            # Returns only nuclear cross-section
                            c_list = np.array(data[:, 2])
                        case 3:
                            # Returns summation of both (default)
                            c_list = np.array(data[:, 1]) + np.array(data[:, 2])

                    if energies is not None:
                        c_list = self._interpolation(
                            e_list, c_list, method=self._interpolation_method
                        )(energies)
                        e_list = energies
                    return e_list, c_list

                case _:
                    # tidied up version of the previous function
                    data = np.loadtxt(
                        f"{self.db_path}{self.name}_{material}.txt",
                        skiprows=self.skiprows,
                    )
                    e_list = self.nonuniquer(np.array(data[:, 0]))
                    c_list = np.array(data[:, self.col])
                    if energies is not None:
                        c_list = self._interpolation(
                            e_list, c_list, method=self._interpolation_method
                        )(energies)
                        e_list = energies

                    return e_list, c_list

    def _raw_db_scraper(self, file_string, energies=None):
        """
        Flexibile database scraper, used in testing to evaluate new cross-section
        tables outside of the main database.

        Declare "file_string" as full path to desired file.
        """
        data = np.loadtxt(f"{file_string}", skiprows=self.skiprows)
        elist = np.array(data[:, 0])
        clist = np.array(data[:, self.col])
        if energies is None:
            return elist, clist
        else:
            ein2 = self.nonuniquer(elist)
            c3 = pchip(ein2, clist)
            cout = c3(energies)
            return energies, cout

    def missing_atomic_entries(self):
        """
        Return list of atomic symbols present in the atomic DB but missing as
        individual material files for this Engine instance.
        """
        atomic_symbols = set(self.db["atomic"]["Symbol"].astype(str).tolist())
        missing = sorted(list(atomic_symbols - self._materials))
        return missing
