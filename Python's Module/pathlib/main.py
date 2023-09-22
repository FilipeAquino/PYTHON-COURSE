# usado para manipular caminhos, pastas e arquivos
from pathlib import Path
from shutil import rmtree

PATH = Path()
print(f"Caminho Relativo {PATH}")
print(f"Caminho absoluto {PATH.absolute()}")
PATH = Path(__file__)
print(f"Caminho do arquivo {PATH}")
print(f"Caminho para pasta do arquivo {PATH.parent}")
print(f"Caminho para pasta da pasta do arquivo {PATH.parent}")
print(f"Caminho da HOME: {PATH.home()}")
novo_path = PATH.parent / "arquivogeradodomodulo.txt"
# cirando a/o pasta/arquivo:
novo_path.touch(exist_ok=True)  # serve para atualizar tbm
print("Criado")
novo_path.write_text("Winner")
print("escreveu")
# novo_path.unlink()  # pode apagar o arquivo ou pasta
print("apagado")
print(novo_path.read_text())  # ler oq tem nele
# criar um diretório
path_pasta = PATH.parent / "pastadeteste"
path_pasta.mkdir(exist_ok=True)  # pasta criada
print("apagado")


dir_ = PATH.parent / "teste"
dir_.mkdir(exist_ok=True)
for i in range(60):
    file = dir_ / f"files_{i}.txt"
    file.touch()

    if file.exists():
        file.unlink(missing_ok=True)
    else:
        file.touch()

    with file.open("+a", encoding="utf8") as arq:
        arq.write("ola mundo \n")
        arq.write(f"files_{i}.txt")

# apagar de forma recursica:
path_pasta.rmdir()  # se a pasta tiver vazia
# apagar de forma recursica:
rmtree(dir_)  # apaga tudo de pastas a arquivos
