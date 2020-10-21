# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print()
maior = 0
menor = 0
for a in range(1, 6):
    peso = float(input(f'Digite o peso da {a}ª pessoa: '))
    if a == 1:
        maior = peso
        menor = peso
        # Qual o raciocínio acima? Neste caso, colocamos que a 1a pessoa assim que começa a contagem, é a mais pesada
        # e a menos pesada, pois só ela foi contada até agora.
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
        # Já as pessoas que vêm em seguida, começam a ser comparadas sucessivamente.
print(f'O maior peso lido foi de {maior}Kg, e o menos foi de {menor}Kg')
