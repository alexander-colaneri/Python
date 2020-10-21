# Jogo de adivinhação
# Escreva um programa que faça o computador pensar em um número de 0 a 5, e você adivinhar.

print()
from random import randint
from emoji import emojize
from time import sleep
# A funcionalidade "sleep" faz com que o computador espere a quantidade de segundos que incluir.
ncomp = randint(0, 5)
print(emojize('Vou pensar em um número, vamos ver se você adivinha! :smirk:', use_aliases=True))
n = int(input('Digite um número de 0 a 5: '))
print('Vamos ver...')
sleep(2)
if n == ncomp:
    print(emojize(f'Isso mesmo, o número que pensei foi {ncomp}! Arrebentou!:smile:', use_aliases=True))
else:
    print(emojize(f'O número que pensei foi {ncomp}. Não foi dessa vez, tente novamente! :confused:', use_aliases=True))
