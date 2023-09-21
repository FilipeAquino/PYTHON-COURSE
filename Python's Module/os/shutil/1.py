# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

# HOME = os.path.expanduser("~")  # vai pegar o home
path = r"C:\Users\Filipe\Programação\Course\Udemy\Linguagens de Programação" \
    r"\PYTHON\Python's Module\os"
P_ORIGINAL = os.path.join(path, "shutil")
NOVA_PASTA = os.path.join(path, "shutil copy")  # caminho da nova pasta

#  crirando a nova pasta, usar o segundo parametro para evitar error
os.makedirs(NOVA_PASTA, exist_ok=True)


for root, dirs, files in os.walk(P_ORIGINAL):
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        novo_arquivo = os.path.join(root.replace(P_ORIGINAL, NOVA_PASTA), file)
        # copiar as pastas
        shutil.copy(caminho_arquivo, novo_arquivo)

#  for pasta in os.listdir(P_ORIGINAL):
#     print(pasta)

#     if not os.path.isdir(os.path.join(path, pasta)):
#         continue

#     for item in os.listdir(os.path.join(path, pasta)):
#         print("   ", item)
