print()
print('* Cálculo de seno, cosseno e tangente de um ângulo *')
print()
# Obs: estes conceitos matemáticos estão sendo usados para mostrar as capacidades do Python, e não necessariamente que para
# se usar o Python é necessário ter conhecimentos matemáticos avançados.
import math

an = float(input('Digite a medida do ângulo: '))
# É preciso, antes, converter o ângulo em graus, usando a funcionalidade "radians" da biblioteca "math" e, em seguida,
# pedir que o Python calcule o seno com a funcionalidade "sin". Para isso, deve se colocar entre parênteses o que deve ser
# feito antes, no caso, a conversão do número digitado em graus e, depois, o cálculo em si.
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'O ângulo de {an} tem o seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}.')
print()
print('*Alternativa 2, importando as funcionalidades no início do código.*')
print()
from math import radians, sin, cos, tan

seno2 = sin(radians(an))
cosseno2 = cos(radians(an))
tangente2 = tan(radians(an))
print(f'Para o ângulo {an}, o seno é {seno2:.2f}, cosseno {cosseno2:.2f} e tangente {tangente2:.2f}.')
