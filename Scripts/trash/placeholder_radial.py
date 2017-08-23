



# Random number generation for r, and z
xmin, xmax = -5,5
rmin, rmax = -2,2

ran_x = (xmax-xmin)*np.random.random_sample()+xmin
ran_r = (rmax-rmin)*np.random.random_sample()+rmin




# Array of r values to define graph
rmin=-2.5
rmax=2.5
npoints=200
r=np.linspace(rmin,rmax,npoints)



# Initializing integer for random
a1 = 0
a2 = 0

# Contribution to field from coil A - integer (random) mode
def coil_1(a,z,r):
    for epsilon in np.arange(vert):             # Sum over the
       for tau in np.arange(horiz):             # whole coil array
           params = (z,R,epsilon*met)
           a = biot(*params,-tau*met,axisOffse) - biotSecond(*params,-tau*met,axisOffset) * r**2
           return a

# Contribution to field from coil B - integer (random) mode
def coil_2(a,z,r):
    for epsilon in np.arange(vert):             # Sum over the
       for tau in np.arange(horiz):             # whole coil array
           params = (z,R,epsilon*met)
           a = biot(*params,tau*met,-axisOffset) - biotSecond(*params,tau*met,-axisOffset) * r**2
           return a

# Saving contributions from each coil in a new array - total contribution
a = coil_1(a1,ran_x,ran_r) + coil_2(a2,ran_x,ran_r)
