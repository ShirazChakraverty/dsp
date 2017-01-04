# Program Logic explained

# First, we need to import pandas library and also the 
# two main datastructures, numpy and csv for importing the csv file

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

# Read the file into a data frame
faculty_data = pd.read_csv('/Users/schakraverty/ds/metis/metisgh/prework/dsp/python/faculty.csv',sep=',', header = 0,names = ('name','degree','title','email'))

faculty_data.degree = faculty_data.degree.str.replace(" ",",")
faculty_data.degree = faculty_data.degree.str.replace(".","")
faculty_data.title = faculty_data.title.str.replace(" is "," of ")
degree_freq = {'Phd':0,'ScD':0,'MD':0,'MPH':0,'BSEd':0,'MS':0,'JD':0,'MA':0}

for key,val_d in degree_freq.iteritems():
        degree_freq[key] = faculty_data.degree.str.contains(key,case=False).sum()
# Q1. print the degree frequency in a neat table
print "Degree","Frequency"
sorted_degree = degree_freq.items()
sorted_degree.sort()
for k, v in sorted_degree:
     print k,"        ", v

#Q2. The different titles and their frequencies
titles = faculty_data.groupby(by='title')
print titles.count()

#Q3. Put the emails in a list and print:

email_list = list(faculty_data.email)

print email_list

faculty_data['domains'] = faculty_data['email'].apply(lambda x: x.split('@')[1])
domains = faculty_data.groupby(by='domains')
print domains.domains.count()

