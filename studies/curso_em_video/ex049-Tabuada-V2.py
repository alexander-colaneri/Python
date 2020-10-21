# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print()
print(f'{" Calculadora de Tabuada V2.0 ":=^40}')
print()
n = int(input('Digite o número a calcular tabuada: '))
print()
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
