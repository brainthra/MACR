import numpy as np
from ..engine import Engine

# Declarations up top for rest of system, can all be redefined during calls
ENERGIES = np.geomspace(0.01, 1, 10000)
ENGINE = Engine("NIST")  # feature complete, changes to other engines might cause errors

from . import elements as elements
from . import g4nist as g4nist
from . import rcf as rcf
from . import scintillators as scintillators
from . import ip as ip

# for those who want access to everything without importing each submodule
from .elements import *
from .g4nist import *
from .rcf import *
from .scintillators import *
from .ip import *