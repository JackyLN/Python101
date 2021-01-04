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

b = plt.boxplot(plotdata, labels=['4-BR', '5-BR','4-BR', '5-BR', '4-BR', '5-BR', '4-BR', '5-BR', '4-BR', '5-BR', '4-BR', '5-BR'], patch_artist=True,)
colours = ['#ffb3ba', '#ffb3ba', '#ffdfba', '#ffdfba', '#ffffba', '#ffffba','#baffc9', '#baffc9', '#bae1ff', '#bae1ff', '#ecd5e3', '#ecd5e3']

for i in range(len(b['boxes'])):  #0 to 11
   b['boxes'][i].set_facecolor(colours[i])
    
for i in range(len(b['medians'])):  #0 to 11
   x,y = b['medians'][i].get_xydata()[1]
   plt.text(x,y,'{:.0f}'.format(y), fontsize=8)


# show plot 

h1, = plt.plot([],'#ffb3ba')
h2, = plt.plot([],'#ffdfba')
h3, = plt.plot([],'#ffffba')
h4, = plt.plot([],'#baffc9')
h5, = plt.plot([],'#bae1ff')
h6, = plt.plot([],'#ecd5e3')
plt.legend((h1, h2, h3, h4, h5, h6),filterTown)

plt.title('Median Resale Prices', fontweight='bold')
plt.xlabel("Flat Type", fontsize=11)
plt.ylabel("SGD$", fontsize=11)
plt.suptitle('Figure 3', fontsize=14, fontweight='bold')
plt.show()
