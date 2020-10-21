# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print()
print('*' * 5, 'Calculadora de aumento de salário', '*' * 5)
print()
salário = float(input('Digite o valor atual de salário: '))
if salário >= 1250.00:
    print(f'O novo valor de salário é {(salário * 10) / 100 + salário:.2f}')
else:
    print(f'O novo valor de salário é {(salário * 15) / 100 + salário:.2f}')