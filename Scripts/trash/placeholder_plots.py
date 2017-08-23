#############################################################################
'''Plotting''' # - Radial
#############################################################################

# Plot labels
x_name1 = 'r'
x_units1 = 'mm'
y_name1 = 'B'
y_units1 = 'Gauss'


# plt.figure(1)
# plt.plot(r,a,marker="",linestyle="-",linewidth=2,color="b",label=" function")
# plt.xlabel('{} [{}]'.format(x_name1,x_units1))
# plt.ylabel('{} [{}]'.format(y_name1,y_units1))
# plt.title('Radial Magnetic Field Distribution for a 5x5 \n turn 2D coil at z = {}'.format(zChoice))
# print ('Displaying plot 1')
# plt.show()
#
# #Reset the global variables
# a1 = np.zeros(step1)
# a2 = np.zeros(step1)

#############################################################################
'''Plotting''' # - Axial
#############################################################################


# Plot labels
x_name = 'z'
x_units = 'mm'
y_name = 'B'
y_units = 'Gauss'

plt.figure(1)
plt.plot(z,y,marker="",linestyle="-",linewidth=2,color="b",label=" function")
plt.xlabel('{} [{}]'.format(x_name,x_units))
plt.ylabel('{} [{}]'.format(y_name,y_units))
plt.title(r'Quasi-Helmholtz [5x5] winding')
print ('Displaying plot 1')
plt.show()
