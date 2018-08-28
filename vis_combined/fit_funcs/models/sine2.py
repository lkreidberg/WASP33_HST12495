import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np

def sine2(t, data, params, visit):
    a1, omega1, phi1, a2, omega2, phi2, a12, omega12, phi12, a22, omega22, phi22  = params

    a1 = a1[visit]
    omega1 = omega1[visit]
    phi1 = phi1[visit]
    a2 = a2[visit]
    omega2 = omega2[visit]
    phi2 = phi2[visit]

    a12 = a12[visit]
    omega12 = omega12[visit]
    phi12 = phi12[visit]
    a22 = a22[visit]
    omega22 = omega22[visit]
    phi22 = phi22[visit]

    t_vis = data.t_vis[data.vis_idx[visit]]

    if t[0] < 2456300.:
        return ( 1. + a1*np.sin(omega1*t_vis + phi1) ) * \
               ( 1. + a2*np.sin(omega2*t_vis + phi2) )
    else:
        return ( 1. + a12*np.sin(omega12*t_vis + phi12) ) * \
               ( 1. + a22*np.sin(omega22*t_vis + phi22) )

           
