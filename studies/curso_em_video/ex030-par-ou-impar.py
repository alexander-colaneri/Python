# Crie um programa que leia um número inteiro e mostre na tela se é par ou ímpar.
print()
print('*' * 10, 'É impar ou par?', '*' * 10)
n = int(input('Digite um número inteiro: '))
# O resto da divisão de qualquer número par é 0, e de qualquer número ímpar é 1.
resposta = n % 2
if resposta == 0:
    print('\033[0;33mO número é par!\033[m')
else:
    print('\033[0;35mO número é ímpar!\033[m')
# Escrevendo a condição de forma simplificada:
print(f'O número é par mesmo!' if resposta == 0 else 'O número é ímpar de verdade!')
