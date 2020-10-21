# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
print()
print(f'{" PAR OU ÍMPAR ":*^40}')
print()
from random import randint
from time import sleep
contador = soma = 0
opcprint = opcpc = ''
while True:
    opcjog = int(input('* Digite "0" para PAR ou "1" para ÍMPAR: '))
    while opcjog > 1:
        opcjog = int(input('! Opção inválida. Digite "0" para PAR ou '
                           '"1" para ÍMPAR:'))
    numjog = int(input('* Digite um número de 0 a 5: '))
    while numjog > 5:
        numjog = int(input('! Opção inválida, um número entre 0 e 5: '))
    numpc = randint(1, 5)
    soma = numpc + numjog
    print('* ' * 5)
    sleep(0.5)
    print('PAR')
    sleep(0.5)
    print('OU')
    sleep(0.5)
    print('ÍMPAR!')
    print('* ' * 5)
    if opcjog == 0:
        opcprint = 'PAR'
        opcpc = 'ÍMPAR'
    else:
        opcprint = 'ÍMPAR'
        opcpc = 'PAR'
    print(f'Você escolheu {opcprint} e jogou {numjog}.\nO computador ficou '
          f'com {opcpc} e jogou {numpc}.')
    print(f'A soma deu {soma}, que é ', end='')
    if soma % 2 == 0:
        print('PAR!')
    else:
        print('ÍMPAR!')
    sleep(3.5)
    if opcjog == 0 and soma % 2 == 0:
        print('Ganhou, continue!')
        print()
        contador += 1
    elif opcjog == 1 and soma % 2 != 0:
        print('Ganhou, continue!')
        print()
        contador += 1
    else:
        break
print(' - ' * 25)
print(f'Perdeu... Você ganhou {contador} partida(s) consecutiva(s)!')
print('Tenha um bom dia!')
