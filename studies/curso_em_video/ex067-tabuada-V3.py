# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.
print(f'{" TABUADA V3 ":*^40}')
n = 0
while True:
    n = int(input('Quer ver a tabuada de que valor? (Digite qualquer valor '
                  'negativo para encerrar) '))
    print('-' * 20)
    if n < 0:
        break
    for mult in range(1, 11):
        print(f'{n} x {mult} = {n * mult} ')
    print('-' * 20)
print('Tenha um bom dia!')
