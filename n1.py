f = "data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv"
d = np.genfromtxt(f,delimiter=",", skip_header=1, 
               dtype=[('month', 'U7'),('town', 'U30'),('type', 'U30'),('block', 'i4'),('street', 'U50'),('storey', 'U30'),
                      ('area', 'i4'), ('flat', 'U30'), ('lease', 'i4'), ('remaining_lease', 'U30'), ('price', 'i8')])

d = d[(d['type'] == '4 ROOM')]
d = d[(d['remaining_lease'] >= '69 years')]
d = d[(d['remaining_lease'] <= '89 years 11 months')]
d = d[(d['price'] >= int('400000'))]
d = d[(d['price'] <= int('650000'))]

filterTown = np.array(['ANG MO KIO','BEDOK','SENGKANG', 'BUKIT BATOK'])
d  = d[(np.isin(d['town'],filterTown))]

print("There are altogether {} rows of data in this dataset.".format(len(d)))
