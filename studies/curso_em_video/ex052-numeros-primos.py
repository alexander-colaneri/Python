# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print()
n = int(input('Digite um número: '))
cont = 0
for contador in range(1, n + 1):
    if n % contador == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{contador}', end=' ')
print (f'\n\033[mO número {n} foi divisível {cont} vezes')
if cont == 2:
    print('É um número PRIMO!')
else:
    print('NÃO É um número PRIMO!')
