# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
from pprint import pprint  # para ver melhor
from typing import TypedDict  # tipar os dicts para o vs conhecer


class Movvie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_ = """
    {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
  }
"""

# pegar o JSON e trazer para o python
movie: Movvie = json.loads(string_)
pprint(movie.get('characters'))

# pegar em python e levar para json:
# ensure_ascii false vai colocar os acentos e sinais
# indent vai arrumar a vizualização
print(json.dumps(movie, ensure_ascii=False, indent=2))
