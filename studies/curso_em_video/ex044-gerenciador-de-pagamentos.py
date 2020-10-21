# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print()
print(f'{" LOJAS POLENTÃO ":*^45}')
print()
preço = float(input('Digite o preço do produto ou serviço: '))
print()
print('''As opções de pagamento são:
[ 1 ] - À vista em dinheiro/cheque.
[ 2 ] - À vista no cartão.
[ 3 ] - Em 2x no cartão.
[ 4 ] - Em 3x ou mais no cartão.''')
print()
opção = int(input('Digite a opção selecionada acima: '))
if opção == 1:
    desconto = preço * 10 / 100
    total = preço - desconto
    print(f'''* Desconto de R${desconto:.2f}
* TOTAL: R${total:.2f}''')
elif opção == 2:
    desconto = preço * 5 / 100
    total = preço - desconto
    print(f'''* Desconto: R${desconto:.2f}
* TOTAL: R${total:.2f}.''')
elif opção == 3:
    parcela = preço / 2
    print(f'''* 2 parcelas sem juros de R${parcela:.2f}
* TOTAL: R${preço:.2f}''')
elif opção == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print()
    if parcelas <= 2:
        print('Opção inválida. Escolha uma opção a partir de 3 parcelas.')
    elif parcelas >= 3:
        juros = preço * 20 / 100
        total = preço + juros
        valorparcela = total / parcelas
        print(f'''Opção com parcelamento (3x ou mais), COM JUROS:
* Juros (20%): R${juros:.2f}
* {parcelas}x de R${valorparcela:.2f}
* TOTAL: De R${preço:.2f} para R${total:.2f}''')
