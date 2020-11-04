# Descrição: Crie um programa que leia quanto dinheiro uma pessoa tem na 
# carteira e mostre quantos dólares ela pode comprar.

class ConversorDolares():
    '''Converte o valor em Reais para Dólares. US$ 1 == R$ 5.76 em Nov/2020'''
    dolar = 5.76

    def __init__(self):
        self.reais = 0

    def converter_reais_para_dolares(self):
        '''Converte e exibe o resultado.'''
        print('Indique o valor em Reais:')
        self.reais = float(input())
        valor = self.reais / conversor.dolar
        print(f'Valor em Dólares: US${valor:.2f}')


conversor = ConversorDolares()
conversor.converter_reais_para_dolares()
