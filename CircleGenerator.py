import math
import numpy as np
import matplotlib.pyplot as plt

a = 20 #
b = 30 # a and b define the center of the circle, could couple to brightest pixel to isolate agn
r = 30 #radius - find ways to define radius needed

#The lower this value the higher quality the circle is with more points generated, 0.01 seems to be a good solid value
stepSize = 0.01

#Generated vertices
positions = []

t = 0
while t < 2 * math.pi:
    positions.append((np.around(r * math.cos(t) + a),np.around(r * math.sin(t) + b))) #np.around rounds to nearest whole number 
    t += stepSize

array = np.array(positions) #converts to array

plt.scatter(array[:,0], array[:,1]) #plots the resulting coords - unneccessary for final code

plt.show()

#ADD documentation at the top, would be useful to adapt this file into a callable process so circles can be generated on the fly
