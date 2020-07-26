"""
lab 6.6 time, datetime modules
"""

import time
import datetime
# time.clock() # not work!
clock = time.time()
print(time.ctime())
print(time.strftime('%Y'))
print(time.gmtime().tm_yday)
print(time.strftime('%d %b %Y %H:%M'))
print(time.strptime('19 Sep. 2012 10:15', '%d %b. %Y %H:%M'))
curdate = datetime.date.today()
# curdate = datetime.datetime.date(datetime.datetime.now()-1) # not work
dt = curdate + datetime.timedelta(days=-1)
delta = curdate - dt
print(delta)
print(time.time() - clock)
# print(f"exec time = {time.clock()}")
