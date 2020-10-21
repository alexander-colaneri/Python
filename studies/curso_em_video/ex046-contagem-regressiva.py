# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
print()
print(f'{" CONTAGEM REGRESSIVA! ":*^40}')
print()
from time import sleep
from emoji import emojize

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('0')
print()
print(emojize(f'\033[1;33m{(":smile: ") * 3}\033[m {" FELIZ 2021!! ":*^40} \033[1;33m{(":smile: ") * 3}\033[m', use_aliases=True))
