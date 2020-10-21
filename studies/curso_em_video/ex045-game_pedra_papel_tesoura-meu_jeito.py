# Crie um programa que faça o computador jogar Jokenpô com você.
print()
print(f'{" JoKemPô ":*^36}')
print()
print('''Bem-vindo ao jogo! Abaixo as opções para jogar!
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
escolha = int(input('Digite o número da sua escolha: '))
from random import randint
from time import sleep

sleep(1)
print('*JO*')
sleep(1)
print('*KEM*')
sleep(1)
print('*PÔ*')
print()
comp = randint(0, 1)
if escolha >= 3:
    print('Opção invalida, tente novamnte!')

elif escolha == comp:
    print(
        f'=== Você jogou {escolha} e o computador {comp} ===!'.replace('0', 'PEDRA').replace('1', 'PAPEL').replace('2',
                                                                                                                   'TESOURA'))
    print(f'{" EMPATE! Jogue novamente! ":*^40}')

elif comp == 0 and escolha == 2:
    print(
        f'=== Você jogou {escolha} e o computador {comp} ===!'.replace('0', 'PEDRA').replace('1', 'PAPEL').replace('2',
                                                                                                                   'TESOURA'))
    print(f'{" PERDEU! Jogue novamente! ":*^40}')

elif comp == 2 and escolha == 1:
    print(
        f'=== Você jogou {escolha} e o computador {comp}! ==='.replace('0', 'PEDRA').replace('1', 'PAPEL').replace('2',
                                                                                                                   'TESOURA'))
    print(f'{" PERDEU! Jogue novamente! ":*^40}')

elif comp == 1 and escolha == 0:
    print(
        f'=== Você jogou {escolha} e o computador {comp}! ==='.replace('0', 'PEDRA').replace('1', 'PAPEL').replace('2',
                                                                                                                   'TESOURA'))
    print(f'{" PERDEU! Jogue novamente! ":*^40}')

else:
    print(
        f'=== Você jogou {escolha} e o computador {comp}! ==='.replace('0', 'PEDRA').replace('1', 'PAPEL').replace('2',
                                                                                                                   'TESOURA'))
    print(f'{" VOCÊ GANHOU!!! ":*^40}')
