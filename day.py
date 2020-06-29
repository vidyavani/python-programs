import datetime
import calendar
date=input()
date=datetime.datetime.strptime(date,'%m %d %Y').weekday()
s=calendar.day_name[date]
print(s.upper())
