# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:42:45 2018

@author: HP 15-E015TX
"""

import datetime
datetime.datetime.today()


from datetime import datetime as dt
time=dt.today()


print(time)
print(type(time))
str(time)[:10] #for today's date

   
from datetime import datetime, timedelta
today = dt.today()
print(today)
_7day_ago = today - timedelta(7)
print(_7day_ago)
_7day_after = today + timedelta(7)
print(_7day_after)


this_moment = dt.now()
this_moment.year
this_moment.day
this_moment.month
this_moment.hour


#formatting datetime
my_date1 = "15/04/2018"
my_date2 = "2018-31-07"



#takes date strings as inputs - strptime() function
dt_my_date1 = dt.strptime(my_date1, "%d/%m/%Y")
dt_my_date2 = dt.strptime(my_date2, "%Y-%d-%m")		

																	
# we need to convert an existing datetime object to formatted string - strftime()
										
#23 June 2018
formatted_date = dt.strftime(dt_my_date1, "%d %B %Y")
print(formatted_date)

import pafy
import os
os.chdir(r"F:\KeepVid Free Converted")

fileList = open("F:\KeepVid Free Converted\yt_4k.txt","r")

for file in fileList:
	video = pafy.new(file)
	video.getbest().download(quiet=False)






