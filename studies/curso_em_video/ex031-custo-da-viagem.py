# Custo de viagem - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas.
print()
print('*' * 10, '\033[1;31;40mCalculadora de preços de viagem!\033[m', '*' * 10)
print()
km = int(input('Digite a distância em Km: '))
if km <= 200:
    print(f'O valor da passagem é R${km * 0.50:.2f}.')
else:
    print(f'O valor da passagem é R${km * 0.45:.2f}.')
# Fazendo do modo "if line", que é o if simplificado:
preço = km * 0.50 if km <= 200 else km * 0.45
print(f'O valor da passagem é R${preço:.2f}.')

