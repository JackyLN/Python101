#import library
import numpy as np
import matplotlib.pyplot as plt


#Load Data
f1 = "data/resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv"
d1 = np.genfromtxt(f1,delimiter=",", skip_header=1, 
               dtype=[('month', 'U7'),('town', 'U30'),('type', 'U30'),('block', 'i4'),('street', 'U50'),('storey', 'U30'),
                      ('area', 'i4'), ('flat', 'U30'), ('lease', 'i4'), ('remaining_lease', 'i4'), ('price', 'i8')])

f2 = "data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"
d2 = np.genfromtxt(f2,delimiter=",", skip_header=1, 
               dtype=[('month', 'U7'),('town', 'U30'),('type', 'U30'),('block', 'i4'),('street', 'U50'),('storey', 'U30'),
                      ('area', 'i4'), ('flat', 'U30'), ('lease', 'i4'), ('remaining_lease', 'U30'), ('price', 'i8')])


#data filtering
d1 = d1[(d1['type'] == '4 ROOM')]
d1 = d1[(d1['remaining_lease'] >= 69)]
d1 = d1[(d1['remaining_lease'] < 90)]
d1 = d1[(d1['price'] >= 400000)]
d1 = d1[(d1['price'] <= 650000)]

d2 = d2[(d2['type'] == '4 ROOM')]
d2 = d2[(d2['remaining_lease'] >= '69 years')]
d2 = d2[(d2['remaining_lease'] < '90 years')]
d2 = d2[(d2['price'] >= 400000)]
d2 = d2[(d2['price'] <= 650000)]


filterTown = np.array(['ANG MO KIO','BUKIT MERAH','QUEENSTOWN', 'KALLANG/WHAMPOA', 'JURONG EAST', 'BEDOK'])
a1 = d1[(np.isin(d1['town'],filterTown))]
a2 = d2[(np.isin(d2['town'],filterTown))]

mySum = a1.size + a2.size

filterYear1 = np.arange(2015, 2017)
filterYear2 = np.arange(2017, 2021)

#Get mean
data = []

for town in filterTown:

    townTmp1 = d1[np.char.find(d1['town'], str(town))> -1]
    townTmp2 = d2[np.char.find(d2['town'], str(town))> -1]

    for year in filterYear1:
        yearTmp = townTmp1[np.char.find(townTmp1['month'], str(year)) > -1]
        avgPrice = yearTmp['price'].mean()
        data.append([town,year,avgPrice])

    for year in filterYear2:
        yearTmp = townTmp2[np.char.find(townTmp2['month'], str(year)) > -1]
        avgPrice = yearTmp['price'].mean()
        data.append([town,year,avgPrice])

#print mean
print("There are altogether {} rows of data in this dataset.".format(mySum))
for x in data: 
    print("The median resale flat price for {} in {} is ${:.0f}".format(x[0], x[1], x[2]))
    
    
#print median
for town in filterTown:

#    tmp = data[np.char.find(data[0], str(town)) > -1]

    tmp = data[(data[0] == town)]
    avg  = tmp[2].mean()
            
    print("The median resale flat price inn {} for the last five year is {}".format(town, avg))
