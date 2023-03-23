import pandas as pd
import CircleMapper as cm
import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np

def autograd():

    catalogue = pd.read_csv('Galaxy cutout checklist.csv')
    directory = os.fsencode('Images/Non-AGNs/')
    root = os.fsdecode(directory)
    framecreated = False
    usedids = []
    foldersum = 0

    for folder in os.listdir(directory):
        foldersum+=1
        id = os.fsdecode(folder)
        fitsfiles = []
        for file in os.listdir(directory+folder):
            filename = os.fsdecode(file)
            
            if filename.endswith('.fits'):
                fitsfiles.append(root+id+'/'+filename) #This whole thing sifts through a file structure (agns at the moment)

        if not fitsfiles: #if no fits files are found, skip this folder
            continue
        
        info = catalogue[catalogue['ID']==id] #turns catalogue into single row for this source
        #print(info)

        try:
            if id == '1011872': #the one odd file with a radius thats just wrong lol
                radius = 6
            else:
                radius = math.ceil(info['Angular size'] + 0.5) #I think this is a decent estimation for the radius of the source based on trial and error
                radius = int(radius) # makes sure its an integer
        except:
            continue

        usedids.append(id) # adds to a list of used sources, theyre stored in chunks in the data frame so I need a way to seperate the sources easily for plotting
        ratio,blueavg,bluepercent,redavg,redpercent = cm.continuousmapper(fitsfiles[1],fitsfiles[0],radius)#runs the mapping function

        d={'id':id,
        'ratio':ratio[:,1],
        'b_avg':blueavg[:,1],
        'b_per':bluepercent[:,1],
        'r_avg':redavg[:,1],
        'r_per':redpercent[:,1],
        'radius':radius} #dict to turn data into a data frame

        if framecreated == False:#creates data frame from dict if df has not been initialised yet
            table = pd.DataFrame(data=d)
            framecreated = True
        else:
            addition = pd.DataFrame(data=d)
            table = pd.concat([table,addition],ignore_index=True,sort=False)#concats onto the end, note d cannot be a dict for this (make interim df)

    table.to_csv('Non_AGN_colour_grads.csv')

def plotter():
    table = pd.read_csv('Non_AGN_colour_grads.csv')
    ids = table['id'].unique()

    vids = ['753883','595481','479295']

    plt.rcParams['figure.figsize']=[6,12]

    fig, [ax1,ax2,ax3] = plt.subplots(3,1,sharex='all')
    shade = 1

    for id in ids:
        shade +=1
        source = table[table['id']==id].copy()

        special = False
        for i in vids:
            if str(id) == i:
                special = True
                break
            
        
        if special == True:
            #Full colour line
            x = np.linspace(0,int(source.iloc[0,7]),int(source.iloc[0,7]))
            ax1.plot(x,'b_avg',data=source,c='b',label='B flux',zorder=1)
            ax1.plot(x,'r_avg',data=source,c='r',label='V flux',zorder=1)

            ax2.plot(x,'b_per',data=source,c='b',label='B flux %',zorder=1)
            ax2.plot(x,'r_per',data=source,c='r',label='V flux %',zorder=1)

            ax3.plot(x,'ratio',data=source,c='m',label='ratio flux B/V',zorder=1)

        else:
            #Grey scale line
            what = source.iloc[0,5]
            x = np.linspace(0,int(source.iloc[0,7]),int(source.iloc[0,7]))
            ax1.plot(x,'b_avg',data=source,color=(0.3,0.3,0.3),alpha=0.01*shade,zorder=0)
            ax1.plot(x,'r_avg',data=source,color=(0.8,0.8,0.8),alpha=0.01*shade,zorder=0)

            ax2.plot(x,'b_per',data=source,color=(0.3,0.3,0.3),alpha=0.01*shade,zorder=0)
            ax2.plot(x,'r_per',data=source,color=(0.8,0.8,0.8),alpha=0.01*shade,zorder=0)

            ax3.plot(x,'ratio',data=source,color=(0.2,0.2,0.2),alpha=0.01*shade,zorder=0)

    ax3.set_xlabel('radius (pixels)')
    ax1.set_ylabel('Total count')
    ax2.set_ylabel('% of Total count')
    ax3.set_ylabel('B/V ratio')

    V_flux = mp.Patch(color='r',label='V flux')
    B_flux = mp.Patch(color='b',label='B flux')
    ratio_patch = mp.Patch(color='m',label='B/V flux ratio')

    ax1.legend(handles=[B_flux,V_flux],loc='upper right')
    ax2.legend(handles=[B_flux,V_flux],loc='upper right')
    ax3.legend(handles=[ratio_patch],loc='upper right')

    plt.subplots_adjust(wspace=0,hspace=0)
    plt.savefig('Non_AGN_grad.png')
    plt.show()

plotter()
#y=