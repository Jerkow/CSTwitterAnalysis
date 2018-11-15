import datetime as dt
str = "Thu Jul 28 00:08:39 +0000 2016"
date = dt.datetime.strptime(str[3:], ' %b %d %H:%M:%S +0000 %Y')
print(date.day)
print(date.month)
print(date.year)
print(date.hour)
