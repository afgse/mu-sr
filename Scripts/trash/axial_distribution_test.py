#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last Updated Mon May 29, 2017

@author: jasonfakidis
"""

import numpy as np
import matplotlib.pyplot as plt

#############################################################################
'''Defining the Constants'''
#############################################################################

x_name = 'z'
x_units = 'mm'
r_name = 'r'
r_units = 'mm'
y_name = 'B'
y_units = 'Gauss'

mu = 4*np.pi
I = 1
constant = mu*I/2

step = 200
minim = -60
maxim = 60





vert = 5
horiz = 5

tau = 27 #offset constants for coil 2

met = 1 # Unit conversion

#############################################################################
'''Initializing the function arrays'''
#############################################################################

y1 = np.zeros(step)
y2 = np.zeros(step)

a1 = np.zeros(step1)
a2 = np.zeros(step1)

zmin=minim
zmax=maxim
npoints=step
z=np.linspace(zmin,zmax,npoints)   # Array of z values

rmin=-2.5
rmax=2.5
npoints=200
r=np.linspace(rmin,rmax,npoints)




#############################################################################
'''Calculating the Fields for Z'''
#############################################################################

###############
#COIL NUMBER 1#
###############

for R in np.arange(vert):
   for i in np.arange(horiz):

       ### Implementation of the Biot-Savart Law###
       def biot(z,R,sep):
           indep = (z+tau/2)-sep
           return constant * (R**2/(R**2+indep**2)**1.5)

       y1 += biot (z,tau/2+R*met,i*met)












###############
#COIL NUMBER 2#
###############
for R in np.arange(vert):
   for i in np.arange(horiz):

       ### Implementation of the Biot-Savart Law ###
       '''NOTE: To account for the spacing between the first and
       second coil an offset (tau) is added. The effect is a shift of the graph to
       the right by tau units.'''
       def biot(z,R,sep):
          indep = (z-tau/2)+sep
          return constant * (R**2/(R**2+indep**2)**1.5)

       y2 += biot (z,tau/2+R*met,i*met)











#############################################################################
'''Summing the two coils'''
#############################################################################

''' This simply sums the effect of the two coils into a single array for output '''
y = y1 + y2

#############################################################################
'''Plotting the Graphs of z'''
#############################################################################

plt.figure(1)
plt.plot(z,y,marker="",linestyle="-",linewidth=2,color="b",label=" function")
plt.xlabel('{} [{}]'.format(x_name,x_units))
plt.ylabel('{} [{}]'.format(y_name,y_units))
plt.title(r'Quasi-Helmholtz [5x5] winding')
print ('Displaying plot 1')
plt.show()

#Reset the global variables
y1 = np.zeros(step)
y2 = np.zeros(step)
