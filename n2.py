#import library
import numpy as np
import matplotlib.pyplot as plt

#import data
f = "data/median-resale-prices-for-registered-applications-by-town-and-flat-type.csv"
d = np.genfromtxt(f, delimiter=',', skip_header=True,
                  dtype=[('qtr', 'U7'),('town', 'U30'),('type','U20'),('price','i4')])
                  
d = d[d['price'] != -1] # remove missing price
d['town'] = np.char.upper(d['town'])
d['type'] = np.char.upper(d['type'])

roomFilter =  ['4-ROOM', '5-ROOM']
filterTown = np.array(['ANG MO KIO','BUKIT MERAH','QUEENSTOWN', 'KALLANG/WHAMPOA', 'JURONG EAST', 'BEDOK'])
filterYear = np.arange(2010,2021)

#remove data before 2010
newData = np.empty( (0,), dtype=[('qtr', 'U7'),('town', 'U30'),('type','U20'),('price','i4')] )
for year in filterYear:

    t =d[np.char.find(d['qtr'], str(year)) > -1]
    newData = np.append(newData, t, axis=0)

plotdata = []
for town in filterTown:
    tmpTown = newData[newData['town'] == town]
    
    for room in roomFilter: 
        tmpRoom = tmpTown[tmpTown['type'] == room]

        plotdata.append(tmpRoom['price'])


#Plot part

fig = plt.figure(figsize =(10, 7)) 
  
# Creating plot 
plt.boxplot(plotdata) 
  
# show plot 
plt.show() 
