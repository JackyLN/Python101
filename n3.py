#import library
import numpy as np
import matplotlib.pyplot as plt

#load data
f1 = "data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv"
d1 = np.genfromtxt(f1,delimiter=",", skip_header=1, 
               dtype=[('month', 'U7'),('town', 'U30'),('type', 'U30'),('block', 'i4'),('street', 'U50'),('storey', 'U30'),
                      ('area', 'i4'), ('flat', 'U30'), ('lease', 'i4'), ('remaining_lease', 'i4'), ('price', 'i8')])

f2 = "data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"
d2 = np.genfromtxt(f2,delimiter=",", skip_header=1, 
               dtype=[('month', 'U7'),('town', 'U30'),('type', 'U30'),('block', 'i4'),('street', 'U50'),('storey', 'U30'),
                      ('area', 'i4'), ('flat', 'U30'), ('lease', 'i4'), ('remaining_lease', 'U30'), ('price', 'i8')])


#filter data
roomFilter =  ['3 ROOM' ,'4 ROOM', '5 ROOM', 'EXECUTIVE']
filterTown = np.array(['ANG MO KIO','BUKIT MERAH','QUEENSTOWN', 'KALLANG/WHAMPOA', 'JURONG EAST', 'BEDOK'])

plotdata = []
for town in filterTown:
    tmpTown1 = d1[d1['town'] == town]
    tmpTown2 = d2[d2['town'] == town]
    
    tempCount = []
    for room in roomFilter: 
        tmpRoom1 = tmpTown1[tmpTown1['type'] == room]
        tmpRoom2 = tmpTown2[tmpTown2['type'] == room]
        count = len(tmpRoom1) + len(tmpRoom2)
        tempCount.append(count)

    plotdata.append([town, tempCount])

#Plot part

fig = plt.figure(figsize=(12,6))

ax1 = fig.add_subplot(2,3,1) 
ax1.pie(plotdata[0][1]) #AMK

ax2 = fig.add_subplot(2,3,2)
ax2.pie(plotdata[1][1]) #BUKIT MERAH

ax3 = fig.add_subplot(2,3,3)
ax3.pie(plotdata[2][1]) #QUEENSTOWN

ax4 = fig.add_subplot(2,3,4)
ax4.pie(plotdata[3][1]) #KALLANG/WHAMPOA

ax5 = fig.add_subplot(2,3,5)
ax5.pie(plotdata[4][1]) #BUKIT MERAH

ax6 = fig.add_subplot(2,3,6)
ax6.pie(plotdata[5][1]) #BUKIT MERAH

plt.show()
