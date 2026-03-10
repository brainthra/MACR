from ..material import Material
from ..library import ENERGIES, ENGINE

# region - G4Nist Materials
ACETONE = Material("C3H6O", 0.7899, genericName="ACETONE", energies=ENERGIES)
ACETYLENE = Material("C2H2", 0.0010967, genericName="ACETYLENE", energies=ENERGIES)
ADENINE = Material("C5H5N5", 1.6, genericName="ADENINE", energies=ENERGIES)
ADIPOSE_TISSUE_ICRP = Material(
    "H0.114C0.598N0.007O0.278Na0.001S0.001Cl0.001",
    0.95,
    genericName="ADIPOSE_TISSUE_ICRP",
    energies=ENERGIES,
)
AIR = Material(
    "C0.000124N0.755268O0.231781Ar0.012827",
    0.00120479,
    genericName="AIR",
    energies=ENERGIES,
)
ALANINE = Material("C3H7NO2", 1.42, genericName="ALANINE", energies=ENERGIES)
ALUMINUM_OXIDE = Material(
    "Al2O3", 3.97, genericName="ALUMINUM_OXIDE", energies=ENERGIES
)
AMBER = Material(
    "H0.10593C0.788974O0.105096", 1.1, genericName="AMBER", energies=ENERGIES
)
AMMONIA = Material("NH3", 0.000826019, genericName="AMMONIA", energies=ENERGIES)
ANILINE = Material("C6H7N", 1.0235, genericName="ANILINE", energies=ENERGIES)
ANTHRACENE = Material("C14H10", 1.283, genericName="ANTHRACENE", energies=ENERGIES)
BAKELITE = Material(
    "H0.057441C0.774591O0.167968", 1.25, genericName="BAKELITE", energies=ENERGIES
)
BARIUM_FLUORIDE = Material(
    "BaF2", 4.89, genericName="BARIUM_FLUORIDE", energies=ENERGIES
)
BARIUM_SULFATE = Material("BaSO4", 4.5, genericName="BARIUM_SULFATE", energies=ENERGIES)
BENZENE = Material("C6H6", 0.87865, genericName="BENZENE", energies=ENERGIES)
BERYLLIUM_OXIDE = Material(
    "BeO", 3.01, genericName="BERYLLIUM_OXIDE", energies=ENERGIES
)
BGO = Material("Bi4Ge3O12", 7.13, genericName="BGO", energies=ENERGIES)
BLOOD_ICRP = Material(
    "H0.102C0.11N0.033O0.745Na0.001P0.001S0.002Cl0.003K0.002Fe0.001",
    1.06,
    genericName="BLOOD_ICRP",
    energies=ENERGIES,
)
BONE_COMPACT_ICRU = Material(
    "H0.064C0.278N0.027O0.41Mg0.002P0.07S0.002Ca0.147",
    1.85,
    genericName="BONE_COMPACT_ICRU",
    energies=ENERGIES,
)
BONE_CORTICAL_ICRP = Material(
    "H0.034C0.155N0.042O0.435Na0.001Mg0.002P0.103S0.003Ca0.225",
    1.92,
    genericName="BONE_CORTICAL_ICRP",
    energies=ENERGIES,
)
BORON_CARBIDE = Material("B4C", 2.52, genericName="BORON_CARBIDE", energies=ENERGIES)
BORON_OXIDE = Material("B2O3", 1.812, genericName="BORON_OXIDE", energies=ENERGIES)
BRAIN_ICRP = Material(
    "H0.107C0.145N0.022O0.712Na0.002P0.004S0.002Cl0.003K0.003",
    1.04,
    genericName="BRAIN_ICRP",
    energies=ENERGIES,
)
BUTANE = Material("C4H10", 0.00249343, genericName="BUTANE", energies=ENERGIES)
CADMIUM_TELLURIDE = Material(
    "CdTe", 6.2, genericName="CADMIUM_TELLURIDE", energies=ENERGIES
)
CADMIUM_TUNGSTATE = Material(
    "CdWO4", 7.9, genericName="CADMIUM_TUNGSTATE", energies=ENERGIES
)
CALCIUM_CARBONATE = Material(
    "CaCO3", 2.8, genericName="CALCIUM_CARBONATE", energies=ENERGIES
)
CALCIUM_FLUORIDE = Material(
    "CaF2", 3.18, genericName="CALCIUM_FLUORIDE", energies=ENERGIES
)
CALCIUM_OXIDE = Material("CaO", 3.3, genericName="CALCIUM_OXIDE", energies=ENERGIES)
CALCIUM_SULFATE = Material(
    "CaSO4", 2.96, genericName="CALCIUM_SULFATE", energies=ENERGIES
)
CALCIUM_TUNGSTATE = Material(
    "CaWO4", 6.062, genericName="CALCIUM_TUNGSTATE", energies=ENERGIES
)
CARBON_DIOXIDE = Material(
    "CO2", 0.00184212, genericName="CARBON_DIOXIDE", energies=ENERGIES
)
CARBON_TETRACHLORIDE = Material(
    "CCl4", 1.594, genericName="CARBON_TETRACHLORIDE", energies=ENERGIES
)
CELLULOSE_CELLOPHANE = Material(
    "C6H10O5", 1.42, genericName="CELLULOSE_CELLOPHANE", energies=ENERGIES
)
CELLULOSE_BUTYRATE = Material(
    "H0.067125C0.545403O0.387472",
    1.2,
    genericName="CELLULOSE_BUTYRATE",
    energies=ENERGIES,
)
CELLULOSE_NITRATE = Material(
    "H0.029216C0.271296N0.121276O0.578212",
    1.49,
    genericName="CELLULOSE_NITRATE",
    energies=ENERGIES,
)
CERIC_SULFATE = Material(
    "H0.107596N0.0008O0.874976S0.014627Ce0.002001",
    1.03,
    genericName="CERIC_SULFATE",
    energies=ENERGIES,
)
CESIUM_FLUORIDE = Material(
    "CsF", 4.115, genericName="CESIUM_FLUORIDE", energies=ENERGIES
)
CESIUM_IODIDE = Material("CsI", 4.51, genericName="CESIUM_IODIDE", energies=ENERGIES)
CHLOROBENZENE = Material(
    "C6H5Cl", 1.1058, genericName="CHLOROBENZENE", energies=ENERGIES
)
CHLOROFORM = Material("CHCl3", 1.4832, genericName="CHLOROFORM", energies=ENERGIES)
CONCRETE = Material(
    "H0.01C0.001O0.529107Na0.016Mg0.002Al0.033872Si0.337021K0.013Ca0.044Fe0.014",
    2.3,
    genericName="CONCRETE",
    energies=ENERGIES,
)
CYCLOHEXANE = Material("C6H12", 0.779, genericName="CYCLOHEXANE", energies=ENERGIES)
DICHLORODIETHYL_ETHER = Material(
    "C4H8OCl2", 1.2199, genericName="DICHLORODIETHYL_ETHER", energies=ENERGIES
)
DIETHYL_ETHER = Material(
    "C4H10O", 0.71378, genericName="DIETHYL_ETHER", energies=ENERGIES
)
DIMETHYL_SULFOXIDE = Material(
    "C2H6OS", 1.1014, genericName="DIMETHYL_SULFOXIDE", energies=ENERGIES
)
ETHANE = Material("C2H6", 0.00125324, genericName="ETHANE", energies=ENERGIES)
ETHYL_ALCOHOL = Material(
    "C2H6O", 0.7893, genericName="ETHYL_ALCOHOL", energies=ENERGIES
)
ETHYL_CELLULOSE = Material(
    "H0.090027C0.585182O0.324791",
    1.13,
    genericName="ETHYL_CELLULOSE",
    energies=ENERGIES,
)
ETHYLENE = Material("C2H4", 0.00117497, genericName="ETHYLENE", energies=ENERGIES)
EYE_LENS_ICRP = Material(
    "H0.096C0.195N0.057O0.646Na0.001P0.001S0.003Cl0.001",
    1.07,
    genericName="EYE_LENS_ICRP",
    energies=ENERGIES,
)
FERRIC_OXIDE = Material("Fe2O3", 5.2, genericName="FERRIC_OXIDE", energies=ENERGIES)
FERROBORIDE = Material("FeB", 7.15, genericName="FERROBORIDE", energies=ENERGIES)
FERROUS_OXIDE = Material("FeO", 5.7, genericName="FERROUS_OXIDE", energies=ENERGIES)
FERROUS_SULFATE = Material(
    "H0.108259N2.7e-05O0.878636Na2.2e-05S0.012968Cl3.4e-05Fe5.4e-05",
    1.024,
    genericName="FERROUS_SULFATE",
    energies=ENERGIES,
)
GADOLINIUM_OXYSULFIDE = Material(
    "Gd2O2S", 7.44, genericName="GADOLINIUM_OXYSULFIDE", energies=ENERGIES
)
GALLIUM_ARSENIDE = Material(
    "GaAs", 5.31, genericName="GALLIUM_ARSENIDE", energies=ENERGIES
)
GEL_PHOTO_EMULSION = Material(
    "H0.08118C0.41606N0.11124O0.38064S0.01088",
    1.2914,
    genericName="GEL_PHOTO_EMULSION",
    energies=ENERGIES,
)
Pyrex_Glass = Material(
    "B0.0400639O0.539561Na0.0281909Al0.011644Si0.377219K0.00332099",
    2.23,
    genericName="Pyrex_Glass",
    energies=ENERGIES,
)
GLASS_LEAD = Material(
    "O0.156453Si0.080866Ti0.008092As0.002651Pb0.751938",
    6.22,
    genericName="GLASS_LEAD",
    energies=ENERGIES,
)
GLASS_PLATE = Material(
    "O0.4598Na0.0964411Si0.336553Ca0.107205",
    2.4,
    genericName="GLASS_PLATE",
    energies=ENERGIES,
)
GLUTAMINE = Material("C5H10N2O3", 1.46, genericName="GLUTAMINE", energies=ENERGIES)
GLYCEROL = Material("C3H8O3", 1.2613, genericName="GLYCEROL", energies=ENERGIES)
GUANINE = Material("C5H5N5O", 2.2, genericName="GUANINE", energies=ENERGIES)
GYPSUM = Material("CaSO6H4", 2.32, genericName="GYPSUM", energies=ENERGIES)
KAPTON = Material("C22H10N2O5", 1.42, genericName="KAPTON", energies=ENERGIES)
LANTHANUM_OXYBROMIDE = Material(
    "LaBrO", 6.28, genericName="LANTHANUM_OXYBROMIDE", energies=ENERGIES
)
LANTHANUM_OXYSULFIDE = Material(
    "La2O2S", 5.86, genericName="LANTHANUM_OXYSULFIDE", energies=ENERGIES
)
LEAD_OXIDE = Material(
    "O0.071682Pb0.928318", 9.53, genericName="LEAD_OXIDE", energies=ENERGIES
)
LITHIUM_AMIDE = Material("LiNH2", 1.178, genericName="LITHIUM_AMIDE", energies=ENERGIES)
LITHIUM_CARBONATE = Material(
    "Li2CO3", 2.11, genericName="LITHIUM_CARBONATE", energies=ENERGIES
)
LITHIUM_FLUORIDE = Material(
    "LiF", 2.635, genericName="LITHIUM_FLUORIDE", energies=ENERGIES
)
LITHIUM_HYDRIDE = Material(
    "LiH", 0.82, genericName="LITHIUM_HYDRIDE", energies=ENERGIES
)
LITHIUM_IODIDE = Material("LiI", 3.494, genericName="LITHIUM_IODIDE", energies=ENERGIES)
LITHIUM_OXIDE = Material("Li2O", 2.013, genericName="LITHIUM_OXIDE", energies=ENERGIES)
LITHIUM_TETRABORATE = Material(
    "Li2B4O7", 2.44, genericName="LITHIUM_TETRABORATE", energies=ENERGIES
)
LUNG_ICRP = Material(
    "H0.105C0.083N0.023O0.779Na0.002P0.001S0.002Cl0.003K0.002",
    1.04,
    genericName="LUNG_ICRP",
    energies=ENERGIES,
)
M3_WAX = Material(
    "H0.114318C0.655824O0.0921831Mg0.134792Ca0.002883",
    1.05,
    genericName="M3_WAX",
    energies=ENERGIES,
)
MAGNESIUM_CARBONATE = Material(
    "MgCO3", 2.958, genericName="MAGNESIUM_CARBONATE", energies=ENERGIES
)
MAGNESIUM_FLUORIDE = Material(
    "MgF2", 3.0, genericName="MAGNESIUM_FLUORIDE", energies=ENERGIES
)
MAGNESIUM_OXIDE = Material(
    "MgO", 3.58, genericName="MAGNESIUM_OXIDE", energies=ENERGIES
)
MAGNESIUM_TETRABORATE = Material(
    "MgB4O7", 2.53, genericName="MAGNESIUM_TETRABORATE", energies=ENERGIES
)
MERCURIC_IODIDE = Material(
    "HgI2", 6.36, genericName="MERCURIC_IODIDE", energies=ENERGIES
)
METHANE = Material("CH4", 0.000667151, genericName="METHANE", energies=ENERGIES)
METHANOL = Material("CH4O", 0.7914, genericName="METHANOL", energies=ENERGIES)
MIX_D_WAX = Material(
    "H0.13404C0.77796O0.03502Mg0.038594Ti0.014386",
    0.99,
    genericName="MIX_D_WAX",
    energies=ENERGIES,
)
MS20_TISSUE = Material(
    "H0.081192C0.583442N0.017798O0.186381Mg0.130287Cl0.0009",
    1.0,
    genericName="MS20_TISSUE",
    energies=ENERGIES,
)
MUSCLE_SKELETAL_ICRP = Material(
    "H0.102C0.143N0.034O0.71Na0.001P0.002S0.003Cl0.001K0.004",
    1.05,
    genericName="MUSCLE_SKELETAL_ICRP",
    energies=ENERGIES,
)
MUSCLE_STRIATED_ICRU = Material(
    "H0.102102C0.123123N0.035035O0.72973Na0.001001P0.002002S0.004004K0.003003",
    1.04,
    genericName="MUSCLE_STRIATED_ICRU",
    energies=ENERGIES,
)
MUSCLE_WITH_SUCROSE = Material(
    "H0.0982341C0.156214N0.035451O0.710101",
    1.11,
    genericName="MUSCLE_WITH_SUCROSE",
    energies=ENERGIES,
)
MUSCLE_WITHOUT_SUCROSE = Material(
    "H0.101969C0.120058N0.035451O0.742522",
    1.07,
    genericName="MUSCLE_WITHOUT_SUCROSE",
    energies=ENERGIES,
)
NAPHTHALENE = Material("C10H8", 1.145, genericName="NAPHTHALENE", energies=ENERGIES)
NITROBENZENE = Material(
    "C6H5NO2", 1.19867, genericName="NITROBENZENE", energies=ENERGIES
)
NITROUS_OXIDE = Material(
    "N2O", 0.00183094, genericName="NITROUS_OXIDE", energies=ENERGIES
)
OCTANE = Material("C8H18", 0.7026, genericName="OCTANE", energies=ENERGIES)
PARAFFIN = Material("C25H52", 0.93, genericName="PARAFFIN", energies=ENERGIES)
PHOTO_EMULSION = Material(
    "H0.0141C0.072261N0.01932O0.066101S0.00189Br0.349103Ag0.474105I0.00312",
    3.815,
    genericName="PHOTO_EMULSION",
    energies=ENERGIES,
)
PLASTIC_SC_VINYLTOLUENE = Material(
    "C9H10", 1.032, genericName="PLASTIC_SC_VINYLTOLUENE", energies=ENERGIES
)
PLUTONIUM_DIOXIDE = Material(
    "PuO2", 11.46, genericName="PLUTONIUM_DIOXIDE", energies=ENERGIES
)
POLYACRYLONITRILE = Material(
    "C3H3N", 1.17, genericName="POLYACRYLONITRILE", energies=ENERGIES
)
POLYCARBONATE = Material(
    "C16H14O3", 1.2, genericName="POLYCARBONATE", energies=ENERGIES
)
POLYCHLOROSTYRENE = Material(
    "C8H7Cl", 1.3, genericName="POLYCHLOROSTYRENE", energies=ENERGIES
)
POLYETHYLENE = Material("CH2", 0.94, genericName="POLYETHYLENE", energies=ENERGIES)
MYLAR = Material("C10H8O4", 1.4, genericName="MYLAR", energies=ENERGIES)
PLEXIGLASS = Material("C5H8O2", 1.19, genericName="PLEXIGLASS", energies=ENERGIES)
POLYOXYMETHYLENE = Material(
    "CH2O", 1.425, genericName="POLYOXYMETHYLENE", energies=ENERGIES
)
POLYPROPYLENE = Material("C2H4", 0.9, genericName="POLYPROPYLENE", energies=ENERGIES)
POLYSTYRENE = Material("C8H8", 1.06, genericName="POLYSTYRENE", energies=ENERGIES)
TEFLON = Material("C2F4", 2.2, genericName="TEFLON", energies=ENERGIES)
POLYTRIFLUOROCHLOROETHYLENE = Material(
    "C2F3Cl", 2.1, genericName="POLYTRIFLUOROCHLOROETHYLENE", energies=ENERGIES
)
POLYVINYL_ACETATE = Material(
    "C4H6O2", 1.19, genericName="POLYVINYL_ACETATE", energies=ENERGIES
)
POLYVINYL_ALCOHOL = Material(
    "C2H4O", 1.3, genericName="POLYVINYL_ALCOHOL", energies=ENERGIES
)
POLYVINYL_BUTYRAL = Material(
    "C8H14O2", 1.12, genericName="POLYVINYL_BUTYRAL", energies=ENERGIES
)
POLYVINYL_CHLORIDE = Material(
    "C2H3Cl", 1.3, genericName="POLYVINYL_CHLORIDE", energies=ENERGIES
)
POLYVINYLIDENE_CHLORIDE = Material(
    "C2H2Cl2", 1.7, genericName="POLYVINYLIDENE_CHLORIDE", energies=ENERGIES
)
POLYVINYLIDENE_FLUORIDE = Material(
    "C2H2F2", 1.76, genericName="POLYVINYLIDENE_FLUORIDE", energies=ENERGIES
)
POLYVINYL_PYRROLIDONE = Material(
    "C6H9NO", 1.25, genericName="POLYVINYL_PYRROLIDONE", energies=ENERGIES
)
POTASSIUM_IODIDE = Material(
    "KI", 3.13, genericName="POTASSIUM_IODIDE", energies=ENERGIES
)
POTASSIUM_OXIDE = Material(
    "K2O", 2.32, genericName="POTASSIUM_OXIDE", energies=ENERGIES
)
PROPANE = Material("C3H8", 0.00187939, genericName="PROPANE", energies=ENERGIES)
lPROPANE = Material("C3H8", 0.43, genericName="lPROPANE", energies=ENERGIES)
PYRIDINE = Material("C5H5N", 0.9819, genericName="PYRIDINE", energies=ENERGIES)
RUBBER_BUTYL = Material(
    "H0.143711C0.856289", 0.92, genericName="RUBBER_BUTYL", energies=ENERGIES
)
RUBBER_NATURAL = Material(
    "H0.118371C0.881629", 0.92, genericName="RUBBER_NATURAL", energies=ENERGIES
)
RUBBER_NEOPRENE = Material(
    "H0.05692C0.542646Cl0.400434",
    1.23,
    genericName="RUBBER_NEOPRENE",
    energies=ENERGIES,
)
SILICON_DIOXIDE = Material(
    "SiO2", 2.32, genericName="SILICON_DIOXIDE", energies=ENERGIES
)
SILVER_BROMIDE = Material(
    "AgBr", 6.473, genericName="SILVER_BROMIDE", energies=ENERGIES
)
SILVER_CHLORIDE = Material(
    "AgCl", 5.56, genericName="SILVER_CHLORIDE", energies=ENERGIES
)
SILVER_HALIDES = Material(
    "Br0.422895Ag0.573748I0.003357",
    6.47,
    genericName="SILVER_HALIDES",
    energies=ENERGIES,
)
SILVER_IODIDE = Material("AgI", 6.01, genericName="SILVER_IODIDE", energies=ENERGIES)
SKIN_ICRP = Material(
    "H0.1C0.204N0.042O0.645Na0.002P0.001S0.002Cl0.003K0.001",
    1.09,
    genericName="SKIN_ICRP",
    energies=ENERGIES,
)
SODIUM_CARBONATE = Material(
    "Na2CO3", 2.532, genericName="SODIUM_CARBONATE", energies=ENERGIES
)
SODIUM_IODIDE = Material("NaI", 3.667, genericName="SODIUM_IODIDE", energies=ENERGIES)
SODIUM_MONOXIDE = Material(
    "Na2O", 2.27, genericName="SODIUM_MONOXIDE", energies=ENERGIES
)
SODIUM_NITRATE = Material(
    "NaNO3", 2.261, genericName="SODIUM_NITRATE", energies=ENERGIES
)
STILBENE = Material("C14H12", 0.9707, genericName="STILBENE", energies=ENERGIES)
SUCROSE = Material("C12H22O11", 1.5805, genericName="SUCROSE", energies=ENERGIES)
TERPHENYL = Material("C18H14", 1.24, genericName="TERPHENYL", energies=ENERGIES)
TESTIS_ICRP = Material(
    "H0.106C0.099N0.02O0.766Na0.002P0.001S0.002Cl0.002K0.002",
    1.04,
    genericName="TESTIS_ICRP",
    energies=ENERGIES,
)
TETRACHLOROETHYLENE = Material(
    "C2Cl4", 1.625, genericName="TETRACHLOROETHYLENE", energies=ENERGIES
)
THALLIUM_CHLORIDE = Material(
    "TlCl", 7.004, genericName="THALLIUM_CHLORIDE", energies=ENERGIES
)
TISSUE_SOFT_ICRP = Material(
    "H0.105C0.256N0.027O0.602Na0.001P0.002S0.003Cl0.002K0.002",
    1.03,
    genericName="TISSUE_SOFT_ICRP",
    energies=ENERGIES,
)
TITANIUM_DIOXIDE = Material(
    "TiO2", 4.26, genericName="TITANIUM_DIOXIDE", energies=ENERGIES
)
TOLUENE = Material("C7H8", 0.8669, genericName="TOLUENE", energies=ENERGIES)
TRICHLOROETHYLENE = Material(
    "C2HCl3", 1.46, genericName="TRICHLOROETHYLENE", energies=ENERGIES
)
TRIETHYL_PHOSPHATE = Material(
    "C6H15O4P", 1.07, genericName="TRIETHYL_PHOSPHATE", energies=ENERGIES
)
TUNGSTEN_HEXAFLUORIDE = Material(
    "WF6", 2.4, genericName="TUNGSTEN_HEXAFLUORIDE", energies=ENERGIES
)
URANIUM_DICARBIDE = Material(
    "UC2", 11.28, genericName="URANIUM_DICARBIDE", energies=ENERGIES
)
URANIUM_MONOCARBIDE = Material(
    "UC", 13.63, genericName="URANIUM_MONOCARBIDE", energies=ENERGIES
)
URANIUM_OXIDE = Material("UO2", 10.96, genericName="URANIUM_OXIDE", energies=ENERGIES)
UREA = Material("CH4N2O", 1.323, genericName="UREA", energies=ENERGIES)
VALINE = Material("C5H11NO2", 1.23, genericName="VALINE", energies=ENERGIES)
VITON = Material(
    "H0.009417C0.280555F0.710028", 1.8, genericName="VITON", energies=ENERGIES
)
WATER = Material("H2O", 1.0, genericName="WATER", energies=ENERGIES)
WATER_VAPOR = Material("H2O", 0.000756182, genericName="WATER_VAPOR", energies=ENERGIES)
XYLENE = Material("C8H10", 0.87, genericName="XYLENE", energies=ENERGIES)
GRAPHITE = Material("C", 2.21, genericName="GRAPHITE", energies=ENERGIES)
# endregion - NIST Compounds
