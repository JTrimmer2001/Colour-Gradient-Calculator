# Colour-Gradient-Calculator
Code to analyse the colour over the extent of a source

===========================================================================

Very primitive method: 
      -Takes in two images in different wavelengths and a user defined radius in pixels (can be taken from a catalogue)
      -Draws a pair of circles over the images given, one near the center and one near the exterior
      -averages values of the pixels covered by these circles
      -Finds the difference between the two averages to approximate a gradient
      
Limitations:
      -Only compares two circles, not able to track fine changes in colour within the galaxy
      -Only draws circles, for a very flat source this may be an issue
      -Slow to work, requires manual switching of files and user input for the radius of the galaxy
      
Future improvements:
      -Change to method, potentially a continuous analysis of the colour and production of a corresponding graph
      -Implementation of the IPAC/NASA API to allow a set of coordinates to be input and the image files to be gathered and processed without user input
      
===========================================================================

The files to be looked at must be manually changed within the code at the moment, locations for the files to be used are indicated with comments

STILL NEEDS TESTING!! Produces "Sensible" results but the actual value isnt directly related to actual colour since it is based on values between 0 and 1 as per the pixel values.

User input of the radius of the source is required once the program is running

===========================================================================
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
===========================================================================
