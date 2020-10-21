print()
from emoji import emojize

print(emojize(
    '* Leitura de catetos oposto e adjacente de um triângulo retângulo :triangular_ruler:, para cálculo de hipotenusa :smile:. *',
    use_aliases=True))
# "O quadrado da hipotenusa é igual à soma dos quadrados dos catetos: hi² = co² + ca².
# Logo, a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print()
print(f'A hipotenusa mede {hi:.2f}.')
#Agora, utilizando a biblioteca "math".
import math
hi2 = math.hypot(co, ca)
print(emojize(f'A hipotenusa, calculada usando a biblioteca "math" e a funcionalidade "hypot" é {hi2:.2f}. :smiley:', use_aliases=True))
from math import hypot
hi3 = hypot(co, ca)
print(f'A hipotenusa, por outro método de uso de biblioteca ("from/import") mede {hi3:.2f}.')
