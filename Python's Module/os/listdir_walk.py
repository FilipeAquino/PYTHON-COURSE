# para navegar pelos caminhos
# C:\user\filipe\Desktop\EXEMPLE

import os

path = r"C:\Users\Filipe\Programação\Course\Udemy" \
 r"\Linguagens de Programação\PYTHON\POO"
print(path)
# vai nos mostrar os item que tem na pasta numa lista
for pasta in os.listdir(path):
    print(pasta)

    if not os.path.isdir(os.path.join(path, pasta)):
        continue

    for item in os.listdir(os.path.join(path, pasta)):
        print("   ", item)
