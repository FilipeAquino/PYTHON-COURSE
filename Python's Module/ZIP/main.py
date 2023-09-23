# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'descompactado'

# deletando todos os arquivo criados de forma recurciva
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

# vamos abrir a pasta que tem os arquivos com os.walk()
# e passar os arquivos para a pasta compactada, compactando-as
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)

# lendo e extraindo arquivos
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    # zip.namelist() serve para saber os arquivos dentro do zip
    for arquivo in zip.namelist():
        print(arquivo)
    # extraindo todo arquivo
    zip.extractall(CAMINHO_DESCOMPACTADO)
