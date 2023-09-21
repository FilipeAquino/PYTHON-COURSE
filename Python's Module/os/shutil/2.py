# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

path = r"C:\Users\Filipe\Programação\Course\Udemy\Linguagens de Programação" \
    r"\PYTHON\Python's Module\os"
P_ORIGINAL = os.path.join(path, "shutil")
NOVA_PASTA = os.path.join(path, "shutil copy")

# apaga todos os arquivo para ai apagar a pasta
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
# copiando mais facil e sem ´da error
shutil.copytree(P_ORIGINAL, NOVA_PASTA, dirs_exist_ok=True)
# renomendo/ movendo
# shutil.move(NOVA_PASTA, "mudei o nome")
