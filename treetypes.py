# -*- coding: utf-8 -*-

import pandas
import numpy
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

data = pandas.read_csv('data/sites.csv', low_memory=False)
data = data.replace(r'^\s*$', numpy.NaN, regex=True)

# print out information from the survey
print('Species Counts:')
speciescounts = data['Species'].value_counts(sort=True)
print(speciescounts)

# graph tree species
#TODO make the x-axis labels legible 
seaborn.histplot(x="Species", data=data)
plt.xlabel('Tree Species')
plt.ylabel('Number of Individuals')
plt.title('Maplewood Tree Survey Species Breakdown')
plt.savefig('images/species.png')