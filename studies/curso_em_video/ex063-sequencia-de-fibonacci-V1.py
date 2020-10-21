# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
print()
print('=' * 7, 'FIBONACCI V1', '=' * 7)
print()
n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} - {termo2}', end='')  # Sequência de Fibonacci inicia com 0
# e 1, portanto já
# colocar os 2 primeiros prints.
contagem = 3  # A contagem começa em "3" porque os primeiros 2 termos de uma
# sequência de Fibonacci serão sempre 0 e 1.
while contagem <= n:
    termo3 = termo1 + termo2
    print(f' - {termo3}', end='')
    # Muita atenção abaixo! Faremos com que na próxima repetição do laço,
    # o termo 1 receba o termo 2, e o termo 2 receba o termo 3! Desta forma,
    # vamos escalando a soma, até que "n" seja igual ao número digitado no
    # início.
    termo1 = termo2
    termo2 = termo3
    contagem += 1
print(' - Fim')
