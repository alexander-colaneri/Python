# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).
print()
n = int(input('Digite um número [999 para parar]: '))
contagem = soma = 0
while n != 999:
    contagem += 1
    soma = soma + n
    n = int(input('Digite um número [999 para parar]: '))  # Percebeu que
    # esta linha é igual ao input? Foi colocado no final para repetir o
    # pedido de inserção, mas para que o 999 (o "flag") não seja somado e o
    # contador não adicione mais uma repetição à contagem. Ao digitar "999",
    # ao subir para uma repetição, ele "ficará preso" na primeira condição,
    # o "while".
print(f'Foram {contagem} números digitados e a soma é {soma}')
print('Fim')
