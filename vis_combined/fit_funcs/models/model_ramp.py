import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np

def model_ramp(idx, data, params):
    r1, r2, r3, r12, r22, r32 = params
    if data.time[idx][0] < 2456300.:
        print "vis 1, time", data.time[idx][0], r1, r2, r3
        return 1.0 - np.exp(-r1*data.t_orb[idx] - r2 - r3*data.t_delay[idx])
    else:
        print "vis 2, time", data.time[idx][0], r12, r22, r32
        return 1.0 - np.exp(-r12*data.t_orb[idx] - r22 - r32*data.t_delay[idx])
