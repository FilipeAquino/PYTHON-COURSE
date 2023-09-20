# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = "%d/%m/%Y %H:%M:%S"
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime("2022-12-13 07:59:23", "%Y-%m-%d %H:%M:%S")
# data = datetime.now()
# essa data(modelo gringo) podemos formatar como queremos
print(datetime.strftime(data, fmt))  # todo formato é str
