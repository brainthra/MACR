from ..material import Material, Scintillator
from ..system import Layer, System
from ..library import ENERGIES, ENGINE

# region - Scintillators
_anthracene_constant = 16
ANTHRACENE = Scintillator(
    "C14H10",
    1.283,
    genericName="ANTHRACENE",
     energies=ENERGIES, engine=ENGINE,
    kappa=_anthracene_constant,
)
GADOX = Scintillator("Gd2O2S", 7.44, genericName="Gadox",  energies=ENERGIES, engine=ENGINE, kappa=60)
LANEX = Scintillator("Gd2O2S", 7.44, genericName="Lanex",  energies=ENERGIES, engine=ENGINE, kappa=60)
LSO = Scintillator("Lu2SiO5", 7.4, genericName="LSO",  energies=ENERGIES, engine=ENGINE, kappa=30)
LYSO = Scintillator(
    "Lu1.8Y0.2SiO5", 7.15, genericName="LYSO",  energies=ENERGIES, engine=ENGINE, kappa=25
)
LuAG = Scintillator("Lu3Al5O12", 6.3, genericName="LuAG",  energies=ENERGIES, engine=ENGINE, kappa=25)
BGO = Scintillator("Bi4Ge3O12", 7.13, genericName="BGO",  energies=ENERGIES, engine=ENGINE, kappa=9)
YAG = Scintillator("Y3Al5O12", 4.55, genericName="YAG",  energies=ENERGIES, engine=ENGINE, kappa=35)
CsI = Scintillator("CsI", 4.51, genericName="CsI",  energies=ENERGIES, engine=ENGINE, kappa=54)
CH = Scintillator(
    "C8H8", 1.06, genericName="CH",  energies=ENERGIES, engine=ENGINE, kappa=0.56 * _anthracene_constant
)
# endregion - Scintillators
