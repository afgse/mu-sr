import numpy as np
import matplotlib.pyplot as plt
from main import *

'''
Errors:
(1) - Units
(2) - Last plot does not compile (peaks?)
'''


#############################################################################
'''Savefigures'''
#############################################################################

#############################################################################
'''Histogram'''
#############################################################################

######
# H1 #
######

plt.figure()
count, bins, ignored = plt.hist(h, 20, normed=True)
plt.xlabel(r'x label')
plt.ylabel(r'y label')
plt.title(r'title')
# plt.savefig(fname1)
plt.show(block=True)

########
# Htot #
########

plt.figure()
count, bins, ignored = plt.hist(h_tot(s), bin_amount, normed=True)
plt.xlabel(r'$B$ [$Gauss$]')
plt.ylabel(r'# $H_{tot}$')
plt.title(r'$H_{tot}$ Histogram')
#plt.savefig(fname2)
plt.show(block=True)

######
# H0 #
######

plt.figure()
count, bins, ignored = plt.hist(s, bin_amount, normed=True)
gaussian = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2))
plt.xlabel(r'$B$ [$Gauss$]')
plt.ylabel(r'# plt$H_0$')
plt.title(r'$H_0$ Histogram')
#plt.savefig(fname1)
plt.show(block=True)

#############################################################################
'''Radial''' # - Radial
#############################################################################

# Plot labels
x_name1 = 'r'
x_units1 = 'mm'
y_name1 = 'B'
y_units1 = 'Gauss'


plt.figure()
plt.plot(radialR,r,marker="",linestyle="-",linewidth=2,color="b",label=" function")
plt.xlabel('{} [{}]'.format(x_name1,x_units1))
plt.ylabel('{} [{}]'.format(y_name1,y_units1))
plt.title('Radial Magnetic Field Distribution for a 5x5 \n turn 2D coil at z = {}'.format(radialZ))
plt.show()

#############################################################################
'''Plotting''' # - Axial
#############################################################################


# Plot labels
x_name = 'z'
x_units = 'mm'
y_name = 'B'
y_units = 'Gauss'

plt.figure()
plt.plot(axialZ,a,marker="",linestyle="-",linewidth=2,color="b",label=" function")
plt.xlabel('{} [{}]'.format(x_name,x_units))
plt.ylabel('{} [{}]'.format(y_name,y_units))
plt.title(r'Quasi-Helmholtz [5x5] winding')
plt.show()


#############################################################################
'''Plotting''' # - Signal & Amplitudes
#############################################################################

fig = plt.figure()
plt.plot(t,signal_array)
plt.xlabel(r'$t$ $[s]$')
plt.ylabel(r'$\overline{S_z}(H_0))$ $[]$')
#np.plt.title(r'Average Polarization Signal - $\omega$ = {}'.format(omega_int))
fig.tight_layout()
#plt.savefig(fname3)
plt.show(block=True)

fig = plt.figure()
plt.plot(t_peak,signal_peak,'.')
plt.xlabel(r'$t$ $[s]$')
plt.ylabel(r'Amplitude $\overline{S_z}(H_0))$ $[]$')
#np.plt.title(r'Average Polarization Signal - $\omega$ = {}'.format(omega_int))
fig.tight_layout()
#plt.savefig(fname4)
plt.show(block=True)


#############################################################################
'''Plotting''' # - Amplitudes
#############################################################################

np.set_printoptions(threshold=np.inf)

gammaAmp = 2*np.pi*0.630 # kHz/G
thetaAmp = np.arcsin(h_1**2/((-h_0+w/gammaAmp)**2+h_1**2))
h_totAmp = np.sqrt(h_1**2 + (h_0 - w/gammaAmp)**2)

plt.figure()
plt.plot(w,np.sin(thetaAmp)**2)     #(h_1/(h_0-w/gamma))**2) , np.sin(theta)^2
plt.xlabel(r'$\omega \quad [rad/s]$')
plt.ylabel(r'$\sin^2(\theta) \quad [none]$')
plt.title(r'Amplitude of $P_z$')
#lt.savefig(fname2)
plt.show(block=True)

plt.figure()
plt.plot(w,h_totAmp) # h_tot
plt.xlabel(r'$\omega \quad [rad/s]$')
plt.ylabel(r'$ \sqrt{h_1^2 + (h_0 - \frac{\omega}{\gamma})^2} \quad [G]$')
plt.title(r'Magnitude of $h_{tot}$')
#plt.savefig(fname1)
plt.show(block=True)
