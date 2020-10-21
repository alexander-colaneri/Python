# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

print()
from datetime import date
contmenor = 0
contmaior = 0
anohj = date.today().year
for contagem in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da pessoa {contagem}: '))
    if anohj - ano >= 18:
        contmaior += 1
    else:
        contmenor += 1
print(f'Há um total de {contmaior} pessoas maiores de idade e {contmenor} pessoas menores de idade.')
