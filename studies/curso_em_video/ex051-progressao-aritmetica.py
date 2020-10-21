# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
# 10 primeiros termos desta progressão.
print()
ptermo = int(input('Digite o primeiro termo: '))
n = int(input('Digite o valor do enésimo número: '))
razão = int(input('Digite o valor da razão: '))
décimo = ptermo + (n - 1) * razão # o exercício pede que avancemos 10 vezes. Logo n tem que ser = 10
for c in range(ptermo, décimo + razão, razão): # para 10 exibições, acrescentado "+ razão" na hora do intervalo
    # final, pois o Python não mostra o último número do range.
    print(c, end=' - ')
print('FIM')