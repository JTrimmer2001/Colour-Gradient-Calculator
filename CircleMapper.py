from CircleGenerator import circlegenerator
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math as mt

'''
This code should find the points on a fits image that line up with the coords defined in CircleGenerator.py
'''


def mapper():

    '''
    Function: 
        mapper

    Purpose: 
        maps a set of coordinates onto an array, taking average value of pixels selected
        Finds difference between two circles to produce a "Gradient"
        Currently uses the circlegenerator function but this could be changed in future to allow more diverse mapping

    Inputs: 
        Image in FITS format (Not able to be specified outside of the code for the time being)
        radius (Currently set by user input)

    Outputs: 
        ColourGradient (float): takes difference of the inner and outer circles to produce a gradient
                                - more negative value indicates a gradient towards blue at the outer edge
                                - more positive value indicates a gradient towards red at the outer edge
                                - greater the absolute value, the bigger the difference in colour
    '''
    
    with fits.open("/Users/Jet26/Documents/Data/subaru/put coords here lol/0001_150.09285000_2.73443000_COSMOS.V.original_psf.v2.fits") as cutout: #Opens file in the with structure, file is auto closed once segment is exited
        data1 = cutout[0].data #data is loaded into a variable

    with fits.open("/Users/Jet26/Documents/Data/subaru/put coords here lol/0001_150.09285000_2.73443000_COSMOS.B.original_psf.v2.fits") as cutout: #To use this program these file location strings will need to be changed
        data2 = cutout[0].data

    '''PLEASE NOTE, DATA1 SHOULD CORRESPOND TO REDDER DATA SUCH AS F140W, F160W ETC. DATA2 SHOULD CORRESPOND TO BLUER DATA'''

    SideLength = mt.sqrt(data1.size) #This assumes that data1 and 2 have the same shape and size, shouldnt be an issue using the cosmos cutout generator

    x = SideLength/2 #halves sidelength to find center (again, assumes same size and assumes square image)

    r = int(input("Enter radius of galaxy to be observed") )
    '''
    Current method of determining radius, official value "Should" be obtainable via the hubble gz meta data file once I find it
    !!Bear in mind the resolution of the picture being used!!
    Radius is input as a number of pixels, so if source is 0.12" wide, and the resolution is 0.03" (Like ACS I think) then the radius is 2 pixels
    '''
    InnerCoords = circlegenerator(x,x,(r/5)) #Default inner circle is taken at 0.2Rsource from the center of the source
    OuterCoords = circlegenerator(x,x,4*(r/5)) #Default outer circle is taken at 0.8Rsource from the center,
                                               #made this choice so that the outer circle does actually cover a fair bit of the galaxy

    Total1 = 0
    Total2 = 0
    Num = 0
    i = int(0)

    #print(InnerCoords[0,0])
    #print(InnerCoords[1,1])
    #print(data1.data[InnerCoords[0,i]:InnerCoords[1,i]])

    size = np.size(InnerCoords)/2

    while i <= size-1:
        Pixel1 = data1[InnerCoords[i,0],InnerCoords[i,1]] #'Should' sum the values of pixels selected by circle generator
        Total1 += Pixel1
        Pixel2 = data2[InnerCoords[i,0],InnerCoords[i,1]] #Does the same for the other image, should be an image taken in a different wavelength
        Total2 += Pixel2
        i+=1
        Num += 1 #Keeps count of pixels used for calculating the average

    ColIn = (Total2/Num) - (Total1/Num) #Finds the colour on a circle closer to the middle of the agn (at r = 0.2Rsource)

    Total1 = 0
    Total2 = 0 #Resets totals so theres no mixing between the two circles
    Num = 0
    i=0

    while i <= size-1:
        Pixel1 = data1[OuterCoords[i,0],OuterCoords[i,1]] #'Should' sum the values of pixels selected by circle generator
        Total1 += Pixel1
        Pixel2 = data2[OuterCoords[i,0],OuterCoords[i,1]] #Does the same for the other image, should be an image taken in a different wavelength
        Total2 += Pixel2
        i+=1
        Num += 1 #Keeps count of pixels used for calculating the average

    ColOut = (Total2/Num) - (Total1/Num)

    ColourGradient = ColIn - ColOut 

    print("Colour gradient of source is ", ColourGradient) #Calculates a difference between inner and outer colour, more negative gradient means redder outer edge
    print("Inner colour: ", ColIn, ", Outer colour: ", ColOut)

    '''
    NB FOR THE FUTURE:

    More reliable results can be gained by taking average colour at more radii, 
    potential for a loop to be used to run through all possible interger radii within bounds of the source

    Data my be difficult to quantify, but could be used for one or two galaxies to examine interesting galaxies such as 
    those with a large extent and a blue strip somewhere along the glactic disk, or for use on galaxies where there is a
    gradient towards blue toward the outer area of the galaxy
    
    '''

    #Also, IPAC/NASA have an API that can be used to request images via the program, requires "Learning" XML lol



def continuousmapper(red,blue,r):
    '''
    Params: 
            red (red file string)
            blue (blue file string)
            r (radius in pixels (int))
            
    Returns:
            colour (currently incorrect, b-v)
            blueavg (blue flux)
            bluepercent (percentage of total thats blue)
            redavg (red flux)
            redpercent (percentage of total thats red)
    '''


    radius = r #Radius in pixels
    with fits.open(red) as cutout: #Opens file in the with structure, file is auto closed once segment is exited
        data1 = cutout[0].data #data is loaded into a variable

    with fits.open(blue) as cutout: #To use this program these file location strings will need to be changed
        data2 = cutout[0].data

    '''PLEASE NOTE, DATA1 SHOULD CORRESPOND TO REDDER DATA SUCH AS F140W, F160W ETC. DATA2 SHOULD CORRESPOND TO BLUER DATA'''

    SideLength = mt.sqrt(data1.size) #This assumes that data1 and 2 have the same shape and size, shouldnt be an issue using the cosmos cutout generator

    x = SideLength/2 #halves sidelength to find center (again, assumes same size and assumes square image)

    colour = []
    blueavg = []
    redavg = []
    coords = []

    for i in range(radius):

        Total1 = 0
        Total2 = 0
        
        coords = circlegenerator(x,x,i)
        size = int(np.size(coords)/2)

        num = 0

        while num <= size-1:
                Pixel1 = data1[coords[i,0],coords[i,1]] #'Should' sum the values of pixels selected by circle generator
                Total1 += Pixel1
                Pixel2 = data2[coords[i,0],coords[i,1]] #Does the same for the other image, should be an image taken in a different wavelength
                Total2 += Pixel2
                num += 1
        
        colour.append((i,((Total2/num) - (Total1/num)) ))
        blueavg.append((i, (Total2/num)))
        redavg.append((i,(Total1/num)))

    colour = np.array(colour)
    blueavg = np.array(blueavg)
    redavg = np.array(redavg)

    '''x = colour[:,0]
    y = colour[:,1]
    plt.plot(x,y)

    bx = blueavg[:,0]
    by = blueavg[:,1]

    plt.plot(bx,by,'b-')

    rx = redavg[:,0]
    ry = redavg[:,1]

    plt.plot(rx,ry,'r-')#This segment will plot three lines - flux/data/whatever for "blue" "red" and "total" emission

    plt.show()'''

    i = 0

    total = []
    bluepercent = []
    redpercent = []

    for i in range(radius):

        b = blueavg[i,1]
        R = redavg[i,1]
        t = b + R
        total.append((i,t))

        averageb = float(100 * b/t)

        bluepercent.append((i, averageb))

        averager = float(100 * R/t)
        redpercent.append((i, averager))

    bluepercent = np.array(bluepercent)
    redpercent = np.array(redpercent)

    '''plt.plot(bluepercent[:,0],bluepercent[:,1], 'b-')
    plt.plot(redpercent[:,0],redpercent[:,1],'r-')

    plt.show()'''

    return colour,blueavg,bluepercent,redavg,redpercent


    
