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

sleep(0.5)
print('*JO*')
sleep(0.5)
print('*KEM*')
sleep(0.5)
print('*PÔ!!!*')
print()
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
if escolha >= 3:
    print('Opção inválida, tente novamente!')

elif escolha == comp:
    print(f'=== Você jogou {itens[escolha]} e o computador {itens[comp]} ===!')
    print(f'{" EMPATE! Jogue novamente! ":*^40}')

elif comp == 0 and escolha == 2:
    print(f'=== Você jogou {itens[escolha]} e o computador {itens[comp]} ===!')
    print(f'{" PERDEU! Jogue novamente! ":*^40}')

elif comp == 2 and escolha == 1:
    print(f'=== Você jogou {itens[escolha]} e o computador {itens[comp]}! ===')
    print(f'{" PERDEU! Jogue novamente! ":*^40}')

elif comp == 1 and escolha == 0:
    print(f'=== Você jogou {itens[escolha]} e o computador {itens[comp]}! ===')
    print(f'{" PERDEU! Jogue novamente! ":*^40}')

else:
    print(f'=== Você jogou {itens[escolha]} e o computador {itens[comp]}! ===')
    print(f'{" VOCÊ GANHOU!!! ":*^40}')

# Obs: para que as strings "PEDRA", "PAPEL" e "TESOURA" aparecessem no lugar dos números nos prints,
# foi colocado o seguinte:
# itens[escolha]: "exiba os itens de acordo com a escolha/comp apresentados".
# Ou seja, por exemplo, se o computador escolhesse aleatoriamente o número 1,
# seria exibido o item na posição 1 da énople pré-determinada (itens), no caso, "PAPEL".
