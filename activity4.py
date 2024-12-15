import datetime
currenttime=datetime.datetime.now()
print("current time is",currenttime)
print("current time is",currenttime.strftime("%Y"))
print("current month is",currenttime.strftime("%B"))
import calendar
print(calendar.calendar(2025))