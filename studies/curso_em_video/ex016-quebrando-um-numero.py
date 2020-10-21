print()
print('* Programa que leia número real e mostre sua porção inteira *')
print()

import math
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}.')
#Opção 2 usando "from math import trunc".
from math import trunc
print(f'O valor digitado foi {num} e sua porção inteira é {trunc(num)}.')
#Opção 3 para fazer o mesmo cálculo abaixo:
print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}.')


