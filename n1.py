d = d[(d['type'] == '4 ROOM')]
d = d[(d['remaining_lease'] >= '69 years')]
d = d[(d['remaining_lease'] <= '89 years 11 months')]
d = d[(d['price'] >= 400000)]
d = d[(d['price'] <= 650000)]

filterTown = np.array(['ANG MO KIO','BUKIT MERAH','QUEENSTOWN', 'KALLANG/WHAMPOA', 'JURONG EAST', 'BEDOK'])
filterYear = np.arange(2017, 2021)

#data = np.array([])
data = []

for town in filterTown:

    townTmp = d[np.char.find(d['town'], str(town))> -1]

    for year in filterYear:
        yearTmp = townTmp[np.char.find(townTmp['month'], str(year)) > -1]
        avgPrice = yearTmp['price'].mean()
        data.append([town,year,avgPrice])
        
print("There are altogether {} rows of data in this dataset.".format(len(d)))
for x in data: 
    print("The median resale flat price for {} in {} is ${:.0f}".format(x[0], x[1], x[2]))
