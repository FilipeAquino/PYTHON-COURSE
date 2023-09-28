# openpyxl para arquivos Excel xlsx, xlsm, xltx e xltm (instalação)
# Com essa biblioteca será possível ler e escrever dados em células
# específicas, formatar células, inserir gráficos,
# criar fórmulas, adicionar imagens e outros elementos gráficos às suas
# planilhas. Ela é útil para automatizar tarefas envolvendo planilhas do
# Excel, como a criação de relatórios e análise de dados e/ou facilitando a
# manipulação de grandes quantidades de informações.
# Instalação necessária: pip install openpyxl
# Documentação: https://openpyxl.readthedocs.io/en/stable/

from typing import List
from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / "workbook.xlsx"

# criando  planilha
workbook = Workbook()  # é o todo com todas as planilhas
# ativando as planilhas
# worksheet: Worksheet = workbook.active

# criando uma nova planilha e selecionando
NAME = "minha planilha"
workbook.create_sheet(NAME)
# worksheet: Worksheet = workbook[NAME]
worksheet: Worksheet = workbook.active

# removendo uma planilha
# workbook.remove_sheet(workbook[NAME])

# criando o header
worksheet.cell(1, 1, "Nome")  # linha, coluna, nome
worksheet.cell(1, 2, "Idade")
worksheet.cell(1, 3, "Nota")

students: List[List[str | int]] = [
        # nome   idade   curso
        ["filipe", 20, "engenharia EL"],
        ["camila", 18, "engenharia C."],
        ["safira", 17, "engenharia En"],
        ["eduardo", 19, "direito"]
]

# Fazendo a logica para adicionar as informações

for i in range(2, 10):  # as linhas desconsiderando o header por isso o 2
    for j in range(1, 4):
        print(f'linha: {i} coluna: {j}')

# adicionando na planinha
# for i, student_row in enumerate(students, start=2):
#     for j, student_column in enumerate(student_row, start=1):
#         print(i, j, student_column)
#         worksheets.cell(i, j, student_column)

# adicionado valores na planilha mais facil
for student in students:
    worksheet.append(student)

# vamos salvar a panilha
workbook.save(WORKBOOK_PATH)
