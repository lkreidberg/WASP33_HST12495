import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np
import matplotlib.pyplot as plt

def sine2(t, data, params):
    a1, omega1, phi1, a2, omega2, phi2, a3, omega3, phi3 = params
    print a1, omega1, phi1, a2, omega2, phi2, a3, omega3, phi3 
    #FIXME data.t_vis won't work if there are multiple visits
    TWOPI = np.pi*2.
    #print data.t_vis
    """lc = ( 1. + a1*np.sin(TWOPI*omega1*data.t_vis + phi1)  
                + a2*np.sin(TWOPI*omega2*data.t_vis + phi2) 
                + a3*np.sin(TWOPI*omega3*data.t_vis + phi3) 
            )
    plt.plot(data.t_vis, lc, '.k')
    plt.show()"""

    return ( 1. + a1*np.sin(TWOPI*omega1*data.t_vis + phi1)  
                + a2*np.sin(TWOPI*omega2*data.t_vis + phi2) 
                + a3*np.sin(TWOPI*omega3*data.t_vis + phi3) 
            )
           
