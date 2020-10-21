# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('-' * 10, 'Conversor de Real em Dólar', '-'*10)
real = float(input('Quantos Reais? R$'))
dólar = real / 5.86
print(f'R${real:.2f} corresponde a US${dólar:.2f}')
