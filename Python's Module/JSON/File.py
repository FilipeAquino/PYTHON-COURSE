# os metodos para arquivo

import json
import os
from pathlib import Path

NOME_ARQUIVO = "file.json"
# caminho absoluto com os
# queremos o path absoluto do caminho do diretorio desse arquivo
# mais o nome do arquivo qu quermeos
PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
)
print(PATH)
# em pathlib
PATH2 = Path(__file__).parent / NOME_ARQUIVO
print(PATH2)

string_ = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

if not Path.exists(PATH2):
    PATH2.touch()

with open(PATH2, "w+", encoding="utf8") as arquivo:

    json.dump(string_, arquivo, ensure_ascii=False, indent=2)

with open(PATH2, "r+", encoding="utf8") as arquivo:

    string_ = json.load(arquivo)
    print(string_)
