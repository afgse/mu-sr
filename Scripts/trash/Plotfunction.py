import numpy as np
import matplotlib.pyplot as plt

#LIST OF ALL INPUTS

# Enter the name and units for x and y axes  on the plot.
# labeled. e.g. x_name = 'Time', x_units = 'ms', y_name = 'Voltage', y_units
# = 'V'.
x_name = 'Time'
x_units = 's'
y_name = 'Voltage'
y_units = 'V'

# definition of the f(x,parameterlist)  whoch is this example is an exponetial
#plus   a constant 
def function(x, amplitude,tau, V_offset):
#    """ exp function """
    return amplitude * np.exp(-x/tau) + V_offset

#define  a set a values  for the parameters  amplitude, tau and V_offset
params= (1.0,10.,0.01)  
      
#define the domain of f(x)  from  xmin to xmax  with npoints  
xmin=0
xmax=100
npoints=100    
# define x as an array  of points  from 0, 100
x= np.linspace(xmin,xmax,npoints)
#dedfine y   as  f(x)
y= function (x,*params)

# plots (x) 
# marker='.' : data points are not indicated by markers
# linestyle= '-' : a continuous line is drawn
# linewidth=2 : the line thickness is set to 2
# color='b' : the color of the line is set to black
# label=string : the string is shown in the legend
plt.plot(x,y,marker="",linestyle="-",linewidth=2,color="b",
         label=" function")
# add axis labels and title
plt.xlabel('{} [{}]'.format(x_name,x_units))
plt.ylabel('{} [{}]'.format(y_name,y_units))
plt.title(r'This is a title with latex $V(t)=A\exp[-t/\tau]+V_{offset}$')
# print out  a statement that the plot is being displayed
print ('Displaying plot 1')
# plt.show() may or may not need to be commented out depending on your python
# editor (spyder) settings.
plt.show()


###############################################################################
# plots residual and histogram of residual. Don't touch this par tof the code
###############################################################################

# residual is the difference between the data and theory
















