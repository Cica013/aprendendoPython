# https://docs.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta

# strptime(str, fmt)
# .strftime(fmt)
# timestamp()
# from .timestamp()
# data = datetime.fromtimestamp(1631569996.0)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 23:30:00', '%d/%m/%Y %H:%M:%S')
# dif = d2 - d1
# print(dif.days)
print(d2 > d1)
print(d1.time())


