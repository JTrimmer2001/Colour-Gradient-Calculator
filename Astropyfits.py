import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from astropy.io import fits


def image_viewer():
    hdulist = fits.open("C:/Users/Jet26/Documents/PHYS 369 Code and data/Data/Subaru B matched/subaru_B_matched-psf_070_sci_20.fits")

    hdulist.info()
    image_data = hdulist[0].data

    print(type(image_data))
    print(image_data.shape)

    hdulist.close()

    plt.imshow(image_data, cmap = "gray", norm = colors.LogNorm())
    plt.colorbar()

    plt.show()


def table_viewer():
    hdulist = fits.open("C:/Users/Jet26/Documents/PHYS 369 Code and data/Data/cosmos2015_NOphotometry_masses_sfrs.fits")

    #hdulist.info()

    hdr = hdulist[1].header
    data = hdulist[1].data

    print(type(data))

    Field = data.field(0)

    print(Field)
    print(type(Field))

    ttype = "TTYPE"

    i = 9

    while i < 4*hdr[7]:

        try:
            print(hdulist[1].header[ttype + str(i)])
            i += 1

        except:
            break

             




    hdulist.close()






    


table_viewer()

