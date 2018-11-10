import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np
#import matplotlib.pyplot as plt

def sine2(t, data, params, visit):
    a1, omega1, phi1, a2, omega2, phi2, a3, omega3, phi3, a12, omega12, phi12, a22, omega22, phi22, a32, omega32, phi32 = params

    p1 = a1[visit]
    p2 = omega1[visit]
    p3 = phi1[visit]
    p4 = a2[visit]
    p5 = omega2[visit]
    p6 = phi2[visit]
    p7 = a3[visit]
    p8 = omega3[visit]
    scale = phi3[visit]
    #x = a12[visit]

    q1 = a12[visit]
    q2= omega12[visit]
    q3= phi12[visit]
    q4= a22[visit]
    q5= omega22[visit]
    q6= phi22[visit]
    q7= a32[visit]
    q8= omega32[visit]
    #phi32 = phi32[visit]


    #print "a1, omega1, phi1, a2, omega2, a3, omega3, phi3, phi2, a12, omega12, phi12, a22, omega22, phi22, a32, omega32, phi32",  a1, omega1, phi1, a2, omega2, a3, omega3, phi3, phi2, a12, omega12, phi12, a22, omega22, phi22, a32, omega32, phi32 
    omega1 = 20.1621
    omega2 = 21.0606
    omega3 = 8.8436
    omega4 = 24.8835
    omega5 = 20.5353
    omega6 = 34.1252
    omega7 = 8.3084
    omega8 = 10.8249

    a1 = 1.03
    a2 = 1.01
    a3 = 0.86
    a4 =0.45
    a5 = 0.77
    a6 = 0.53
    a7 = 0.68
    a8 = 0.69

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

           
