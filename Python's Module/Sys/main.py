# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys
# vai me mostrar os argumentos mandados no terminal
# print(sys.argv)
# 1- o primeiro argumento sempre é o script que vc vai exevutar
# 2 - os outos vc pode fazer alguma coisa

argumentos = sys.argv
quant = len(argumentos)

print(argumentos, quant, sep="\n\n")
