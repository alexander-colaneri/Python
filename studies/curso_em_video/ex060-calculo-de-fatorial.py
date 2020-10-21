# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# A forma abaixo seria a usada em Python, porém há linguagens que não têm essa funcionalidade.

'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''
print()
n = int(input('Digite um número para calcular seu fatorial: '))
contador = n  # O contador começa com o número a ser calculado. Por exemplo, fatorial de 5 começa a contagem no 5.
fatorial = 1  # Como serão multiplicações seguidas, a variável não pode começar em "0", senão não avançará.
print(f'Calculando {contador}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')  # Colocar um "x" entre os números maiores que 1.
    fatorial = fatorial * contador
    contador -= 1
print(f'{fatorial}')

# Conforme pedido em aula, abaixo utilizando "for" (já que há como saber a quantidade de repetições do laço).
print('-=' * 40)
num = int(input('Digite o número para cálculo de fatorial: '))
fat = 1
print(f'Calculando {num}! = ', end='')
for cont in range(num, 0, -1):
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
print(fat)