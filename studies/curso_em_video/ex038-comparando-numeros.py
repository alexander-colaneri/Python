# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
print()
print('\033[0;32m*\033[m' * 5, 'Comparador de números', '\033[0;32m*\033[m' * 5)
print()
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
print()
if n1 > n2:
    print(f'O número {n1} é MAIOR que {n2}!')
elif n2 > n1:
    print(f'O número {n2} é MAIOR que {n1}!')
else:
    print(f'O número {n1} é IGUAL a {n2}!')
