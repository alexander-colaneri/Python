print()
print('*'*5, 'Cálculo de preço de produto - pagamento à vista X parcelado', '*'*5)
print()
p = float(input('Digite o valor do produto: R$'))
porv = float(input('Digite o valor da porcentagem de desconto para compra à vista: '))
porp = float(input('Digite o valor da porcentagem de acréscimo para compra a prazo: '))
parcelas = int(input('Digite a quantidade de parcelas: '))
vdesc = p * porv / 100
vacre = p * porp / 100
pcomdesc = p - vdesc
pcomacre = p + vacre
vparcela = pcomacre / parcelas
print()
print('*', 'Pagamento à Vista', '*')
print(f'Para compra à vista, o desconto é de {porv}%.\nO valor do desconto é R${vdesc:.2f} e o preço é R${pcomdesc:.2f}.')
print()
print('*', 'Pagamento Parcelado', '*')
print(f'Para compra parcelada, o acrésimo é de {porp}%.\nO valor do acréscimo é R${vacre:.2f} e o preço é R${pcomacre:.2f}.')
print(f'A compra poderá ser parcelada em {parcelas}x e o valor da parcela é R${vparcela:.2f}.')

