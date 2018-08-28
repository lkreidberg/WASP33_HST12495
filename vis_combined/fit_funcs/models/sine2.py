import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np

def sine2(t, data, params, visit):
    a1, omega1, phi1, a2, omega2, phi2  = params

    a1 = a1[visit]
    omega1 = omega1[visit]
    phi1 = phi1[visit]
    a2 = a2[visit]
    omega2 = omega2[visit]
    phi2 = phi2[visit]

    t_vis = data.t_vis[data.vis_idx[visit]]

    return ( 1. + a1*np.sin(omega1*t_vis + phi1) ) * \
           ( 1. + a2*np.sin(omega2*t_vis + phi2) )
           
