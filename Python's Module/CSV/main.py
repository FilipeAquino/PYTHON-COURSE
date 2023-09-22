# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__). parent / "arquivo1.csv"
print(PATH_CSV)

# temos que abrir o arquivo:

with open(PATH_CSV, "r", encoding="utf8") as arq:
    # retorna um generator tem que usar o next para cada linha
    leitor = csv.reader(arq)
    # assim
    # print(next(leitor))
    # print(next(leitor))
    # print(next(leitor))
    # ou:
    # for lin in leitor:
    #     print(lin)

with open(PATH_CSV, "r", encoding="utf8") as arq:
    # ler como dicionario
    leitor = csv.DictReader(arq)
    for linha in leitor:
        print(linha.get("Nome"))

##############
# escrever

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# escrever normal
with open(PATH_CSV, "w+", encoding="utf8") as arq:
    colunas = lista_clientes[0].keys()

    escritor = csv.writer(arq)
    escritor.writerow(colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())

# escrever com dicts
with open(PATH_CSV, "w+", encoding="utf8") as arq:
    colunas = lista_clientes[0].keys()

    escritor = csv.DictWriter(arq, fieldnames=colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
