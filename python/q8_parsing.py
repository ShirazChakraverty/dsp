# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

# Read the file into a data frame

football_data = pd.read_csv('/Users/schakraverty/ds/metis/metisgh/prework/dsp/python/football.csv',sep=',', header = 0,names = ('team','games','wins','losses','draws','goals','goals_allowed','points'))

fd = football_data
fd['goal_difference'] = fd.goals - fd.goals_allowed

fd['goal_difference'] = fd.goal_difference.abs()

print fd['team'][fd.goal_difference==fd.goal_difference.min()]
