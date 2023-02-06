import pandas as pd
import numpy as np
from astropy.io import fits


def fitsToCsv(): #Function to convert a fits file to csv format for use in excel or qti or whatever

    File = fits.open("file name") #Opens fits file, convert to user/specified input at a later date

    hdr = File[1].header #astropy.io.fits.header.Header
    dta = File[1].data   #astropy.io.fits.fitsrec.FITS_rec

    #Neither of these are currently in useable format, using .field can take a column from the fits data table and return a 1D numpy array
    #As seen in Astropyfits.py we can find values for each header by looping through the header list
    #By appending to a panda dataframe we should be able to construct a data frame environment with all entries and 


