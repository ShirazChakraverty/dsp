
# Program Logic explained

# First, we need to import pandas library and also the 
# two main datastructures, numpy and csv for importing the csv file

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

# Read the file into a data frame
faculty_data = pd.read_csv('/Users/schakraverty/ds/metis/metisgh/prework/dsp/python/faculty.csv',sep=',', header = 0,names = ('name','degree','title','email'))

email_data = faculty_data.email
email_data.to_csv('/Users/schakraverty/ds/metis/metisgh/prework/dsp/python/emails.csv', encoding='utf-8', index = False)