import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np
#import matplotlib.pyplot as plt

def vonessen(t, data, params, visit):
    scale, a1, a2, a3, a4, a5, a6, a7, a8, p1, p2, p3, p4, p5, p6, p7, p8, q1, q2, q3, q4, q5, q6, q7, q8 = params 
    
    scale = scale[visit]
    a1 = a1[visit] 
    a2 = a2[visit] 
    a3 = a3[visit] 
    a4 = a4[visit] 
    a5 = a5[visit] 
    a6 = a6[visit] 
    a7 = a7[visit] 
    a8 = a8[visit] 
    p1 = p1[visit]
    p2 = p2[visit]
    p3 = p3[visit]
    p4 = p4[visit]
    p5 = p5[visit]
    p6 = p6[visit]
    p7 = p7[visit]
    p8 = p8[visit]
    q1 = q1[visit]
    q2 = q2[visit]
    q3 = q3[visit]
    q4 = q4[visit]
    q5 = q5[visit]
    q6 = q6[visit]
    q7 = q7[visit]
    q8 = q8[visit]

    omega1 = 20.1621
    omega2 = 21.0606
    omega3 = 8.8436
    omega4 = 24.8835
    omega5 = 20.5353
    omega6 = 34.1252
    omega7 = 8.3084
    omega8 = 10.8249

    """a1 = 1.03
    a2 = 1.01
    a3 = 0.86
    a4 =0.45
    a5 = 0.77
    a6 = 0.53
    a7 = 0.68
    a8 = 0.69"""

    a1 *= scale
    a2 *= scale
    a3 *= scale
    a4 *= scale
    a5 *= scale
    a6 *= scale
    a7 *= scale
    a8 *= scale

    TWOPI = np.pi*2.

    t_vis = data.t_vis[data.vis_idx[visit]]

    if t[0] > 2456300.:
        return ( 1. + a1*np.sin(TWOPI*omega1*t_vis + p1) 
                    + a2*np.sin(TWOPI*omega2*t_vis + p2) 
                    + a3*np.sin(TWOPI*omega3*t_vis + p3) 
                    + a4*np.sin(TWOPI*omega4*t_vis + p4) 
                    + a5*np.sin(TWOPI*omega5*t_vis + p5) 
                    + a6*np.sin(TWOPI*omega6*t_vis + p6) 
                    + a7*np.sin(TWOPI*omega7*t_vis + p7) 
                    + a8*np.sin(TWOPI*omega8*t_vis + p8) 
               )
    else:
        return ( 1. + a1*np.sin(TWOPI*omega1*t_vis + q1 ) 
                    + a2*np.sin(TWOPI*omega2*t_vis + q2 ) 
                    + a3*np.sin(TWOPI*omega3*t_vis + q3 ) 
                    + a4*np.sin(TWOPI*omega4*t_vis + q4 ) 
                    + a5*np.sin(TWOPI*omega5*t_vis + q5 ) 
                    + a6*np.sin(TWOPI*omega6*t_vis + q6 ) 
                    + a7*np.sin(TWOPI*omega7*t_vis + q7 ) 
                    + a8*np.sin(TWOPI*omega8*t_vis + q8 )
                )

           
