
from pathlib import Path
from openpyxl import Workbook, load_workbook  # para ler
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / "workbook.xlsx"

# Carregando o arquivo do excel
workbook: Workbook = load_workbook(WORKBOOK_PATH)

# selecionar planilha
worksheet: Worksheet = workbook.active

# pegando as linhas
row: tuple[Cell]
cell: Cell
for row in worksheet.iter_rows(min_row=1):
    for cell in row:
        print(cell.value, end="\t")
        # alterando dentro
        match cell.value:
            case "safira":
                worksheet.cell(cell.row, cell.col_idx + 1, 17)
            case "camila":
                worksheet.cell(cell.row, cell.col_idx + 1, 18)

    print()

workbook.save(WORKBOOK_PATH)
# alterando fora
# worksheet["B3"].value = 20
