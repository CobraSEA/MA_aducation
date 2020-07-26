import sys
import datetime
import time
import argparse

print(sys.platform)
print(sys.argv)

print(time.gmtime())
print(time.asctime(time.localtime(time.time())))
print(str(datetime.datetime.now()))
print(str(datetime.date.today()))

