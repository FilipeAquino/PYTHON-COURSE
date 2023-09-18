# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple
from typing import NamedTuple
from collections import namedtuple

Carta = namedtuple("carta", ["valor", "naipe"],
                   defaults=["", ""])  # dando valores padrao para o naipe e
# valor


espadas = Carta("A", "Espadas")

print(espadas._fields)  # oq tem que ir nela
print(espadas._field_defaults)  # os valores padroes dela
print(espadas)

# outra forma de fazer:


class Carta(NamedTuple):
    valor: str = "valor"
    name: str = "naipe"

# vai funcinar igual
