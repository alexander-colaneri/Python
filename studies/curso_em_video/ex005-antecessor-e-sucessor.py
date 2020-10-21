#  Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número= '))
n1 = n - 1
n2 = n + 1
print(f'Analisando o valor {n}, seu antecessor é {n1} e seu sucessor é {n2}.')
print()
print('Uma segunda forma, mais simples, de fazer, abaixo:')
print()
n = int(input('Digite um número= '))
print(f'Analisando o valor {n}, seu antecessor é {n-1} e seu sucessor é {n+1}.')
