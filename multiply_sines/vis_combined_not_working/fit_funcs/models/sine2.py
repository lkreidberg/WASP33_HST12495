import sys
sys.path.insert(0,'..')
from read_data import Data
import numpy as np

def sine2(idx, data, params):
    a1, omega1, phi1, a2, omega2, phi2, a12, omega12, phi12, a22, omega22, phi22  = params
    if data.time[idx][0] < 2456300.:
#        print "in here 1", a1, omega1, phi1
        return ( 1. + a1*np.sin(omega1*data.t_vis[idx] + phi1) ) * \
               ( 1. + a2*np.sin(omega2*data.t_vis[idx] + phi2) )
    else:
#        print "in here 2"
        return ( 1. + a12*np.sin(omega12*data.t_vis[idx] + phi12) ) * \
               ( 1. + a22*np.sin(omega22*data.t_vis[idx] + phi22) )
