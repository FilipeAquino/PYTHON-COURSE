from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(default="Sem nome")
    sobrenome: str = field(default="Sem sobrenome")
    # como os valores padroes n aceitam coisas mutaveis, usamos o field para
    # nos ajudar com isso
    enderecos: list[str] = field(default_factory=list)
    idade: int = 0  # somente pode atribuir se forem imutaveis


if __name__ == "__main__":
    p1 = Pessoa("filipe", "aquino")
    print(fields(p1))  # vai mostrar as configurações feitas nessa classe
    print(p1)
