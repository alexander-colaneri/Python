# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('=== Conversão de medidas ===')
n = float(input('Insira a distância em metros= '))
print(
    f'A medida {n}m corresponde a: \n{n * (1 / 1000)}Km\n{n * (1 / 100)}hm\n{n *(1 / 10)}dam\n'
    f'{n * 10:.0f}dm\n{n * 100:.0f}cm\n{n * 1000:.0f}mm')

