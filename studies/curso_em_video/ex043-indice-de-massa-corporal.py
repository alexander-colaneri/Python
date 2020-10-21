# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print()
print('*' * 5, 'Calculadora de IMC', '*' * 5)
peso = float(input('Digite o peso em quilos: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'O IMC é {imc} e indica ABAIXO DO PESO')
elif imc <= 25:
    print(f'O IMC é {imc:.1f} e indica PESO IDEAL!')
elif imc <= 30:
    print(f'O IMC é {imc:.1f} e indica SOBREPESO!')
elif imc <= 40:
    print(f'O IMC é {imc:.1f} e indica OBESIDADE!')
else:
    print(f'O IMC é {imc:.1f} e indica OBESIDADE MÓRBIDA!')
