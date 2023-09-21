# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

# juntar pastas e arquivos
path = os.path.join(r"\home\user", "desktop", "aqurivoteste.txt")
print(path, "",  sep="\n")
# dividir o caminho em diretorio e arquivo em uma tupla
dir, arq = os.path.split(path)
print(f"Dir:{dir}\nArq: {arq}")
# pegar o caminho e a extensão do arquivo
caminho, extncao = os.path.splitext(path)
print(f'Path: {caminho}\nExtensão: {extncao}')
# vrificar se o caminho existe no sitema
print(os.path.exists(path))  # false
print(os.path.exists(
 r"\Users\Filipe\Programação\Course\Udemy\Linguagens de Programação\PYTHON"
    ))  # true
# rertornar o caminho absoluto:
print(os.path.abspath("."))  # pasta atual
# achar o basename do arquivo e o dirname
print(os.path.basename(caminho))  # parte final do caminho
print(os.path.dirname(caminho))
