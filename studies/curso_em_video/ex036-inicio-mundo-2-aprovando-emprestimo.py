print()
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.
from emoji import emojize

print(emojize(':house_with_garden: Calculadora de Prestação para Compra de Casa :house_with_garden:', use_aliases=True))
print()
casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o valor do salário: R$'))
anos = int(input('Digite a quantidade de anos para pagamento: '))
print()
meses = anos * 12
prestação = casa / meses
if prestação >= salário * 30 / 100:
    print(f'O valor da prestação é R${prestação:.2f}, com pagamento em {meses} meses.'
          f'\nO valor permitido de prestação, de acordo com o salário, é de até R${salário * 30 / 100:.2f}.'
          f'\n\033[1;31mPagamento não aprovado.\033[m')
else:
    print(f'O valor da prestação é R${prestação:.2f}, com pagamento em {meses} meses.'
          f'\nO valor permitido de prestação, de acordo com o salário, é de até R${salário * 30 / 100}.'
          f'\n\033[1;32mPagamento aprovado!\033[m')
