import numpy as np
import matplotlib.pyplot as plt
from physics import *

'''
Distribution

Calculates the magnetic field distribution along z (axial) and radially outwards
from z. The calculation is done by calculating the Biot-Savart contributions
for all turns in the mxn rectangular RF coil.
'''

###############
# Axial #
###############

    # Define a domain of z values along the axis of
    # the RF coil
minimumZ, maximumZ, stepZ = -60,60,200

    # Initialize two empty arrays (filled with zeros) which will hold
    # the magnetic field values along the z-domain
a1, a2 = np.zeros(stepZ), np.zeros(stepZ)

    # Define an array of z values corresponding to the domain
    # initiated above
axialZ = np.linspace(minimumZ,maximumZ,stepZ)

# The following functions work by adding the values of each wire in each coil
# to the previously initialized arrays (1 function per coil).
# Here vert and horiz are the vertical
# and horizontal size of the coil in windings. An nxm coil would have
# n horizontal turns and m vertical turns. The calculation assumes that
# the diameter of each wire is 1 mm. The calculation starts at the bottom right
# of the coil array (n,m) = (0,0) and continues along each row leftwards. See
# report for clarification

# This function calculates the contribution to the magnetic field from
# the first coil in the pair. The left coil.
def axialCoilA(array):
    for epsilon in np.arange(vert):             # For each vertical row in the coil
       for tau in np.arange(horiz):             # For each horizontal column in the coil
           # params: The three parameters are z, the radius of the coil and the wire
           # offset epsilon. An array containing all the z-values of interest (axialZ) is
           # passed to the z parameter. R is the radius of the coil. The wire offset epsilon
           # is used here to increment through the vertical wires. As epsilon increases
           # according to the loop the radius will increase by an amount R = R + \epsilon.
           # See definition of the biot function in physics.py for clarification.
           params = (axialZ,R,epsilon*met)
           # Tau and axisOffset are passed as the final parameters to the biot function.
           # Tau serves the same purpose as epsilon (above) except in the horizontal direction.
           # That is, tau increments z. We can se here (and in the definition of biot in physics.py)
           # that as tau increases according to the loop, tau will increase the z-coordinate by 1 which
           # corresponds to 1 mm or the diameter of a wire. Thus we are able to work through all of the
           # horizontal turns in the coil
           ## Warning ## tau - decreases z, axisOffset > 0
           array += biot(*params,-tau*met,axisOffset)


# This function calculates the contribution to the magnetic field from
# the second coil in the pair. The right coil
def axialCoilB(array):
    for epsilon in np.arange(vert):             # For each vertical row in the coil
       for tau in np.arange(horiz):             # For each horizontal column in the coil
           # params: The three parameters are z, the radius of the coil and the wire
           # offset epsilon. An array containing all the z-values of interest (axialZ) is
           # passed to the z parameter. R is the radius of the coil. The wire offset epsilon
           # is used here to increment through the vertical wires. As epsilon increases
           # according to the loop the radius will increase by an amount R = R + \epsilon.
           # See definition of the biot function in physics.py for clarification.
           params = (axialZ,R,epsilon*met)
           # Tau and axisOffset are passed as the final parameters to the biot function.
           # Tau serves the same purpose as epsilon (above) except in the horizontal direction.
           # That is, tau increments z. We can se here (and in the definition of biot in physics.py)
           # that as tau increases according to the loop, tau will increase the z-coordinate by 1 which
           # corresponds to 1 mm or the diameter of a wire. Thus we are able to work through all of the
           # horizontal turns in the coil. axisOffset is a simple constant used for positioning the wire
           # correctly. 

           ## Warning ## tau - increases z, axisOffset < 0
           array += biot(*params,tau*met,-axisOffset)

###############
# Radial #
###############

    # Define the domain on which we wish to calculate the radial value of the magnetic
    # field.
minimumR,maximumR,stepR = -2.5,2.5,200

    # Initialize two empty arrays (filled with zeros) which will hold
    # the magnetic field values along the radial-domain
r1, r2 = np.zeros(stepR),np.zeros(stepR)

    # Define an array of radial values corresponding to the domain
    # initiated above
radialR=np.linspace(minimumR,maximumR,stepR)

    # radialZ is the choice of z for which we wish to investigate how the field changes
    # radially. radialZ is a z slice of materal at the point z = radialZ.
radialZ = -2.5   # in mm


# The functions below function in exactly the same way as the functions above. The only
# difference being the addition of the second derivative to the equation.

# Contribution to field from coil A - integer (random) mode
def radialCoilA(array):
    for epsilon in np.arange(vert):             # For each vertical row in the coil
       for tau in np.arange(horiz):             # For each horizontal column in the coil
           params = (radialZ,R,epsilon*met)
           #radialR is the array of r values for which we wish to calculate the field.
           array += biot(*params,-tau*met,axisOffset) - biotSecond(*params,-tau*met,axisOffset) * (radialR)**2


# Contribution to field from coil B - integer (random) mode
def radialCoilB(array):
    for epsilon in np.arange(vert):             # Sum over the
       for tau in np.arange(horiz):             # whole coil array
           params = (radialZ,R,epsilon*met)
            #radialR is the array of r values for which we wish to calculate the field.
           array += biot(*params,tau*met,-axisOffset) - biotSecond(*params,tau*met,-axisOffset) * (radialR)**2
