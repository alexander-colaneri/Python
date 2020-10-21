# Crie um programa que leia números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada. No
# final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).
print()
cont = soma = 0
while True:
    n = int(input('Digite um número ou 999 para terminar: '))
    if n == 999:
        break  # Ao digitar 999, o laço de iteração é desativado e o fluxo
        # segue para a identação exterior.
    cont += 1
    soma += n
print()
print(f'Foram digitados {cont} números e a soma deles é {soma}')
