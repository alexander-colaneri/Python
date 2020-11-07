# Descrição: Escreva um programa que converta uma temperatura digitando em 
# graus Celsius e converta para graus Fahrenheit.

class ConversorTemperatura():
    '''Converte temperatura de graus Celsius para Fahrenheit.'''
    def __init__(self):
        self.celsius = 0
        self.fahrenheit = 0

    def iniciar(self):
        '''Início do programa.'''
        print('*** Conversor de temperatura - Celsius para Fahrenheit ***\n')
        self.receber_graus_celsius()
        self.converter_temperatura()
        self.exibir_resultado()

    def receber_graus_celsius(self):
        '''Recebe o valor digitado pelo usuário.'''
        print('Digite a temperatura em graus Celsius:')
        self.celsius = float(input())
        return self.celsius

    def converter_temperatura(self):
        '''Converte o valor digitado de graus Celsius para graus Fahrenheit.'''
        self.fahrenheit = self.celsius * 9 / 5 + 32
        return self.fahrenheit

    def exibir_resultado(self):
        '''Exibe o valor convertido em graus Fahrenheit.'''
        print(f'{self.celsius}ºC = {self.fahrenheit:.1f}ºF')


conversor = ConversorTemperatura()
conversor.iniciar()
