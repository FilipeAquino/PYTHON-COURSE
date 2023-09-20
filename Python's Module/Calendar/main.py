# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo (talvez esteja errado!)
import calendar

# calendario de 2022
print(calendar.calendar(2023))
# calendario so o mes
print(calendar.month(2023, 8))
# ultimo do dia do mês
print(calendar.monthrange(2023, 8))  # dia, data final
# como saber oq o numero representa
print(list(enumerate(calendar.day_name)))
# saber o dia
print(calendar.weekday(2023, 8, 31))  # mais confiavel
# ver o mes dividido em semanas, onde 0 não significam nada
print(calendar.monthcalendar(2023, 8))
for week in calendar.monthcalendar(2023, 8):
    print(week)
