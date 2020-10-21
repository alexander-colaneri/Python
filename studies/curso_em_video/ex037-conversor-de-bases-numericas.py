# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print()
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] PARA HEXADECIMAL''')
# Novo aprendizado: você pode colocar um texto entre 3 aspas para ele aparecer como foi escrito.
opção = int(input('Digite a opção excolhida: '))
if opção == 1:
    print(f'{num} convertido em BINÁRIO é igual a {bin(num) [2:]}')
elif opção == 2:
    print(f'{num} convertido em OCTAL é igual a {oct(num) [2:]}')
elif opção == 3:
    print(f'{num} convertido em HEXADECIMAL é igual a {hex(num) [2:]}')
else:
    print('Opção inválida, digite novamente.')
# Obs: nos resultados, antes da resposta, vai aparecer:
# 0b para indicar que é BINÁRIO
# 0o para indicar que é OCTAL
# 0x para indicar que é HEXADECIMAL
# Porém, para excluir dos resultados, foi colocado [2:] para indicar que os resultados sejam exibidos
# da 3a posição em diante.
