# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html


from dataclasses import dataclass  # é um sugar syntax

# se atribuirmos init=false temos que fazer nosso init


@dataclass(init=False)
# dessa forma o init ja foi executado e os atributos já foram feitos
class Pessoa:
    nome: str
    idade: int

    # Sem init n tem post_init
    def __post_init__(self):  # executado dps do init
        ...

    @property
    def nome_completo(self):
        return f"{self.nome} tem {self.idade} anos"


p1 = Pessoa("filipe", 20)
print(p1.nome)
