import sys
sys.path.insert(0,'..')
import numpy as np
from read_data import Data

def constant(t, data, params, visit = 0, multi = True):
    C = params
    C = C[visit]
    
    if multi:
        tt = t[data.vis_idx[visit]]
    else:
        tt = t

    return 1. + C*np.ones_like(tt)
