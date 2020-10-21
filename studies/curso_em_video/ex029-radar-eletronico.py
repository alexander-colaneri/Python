# Radar Eletrônico
# Enunciado: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
# mostre uma mensagem de multa. A multa custa R$7,00 por cada Km acima do limite.
print()
print( '*' * 10, 'Radar Eletrônico', '*' * 10)
print()
v = int(input('Digite a velocidade: '))
if v <= 80:
    print(f'Velocidade detectada: {v}Km/h. \033[1;32mTudo ok! Obrigado, pode continuar sua viagem!\033[m')
else:
    print(f'Velocidade detectada: {v}Km/h.\nVocê excedeu a velocidade em {v - 80}Km/h.\nVocê foi multado.\nValor da '
          f'multa = R${(v - 80) * 7 :.2f}.')
