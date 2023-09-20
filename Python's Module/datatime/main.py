# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime, timezone  # é uma class
# somente a data ano,mes,dia
data = datetime(2023, 9, 19)
print(data)
# data e horas, min, seg
data = datetime(2023, 9, 19, 10, 55, 59)
print(data)
# tranformar str em data e hora
data_str = "2002-5-09 10:59:01"
# adicionar str e formato
data = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
print(data)
# pegar dia e hora de agr:
data = datetime.now()
print(data)
# datetime com timezone
data = datetime.now(tz=timezone.utc)
print(data)
# segundo de 01/01/1970 ate hj
data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(12548855))  # vai gerar um datetime com isso
