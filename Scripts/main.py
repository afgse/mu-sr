import numpy as np
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
from scipy.stats import norm

# in this order
from physics import *
from histogram import *
from distribution import *

'''
Main

Create histograms for both the H1 and H0 fields with normal distributions then
use these values to calculate the polarization signal. The peak values of the
polarization signal are also calculated.
'''

#############################################################################
'''Histograms'''
#############################################################################

######
# H0 #
######

sample_size,bin_amount = 100,100

# Define mu and sigma for H0 normal distribution
mu_h0, sigma_h0 = h_0, 1

# Pull random samples of H0 from its normal distribution
s = np.random.normal(mu_h0, sigma_h0, sample_size)

######
# H1 #
######

# Create a set of randomly generated samples for H1
h = histogramCoilA(h1,ran_z,ran_r) + histogramCoilB(h2,ran_z,ran_r)

# Fit h to a normal distribution. Find mu, sigma
h1_mu, h1_sigma = norm.fit(h)

#############################################################################
'''Calculations'''
#############################################################################

#################
# Distributions #
#################
# Calculate the axial distribution
axialCoilA(a1)
axialCoilB(a2)
a = a1 + a2

# Calculate the radial distribution
radialCoilA(r1)
radialCoilB(r2)
r = r1 + r2

##########
# Signal #
##########

# Initialize an array to hold the signal values.
# time_step (defined in physics.py) is equal in size
# to array t. Also define an empty integer to hold
# the sum of probabilites.
signal_array = np.zeros(time_step)
weighting_factor_array = 0

# Calculate signal for all random H0
for i in s:
    signal_array +=  signal(i,probability(i,mu_h0,sigma_h0))
    weighting_factor_array += probability(i,mu_h0,sigma_h0)

# Divide by the weighting factor
signal_array = ( 1 / weighting_factor_array ) * signal_array

################
# Signal Peaks #
################

peaks = find_peaks_cwt(signal_array,[1])

t_peak = t[peaks]
signal_peak = signal_array[peaks]
