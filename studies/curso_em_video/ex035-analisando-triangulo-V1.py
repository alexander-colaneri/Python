# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.
print()
print('*-' * 7, 'Analisador de Triângulos', '*-' * 7)
# Regra matemática. Para um triângulo "fechar", a soma de dois lados não pode ser menor que um dos lados.
# Ou seja, por exemplo, lado1 < lado2 + lado3
l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))
print()
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Os lados {l1}, {l2} e {l3} podem formar um triângulo!')
else:
    print(f'Os lados {l1}, {l2} e {l3} NÃO podem formar um triângulo!')

