import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np
import matplotlib.pyplot as plt

def sine2(t, data, params, visit):
    a1, omega1, b1, a2, omega2, b2, a3, omega3, b3, a12, omega12, b12, a22, omega22, b22, a32, omega32, b32 = params

    a1 = a1[visit]
    omega1 = omega1[visit]
    b1 = b1[visit]
    a2 = a2[visit]
    omega2 = omega2[visit]
    b2 = b2[visit]
    a3 = a3[visit]
    omega3 = omega3[visit]
    b3 = b3[visit]

    a12 = a12[visit]
    omega12 = omega1 
    b12 = b12[visit]
    a22 = a22[visit]
    omega22 = omega2
    b22 = b22[visit]
    a32 = a32[visit]
    omega32 = omega3
    b32 = b32[visit]


    TWOPI = np.pi*2.

    t_vis = data.t_vis[data.vis_idx[visit]]
    t = np.linspace(t[0], t[-1], 1000)

    if t[0] < 2456300.:
        return ( 1. + a1*np.sin(TWOPI*omega1*t_vis) + b1*np.cos(TWOPI*omega1*t_vis)
                    + a2*np.sin(TWOPI*omega2*t_vis) + b2*np.cos(TWOPI*omega2*t_vis) 
                    + a3*np.sin(TWOPI*omega3*t_vis) + b3*np.cos(TWOPI*omega3*t_vis)
               )
    else:
        return ( 1. + a12*np.sin(TWOPI*omega12*t_vis) + b12*np.cos(TWOPI*omega12*t_vis) 
                    + a22*np.sin(TWOPI*omega22*t_vis) + b22*np.cos(TWOPI*omega22*t_vis) 
                    + a32*np.sin(TWOPI*omega32*t_vis) + b32*np.cos(TWOPI*omega32*t_vis) 
               )

           
