# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
print()
print('*' * 5, 'Analisador de Triângulos V2.0', '*' * 5)
print()
l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
print()
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Os lados {l1}, {l2} e {l3} podem formar um triângulo ', end='') #"end''" colocado para mostrar que
    # a linha não tem fim.
    # Novidade: pode-se colocar "if" dentro de "if"!
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print(f'Os lados {l1}, {l2} e {l3} NÃO podem formar um triângulo!')
