print('*'*5, 'Cálculo de tinta para parede', '*'*5)
print()
print('Obs: cada litro de tinta pinta uma área de 2m²')
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura * altura
tinta = (largura * altura) / 2
print()
print(f'A área da parede é de {área}m² e a quantidade de tinta necessária é de {tinta}l.')