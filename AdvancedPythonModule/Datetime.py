import datetime
t=datetime.time(2,23,1,1)
print(t)
print(t.hour)
print(t.second)
print(t.min)
print(t.microsecond)
print(t.min)
print(t.max)
print(t.resolution)

today=datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.timetuple())
print(today.min)
print(today.max)
d1=datetime.date(2018,8,27)
print(d1)
d2=d1.replace(year=1991)
print(d2)

