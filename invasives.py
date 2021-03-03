# -*- coding: utf-8 -*-

import pandas
import numpy
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
import scipy.stats
import seaborn
import matplotlib.pyplot as plt
import re

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

# load the 2020 Maplewood Tree Survey
ourtrees = pandas.read_csv('data/sites.csv', low_memory=False)
ourtrees = ourtrees.replace(r'^\s*$', numpy.NaN, regex=True)

# load the list of midwest invasive trees from eddmaps.org
invasives = pandas.read_csv('data/eddmaps.org_midwest_species.csv', low_memory=False)

# extract the scientific name from the tree survey into its own column
def SPECIESNAME(row):
    return re.findall(pattern='\(([^)]+)\)', string=row['Species'])[0]
ourtrees['Scientific'] = ourtrees.apply(lambda row: SPECIESNAME (row),axis=1)

# print out information from the survey
print('Scientific Names Counts:')
scientificcounts = ourtrees['Scientific'].value_counts(sort=True)
print(scientificcounts)

# print out the list of invasive trees
print('Invasive Trees:')
print(invasives['Scientific Name'])

# make a new column in ourtrees to indicate whether invasive
ourtrees['Invasive'] = ourtrees.Scientific.isin(invasives['Scientific Name']).astype(int)
print('Maplewood Invasives Count:')
mwinvasivescount = ourtrees['Invasive'].value_counts(sort=False)
print(mwinvasivescount)

# print list of invasive species present in maplewood
ourinvasivetrees = ourtrees[ourtrees['Invasive']>0].groupby('Species')['Site ID'].count()
ourinvasivetrees = ourinvasivetrees.sort_values(ascending=False)
print('Invasive Trees Present in Maplewood')
print(ourinvasivetrees)

