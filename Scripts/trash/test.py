# Generate a set of random numbers.
# Index these random numbers into your y array.
# Plot the histogram of this.
# See how they differ for each random (running the script each time.)

import numpy as np
import matplotlib.pyplot as plt
import axial_distribution as zd
import radial_distribution as rd

# Domain

xmin, xmax = -2,2
rmin, rmax = 5,5

# Random number generator
ran_x = (xmax-xmin)*np.random_sample()+xmin
ran_r = (rmax-rmin)*np.random_sample()+rmin

# Function
def fn(x,r):
    
