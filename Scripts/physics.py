#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:07:41 2017

@author: jasonfakidis
"""

import numpy as np
import matplotlib.pyplot as plt


#############################################################################
'''
Physics

Define physical constants to be used throughout the program. Also define
equations governing the physics of the experiment. A normal distribution
function is included. Also, RF coil geometry is defined.
'''
#############################################################################

#######################
# Physical Constants  #
#######################

# Physical Constants
mu_naught = 4*np.pi
I = 1
constant = mu_naught * I / 2

# Stable and RF field magnitudes
h_0 = 100
h_1 = 3 # Gauss

# Gyromagnetic ratio and angular frequency (set to resonance)
gamma = 2*np.pi*0.630*1000 # Hz/G
omega = gamma * h_0


##################
# Coil Geometry  #
##################

# Coil geometry
vert = 5
horiz = 5

# Unit conversion
met = 1 # Unit conversion

# Parameters - Defined by geometry
axisOffset = 25/2
R = 25/2

##############################
# Time and Frequency Arrays  #
##############################

# Domain (time) values for the polarization signal [s]
tmin,tmax,time_step = 0,0.2,4000
t = np.linspace(tmin,tmax,time_step)

# Domain (frequency) values for the plots of the Amplitude of
#   the polarization and the total field [Hz]
wmin,wmax,wstep = 0,800,800
w = np.linspace(wmin,wmax,wstep)

#############################################################################
'''Equations'''
#############################################################################

# Biot-Savart Law
def biot(z,R,epsilon,tau,aOffset):

    # epsilon, tau - incremental offset parameters to represent individual
    #                   turns on the RF cable

    indep = (z+tau+aOffset)
    return constant * (R+epsilon)**2 / ((R+epsilon)**2+(indep)**2)**1.5

#Biot-Savart Law - First Derivative
def biotFirst(z,R,sep):
    indep = (z+tau+aOffset)
    return constant * -3 * (R+epsilon)**2 * indep / (indep**2 + (R+epsilon)**2)**2.5

# Biot-Savart Law - Second Derivative
def biotSecond(z,R,epsilon,tau,aOffset):
    indep = (z+tau+aOffset)
    return constant * ( 15 * (R+epsilon)**2 * indep**2  / (((R+epsilon)**2 + (indep)**2)**(7/2)) - 3 * (R+epsilon)**2 /
             (((R+epsilon)**2 + (indep)**2)**(5/2)))

# Amplitude of the signal
def sin_squared_theta(h_0):
    sin_theta_squared = h_1**2 / ( (h_0-omega/gamma)**2 + h_1**2 )
    return sin_theta_squared

# Constant Term
def cos_squared_theta(h_0):
    cos_theta_squared = ( h_0 - omega/gamma )**2 / ( (h_0-omega/gamma)**2 + h_1**2 )
    return cos_theta_squared

# Total Magnetic Field
def h_tot(h_0):
    h_tot = np.sqrt( h_1**2 + (h_0-omega/gamma)**2 )
    return h_tot

# Polarization Signal
def signal(h_0,probability):
    signal = ( cos_squared_theta(h_0) + sin_squared_theta(h_0) * np.cos( h_tot(h_0) * gamma * t) ) * probability
    return signal

# Normal Distribution
def probability(h_0,mu,sigma):
    gaussian = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (h_0 - mu)**2 / (2 * sigma**2))
    return gaussian
