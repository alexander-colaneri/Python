print()
print('*'*5, 'Cálculo de reajuste de salário', '*'*5)
print()
salário = float(input('Digite o valor do salário: R$'))
porcent = float(input('Digite a porcentagem de aumento: '))
aumento = salário * porcent / 100
novosala = salário + aumento
print()
print(f'O valor do aumento é de R${aumento:.2f}.')
print(f'O novo valor de salário é R${novosala:.2f}.')
