import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


d = pd.read_csv("data/average-annual-electricity-consumption-by-planning-area-and-dwelling-type.csv")
d['average_monthly_electricity_consumption_kwh'] = pd.to_numeric(d['average_monthly_electricity_consumption_kwh'], errors = 'coerce')

#filtter for Overall and year
d = d[(d['dwelling_type']=='Overall')]
d = d[(d['year'] >= 2010) & (d['year'] <= 2019)]

#filter for towns
towns = ["Jurong East", "Bedok", "Yishun", "Bukit Merah"]
plotData = d[d["planning_area"].isin(towns)]

#plot
sns.lineplot(data=plotData, x="year", y="average_monthly_electricity_consumption_kwh", hue="planning_area")
