import matplotlib.pyplot as plt
import numpy as np
import random as ran

'''
In fig 1    I think you are plotting  Htot  versus omega   for a particular value  of Ho  100 G. Please confirm.

###
Can you also make plots of the average value and rms values of Htot  using the Gaussian distribtion of H0

Please start the y axis  from Htot=0.

Do the same  for sin^2 theta  in  figure 2.

One other thing.

Please repeat the calculation  assimng the distribution in  Ho is 10  times narrower.
    ie 0.1G instead of 1 G but still centered at 100G. It is looking better.
###
 plt.2

rms of  a random variable x_i   is  defined as 1/N times sum_i [x_i-<x>]^2  where  <x> =1/N times sum_i  x_i
    is the mean value of x_i and N is the total  number  of points  over which the rms is being evaluated .
It  should be small on the order of sigma  ~1G  or less.
'''

## Number of samples
bin_amount = 1000
sample_size = 500

## <H_0>
h_0 = 100 # Gauss

# Filenames
#fname5 = 'comparison-plots/aggregate.jpg'


## Plot the gaussian
plt.figure(1)
mu, sigma = h_0, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, sample_size)
count, bins, ignored = plt.hist(s, bin_amount, normed=True)
gaussian = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2))
plt.plot(bins, gaussian,linewidth=2, color='r')
plt.xlabel(r'$B$ [$Gauss$]')
plt.ylabel(r'$pdf(H_0)$')
plt.title(r'$H_0$ Histogram')
plt.show()

### Define a probability function for a given H_0

def probability(h_0):
    gaussian = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (h_0 - mu)**2 / (2 * sigma**2))
    return gaussian

### This portion of the code defines functions for sin^(theta) and cos^2(theta).

#h_0 = 100 # Gauss
h_1 = 1 # Gauss
gamma = 2*np.pi*0.630 # kHz/G

# Omega - be careful
omega_int = gamma #+ 3*sigma

# Sigma Multiplier
sigma_int = 3

# Range for omega values
wmin = 0
wmax = 800
step = sample_size

# Frequency Range
w = np.linspace(wmin,wmax,step)


def sin_squared_theta(h_0,omega):

    ## Omega changes for each gaussian h_0 !

    #omega = omega_int * 100 + sigma_int * sigma
    sin_theta_squared = h_1**2 / ( (h_0-omega/gamma)**2 + h_1**2 )
    return sin_theta_squared

### Define a function to calculate H_tot

def h_total(h_0,omega):

    #omega = omega_int * 100 + sigma_int * sigma
    h_tot = np.sqrt( h_1**2 + (h_0 - omega / gamma )**2 )
    return h_tot



### Define an array to hold averaged signal values

function_array_1 = np.zeros(sample_size)
function_array_2 = np.zeros(sample_size)

### Define a loop to fill the array

for i in s:
    function_array_1 += sin_squared_theta(i,w)
    function_array_2 += h_total(i,w)

'''
Calculating the Averages
'''
# Divide by the weighting fact]
function_array_1_avg = ( 1 / s.size ) * function_array_1
function_array_2_avg = ( 1 / s.size ) * function_array_2

'''
Calculating the RMSE
'''
# Divide by the weighting fact]
function_array_1_rms =  np.sqrt( ( 1 / s.size ) * (function_array_1_avg **2 - ( 1 / s.size ) * (function_array_1 **2 ) )**2 )
function_array_2_rms =  np.sqrt( ( 1 / s.size ) * (function_array_2_avg **2 - ( 1 / s.size ) * (function_array_2 **2 ) )**2 )


### Working out the plots

# plot with various axes scales
plt.figure(1,figsize=(8,8))

### Average 1
plt.subplot(221)
# # Original Function
plt.plot(w,sin_squared_theta(100,w),'r--',label="Original Function")
# Averaged Function
plt.plot(w,function_array_1_avg, label="Average Function") #(h_1/(h_0-w/gamma))**2)
plt.xlabel(r'$\omega \quad [rad/s]$')
plt.ylabel(r'Average of $\sin^2(\theta) \quad [none]$')
plt.title(r'')
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(1.2, 1), loc=1, borderaxespad=0.)
plt.grid(True)


### Average 2
plt.subplot(222)
# # Original Function
plt.plot(w,h_total(100,w),'r--')
# Averaged Function
plt.plot(w,function_array_2_avg)
plt.xlabel(r'$\omega \quad [rad/s]$')
plt.ylabel(r'Average of $H_{Tot}$ $[G]$')
plt.title(r'')
plt.grid(True)


### RMSE 1
plt.subplot(223)
# # Original Function
#plt.plot(w,sin_squared_theta(100,w),'r--',label="Original Function")
# RMS Function
plt.plot(w,function_array_1_rms,label="RMSE")
plt.xlabel(r'$\omega \quad [rad/s]$')
plt.ylabel(r'RMSE of $\sin^2(\theta) \quad [none]$')
plt.title(r'')
# Place a legend to the right of this smaller subplot.
#plt.legend(bbox_to_anchor=(1.2, 1), loc=1, borderaxespad=0.)
plt.grid(True)

### RMSE 2
plt.subplot(224)
# # Original Function
#plt.plot(w,h_total(100,w),'r--')
# RMS Function
plt.plot(w,function_array_2_rms)
plt.xlabel(r'$\omega \quad [rad/s]$')
plt.ylabel(r'RMSE of $H_{Tot}$ $[G]$')
#plt.title(r'')
plt.grid(True)

#plt.savefig(fname5)

# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92,
bottom=0.08, left=0.10, right=0.95, hspace=0.5,
                    wspace=0.5)

plt.show(block=True)
