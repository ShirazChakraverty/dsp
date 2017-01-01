# Hint:  use Google to find python function

import pandas as pd
import datetime
import dateutil
from dateutil import parser


####a) 
date_start = "01-02-2013"
date_stop = '07-28-2015'

dt_start = parser.parse(date_start)
dt_stop = parser.parse(date_stop)
date_diff = dt_stop - dt_start
print "number of days:", date_diff.days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

dt_start = datetime.datetime.strptime(date_start, "%m%d%Y")
dt_stop = datetime.datetime.strptime(date_stop, "%m%d%Y")
dt_start = parser.parse(dt_start.strftime("%d-%m-%Y"))
dt_stop = parser.parse(dt_stop.strftime("%d-%m-%Y"))
date_diff = dt_stop - dt_start
print "number of days:", date_diff.days


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

dt_start = datetime.datetime.strptime(date_start, "%d-%b-%Y")
dt_stop = datetime.datetime.strptime(date_stop, "%d-%b-%Y")
dt_start = parser.parse(dt_start.strftime("%d-%m-%Y"))
dt_stop = parser.parse(dt_stop.strftime("%d-%m-%Y"))
date_diff = dt_stop - dt_start
print "number of days:", date_diff.days