# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime("20/04/1987 09:30:30", fmt)
data_final = datetime.strptime("12/12/2022 08:20:20", fmt)
# podemos comparar
print(data_final > data_inicio)
print(data_final < data_inicio)
print(data_final == data_inicio, sep="\n")
# operações
print(data_final - data_inicio)
# delta é um dado que pode represnetar a diferença
delta = data_final - data_inicio
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
# criando uma timedelta
delta = timedelta(days=10, minutes=60)
print(delta)
print(delta + data_final)  # soma
# com o relaticedelta tem mais opções para o timedelta
print(data_final + relativedelta(yearday=45))
print(relativedelta(data_final, data_inicio))  # retorna a difereça
# vc pode pegar separadamente pq sao atributos
