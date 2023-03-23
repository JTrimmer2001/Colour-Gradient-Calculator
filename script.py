import CircleMapper as cm
import os
import matplotlib.pyplot as plt
import numpy as np

directory = os.fsencode('Images/AGNs/890018')
root = os.fsdecode(directory)

fitsfiles = []


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    if filename.endswith('.fits'):
        fitsfiles.append(root+'/'+filename)

radius = 5

ratio,blueavg,bluepercent,redavg,redpercent  = cm.continuousmapper(fitsfiles[1],fitsfiles[0],radius)

plt.rcParams['figure.figsize'] = [6,4]

fig, [ax1,ax2] = plt.subplots(1,2)
x = np.linspace(0,10,10)
ax1.plot(blueavg[:,0],blueavg[:,1],c='b',label='B flux')
ax1.plot(redavg[:,0],redavg[:,1],c='r',label='V flux')
ax1.set_xlabel('Radius (pixels)')
ax1.set_ylabel('Count')
ax1.legend()

ax2.plot(ratio[:,0],ratio[:,1],c='g',label='B/V flux ratio')
ax2.set_xlabel('Radius (pixels)')
ax2.set_ylabel('B/V ratio')
ax2.legend()

plt.tight_layout()
plt.show()