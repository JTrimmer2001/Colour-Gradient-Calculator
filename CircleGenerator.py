import math
import numpy as np
import matplotlib.pyplot as plt


''' Circle Generator

    Inputs - a (int): x-coord of the center of the circle
             b (int): y-coord of the center of the circle
             r (int): radius of the circle
    
    Return - coords (np.array): 2D array of x- and y- coords in the circle. Coords are rounded to whole numbers using numpy.around
                                x-coords are in [:,0], y-coords are in [:,1]

'''

def circlegenerator(a,b,r):

    #The lower this value the higher quality the circle is with more points generated, 0.01 seems to be a good solid value
    stepSize = 0.01

    #Generated vertices
    positions = []

    t = 0
    while t < 2 * math.pi:
        positions.append((int(np.around(r * math.cos(t) + a)),int(np.around(r * math.sin(t) + b)))) #np.around rounds to nearest whole number 
        t += stepSize

    coords = np.array(positions) #converts to array

    return coords

    #plt.scatter(array[:,0], array[:,1]) #plots the resulting coords - unneccessary for final code

    #plt.show()

    #ADD documentation at the top, would be useful to adapt this file into a callable process so circles can be generated on the fly
