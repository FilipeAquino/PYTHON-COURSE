from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    idade: int


p1 = Pessoa("filipe", 20)
print(p1)
print(asdict(p1))  # transforma a dataclass em um dicionario
print(astuple(p1))  # transforma a dataclass em uma tupla
