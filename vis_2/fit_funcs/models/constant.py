import sys
sys.path.insert(0,'..')
import numpy as np
from read_data import Data

def constant(t, data, params):
    C = params
    return 1. + C*np.ones_like(t)
