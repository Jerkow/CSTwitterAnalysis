import datetime as dt
import time
str = "Thu Jul 28 01:08:00 +0000 2016"
date = dt.datetime.strptime(str[3:], ' %b %d %H:%M:%S +0000 %Y')
print(date.day)
print(date.month)
print(date.year)
print(date.hour)
print(date)
a=time.mktime(date.timetuple())
print(int(a)//3600)
print(dt.datetime.fromtimestamp(a))
print(dt.datetime.fromtimestamp(a-int(a)%3600))
