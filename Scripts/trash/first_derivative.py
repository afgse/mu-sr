#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last Updated Mon May 29, 2017

@author: jasonfakidis

"""

import numpy as np
import matplotlib.pyplot as plt


'''
A list of variables defining the names used on the axes of the graph produced
by matplotlib.
'''

x_name = 'z'
x_units = 'mm'
y_name = 'B'
y_units = 'Gauss/mm' # first deriv


#############################################################################
'''Defining the Constants'''
#############################################################################

mu = 4*np.pi
I = 1
constant = mu*I/2


step = 200
minim = -60
maxim = 60

vert = 5
horiz = 5

tau = 27 #offset constants for coil 2

met = 1

#############################################################################
'''Initializing the function arrays'''
#############################################################################

'''
Here we create two empy numpy arrays meant to hold each of the 'step' functions points
in our graph.

Note that they are set to a size of 'step'.
'''
y1 = np.zeros(step)
y2 = np.zeros(step)

zmin=minim
zmax=maxim
npoints=step

z=np.linspace(zmin,zmax,npoints)

#############################################################################
'''Calculating the Fields for Z'''
#############################################################################

###############
#COIL NUMBER 1#
###############

for R in np.arange(vert):
   for i in np.arange(horiz):

       ### Implementation of the Biot-Savart Law###
       def biotFirst(z,R,sep):
           indep = (z+tau/2)-sep
           return constant * -3 * R**2 * indep / (indep**2 + R**2)**2.5

       y1 += biotFirst(z,tau/2+R*met,i*met)



###############
#COIL NUMBER 2#
###############
for R in np.arange(vert):
   for i in np.arange(horiz):

       ### Implementation of the Biot-Savart Law ###
       '''NOTE: To account for the spacing between the first and
       second coil an offset (tau) is added. The effect is a shift of the graph to
       the right by tau units.'''
       ### Implementation of the Biot-Savart Law###
       def biotFirst(z,R,sep):
           indep = (z-tau/2)+sep
           return constant * -3 * R**2 * indep / (indep**2 + R**2)**2.5

       y2 += biotFirst(z,tau/2+R*met,i*met)


#############################################################################
'''Summing the two coils'''
#############################################################################

''' This simply sums the effect of the two coils into a single array for output '''
y = y1 + y2


#############################################################################
'''Plotting the Graphs of z'''
#############################################################################

plt.figure(1)
plt.plot(z,y,marker="",linestyle="-",linewidth=2,color="b",
         label=" function")
# add axis labels and title
plt.xlabel('{} [{}]'.format(x_name,x_units))
plt.ylabel('{} [{}]'.format(y_name,y_units))
plt.title(r'Quasi-Helmholtz [5x5] winding')
# print out  a statement that the plot is being displayed
print ('Displaying plot 1')
# plt.show() may or may not need to be commented out depending on your python
# editor (spyder) settings.
plt.show()


#Reset the global variables
y1 = np.zeros(step)
y2 = np.zeros(step)
