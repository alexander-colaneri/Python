# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
print()
opc = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while opc != 5:  # Se quiser, pode colocar "while not opc == 5".
    print('''As opções são as seguintes: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opc = int(input('Digite a opção desejada: '))
    print()
    if opc == 1:
        soma = n1 + n2
        print(f'A soma dos números {n1} + {n2} = {soma}')
    elif opc == 2:
        mult = n1 * n2
        print(f'A multiplicação dos números {n1} x {n2} é {mult}')
    elif opc == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        elif n1 < n2:
            print(f'O número {n2} é maior que {n1}')
        else:
            print('Os dois números são iguais')
    elif opc == 4:
        print('Recomeçando digitação de números...')
        sleep(1)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opc == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida! Digite novamente.')
    print('=-=' * 10)
print(f'{" Obrigado, tenha um bom dia! ":=^40}')
