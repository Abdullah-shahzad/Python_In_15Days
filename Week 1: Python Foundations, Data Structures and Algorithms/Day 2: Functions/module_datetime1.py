import datetime
from zoneinfo import ZoneInfo

# manual added date & time
print(datetime.datetime(2000, 12, 2, 12, 2, 23))

# it will return the current time
now = datetime.datetime.now()
print("Current date and time:", now)

# you can set the format according to your choice
formatted_now = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted_now)

# you can go ahead of the time or go back
delta = datetime.timedelta(days=10)
future_date = now - delta
print("Date 10 days from now:", future_date)

##########

timezone = ZoneInfo('Asia/Karachi')
now1 = datetime.datetime.now(timezone)
print("Current date and time in karachi:", now1)
###########
timezone = ZoneInfo('Asia/Kolkata')

now = datetime.datetime.now(timezone)
print("Current date and time in kolkata:", now)

