# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_inicio = datetime(2020, 12, 20)
duracao = relativedelta(years=5)
data_final = data_inicio + duracao
data_parcela = data_inicio
data_parcelas = []

# print(data_parcela + relativedelta(months=+1))

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela = data_parcela + relativedelta(months=1)
# print(data_parcelas)
num_parcelas = len(data_parcelas)
valor_parcela = valor_total / num_parcelas
for data in data_parcelas:

    print(datetime.strftime(data, "%d/%m/%Y"), f"R$ {valor_parcela:,.2f}")

print(
    f'Vc pegou um emprestimo de R$ {valor_total:,.2f} para pagar'
    f'em {duracao.years} anos'
    f'({num_parcelas} meses) em parcelas de R$ {valor_parcela:,.2f}'
    )
