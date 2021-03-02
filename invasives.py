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
#TODO why is this adding square brackets?
def SPECIESNAME(row):
    return re.findall(pattern='\(([^)]+)\)', string=row['Species'])
ourtrees['Scientific'] = ourtrees.apply(lambda row: SPECIESNAME (row),axis=1)

# print out information from the survey
print('Scientific Names Counts:')
scientificcounts = ourtrees['Scientific'].value_counts(sort=True)
print(scientificcounts)