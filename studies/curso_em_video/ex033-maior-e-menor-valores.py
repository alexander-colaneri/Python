# Faça um programa que peça 3 números e indique qual é o maior e qual é o menor.
print()
print('* Digite 3 números abaixo *')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# Dica: já pré-determine, etiquete, um número como o menor.
# Abaixo, fazer a verificação de qual é o menor.
# menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a < c and a < b:
    menor = a
# Agora, a verificação de qual é o maior.
# maior = a
if b > a and c > a:
    maior = b
if c > a and c > b:
    maior = c
if a > c and a > b:
    maior = a
print()

# Criei referências dos códigos de cor, para testar, conforme abaixo:

red = '\033[;31m'
green = '\033[;32m'

print(f'O menor número é {red}{menor}\033[m e o maior número é {green}{maior}\033[m.')
