import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from physics import *

#############################################################################
'''
Histogram

This script includes variables and functions used to define histograms
for distributions of both H0 and H1 magnetic fields.

'''
#############################################################################

######
# H1 #
######

# Sample size
samples = 4999

# Domain for axial and radial components of the RF field
zmin, zmax = -5,5
rmin, rmax = -5,5

# Generate random numbers for z and r
ran_z = (zmax-zmin)*np.random.random_sample((samples))+zmin
ran_r = (rmax-rmin)*np.random.random_sample((samples))+rmin

# Create null arrays to hold the values from the contribution of each field
h1,h2 = np.zeros(samples), np.zeros(samples)

# Calculates the magnetic field using the Biot-Savart Law and its Second
#   derivative for each coil turn on the mxn rectangular coil where the
#   diameter of each turn (wire) is equal to tau and epsilon for horizontal
#   and vertical contributions respectively

# Contribution to field from coil A - integer (random) mode
def histogramCoilA(a,z,rad):
    for epsilon in np.arange(vert):             # Sum over the
       for tau in np.arange(horiz):             # whole coil array
           params = (z,R,epsilon*met)
           a += biot(*params,-tau*met,axisOffset) - biotSecond(*params,-tau*met,axisOffset) * rad**2
    return a

# Contribution to field from coil B - integer (random) mode
def histogramCoilB(a,z,rad):
    for epsilon in np.arange(vert):             # Sum over the
       for tau in np.arange(horiz):             # whole coil array
           params = (z,R,epsilon*met)
           a += biot(*params,tau*met,-axisOffset) - biotSecond(*params,tau*met,-axisOffset) * rad**2
    return a
