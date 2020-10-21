# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre: A)
# qual é o total gasto na compra. B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print()
print(f'{" LOJAS POLENTÃO ":*^40}')
total = qt_produto_1000 = menor_preco = preco = 0
produto_mais_barato = ' '
contador = 0
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$'))
    if contador == 0 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto
        # Obs: percebe que a parte abaixo é igual à acima? Então, podemos
        # embutí-la com um "or" (veja acima), para aproveitar o mesmo
        # processamento e diminuir linhas.
    # if preço < menor_preço:
        # produto_mais_barato = produto
    if preco > 1000:
        qt_produto_1000 += 1
    total += preco
    print()
    prosseguir = str(input('Adicionar outro produto? [S/N] ')).strip().upper()
    print('-' * 30)
    while prosseguir != 'N' and prosseguir != 'S':
        prosseguir = str(input('Opção inválida, '
                               'digite novamente [S/N]: ')).strip().upper()
    if prosseguir == 'N':
        break
    contador += 1
print()
print('======== RESUMO =======')
print(f'TOTAL: R${total:.2f}')
print(f'{qt_produto_1000} produtos custaram mais de R$1000,00')
print(f'Produto mais barato é {produto_mais_barato}, no valor de '
      f'R${menor_preco:.2f}')
print()
print('***** TENHA UM BOM DIA *****! ')
