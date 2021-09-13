# https://docs.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

# strptime(str, fmt)
# .strftime(fmt)
# timestamp()
# from .timestamp()
# data = datetime.fromtimestamp(1631569996.0)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)
print(mes_atual, mdays[mes_atual])

# dif = d2 - d1
# print(dif.days)
# print(d2 > d1)
# print(d1.time())
