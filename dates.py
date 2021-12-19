import datetime

today_date = datetime.datetime.now()
print(today_date.strftime("%d-%m-%Y %H:%M:%S"))

tmr_date = today_date + datetime.timedelta(days=1)
print(tmr_date.strftime("%d-%m-%Y"))

import datetime

today_date = datetime.datetime.now()
print(today_date)

tmr_date = today_date + datetime.timedelta(days=1)
print(tmr_date)