#faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
 #             'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

# Program Logic explained

# First, we need to import pandas library and also the 
# two main datastructures, numpy and csv for importing the csv file

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

# Read the file into a data frame
faculty_data = pd.read_csv('/Users/schakraverty/ds/metis/metisgh/prework/dsp/python/faculty.csv',sep=',', header = 0,names = ('name','degree','title','email'))

faculty_data.degree = faculty_data.degree.str.replace(".","")
faculty_data.title = faculty_data.title.str.replace(" is "," of ")

faculty_data['firstname'] = faculty_data['name'].apply(lambda x: x.split(' ')[0])
faculty_data['lastname'] = faculty_data['name'].apply(lambda x: x.split(' ')[-1])

faculty_data1 = faculty_data[['lastname','degree','title','email']]

fac_dict = {}

x = faculty_data1.values
y = len(x)      
z = 0
while z < y:
    key =  x[z][0]
    a = x[z][1]
    b = x[z][2]
    c = x[z][3]
    value_pair =  [a,b,c]
    fac_dict.setdefault(key,[]).append(value_pair)
    z = z + 1

first3key_val_pairs = {k:fac_dict[k] for k in sorted(fac_dict.keys())[:3]}

print "\n"
print "Q6. : First three key value pairs", "\n"
print first3key_val_pairs

"""
>>> Q7. A more efficient dict key design
>>>
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
, ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], 
('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
"""


faculty_data2 = faculty_data[['firstname','lastname','degree','title','email']]
#faculty_data2 = faculty_data2.sort('lastname')

fac_dict2 = {}

x = faculty_data2.values
y = len(x)      
z = 0
while z < y:
    k1 = x[z][0]
    k2 = x[z][1]
    key = (k1,k2)
    a = x[z][2]
    b = x[z][3]
    c = x[z][4]
    #value_pair =  [a,b,c]
    fac_dict2.setdefault(key,[]).append(a)
    fac_dict2.setdefault(key,[]).append(b)
    fac_dict2.setdefault(key,[]).append(c)
    z = z + 1

first3key_val_pairs2 = {k:fac_dict2[k] for k in sorted(fac_dict2.keys())[:3]}

print "\n"

print "Q7. : First three key value pairs, with key as first name and last name", "\n"

print first3key_val_pairs2

print "\n"

print "Q8. : First three key value pairs, with key sorted by last name", "\n"


keylist = fac_dict2.keys()
keylist = sorted(keylist, key=lambda x: x[-1])
counter = 1
for k in keylist:
    print k ,":", fac_dict2[k]
    counter = counter + 1
    if counter > 3:
        break
    else:
        continue

