# Somando Dois Números
# Descrição: Crie um programa que leia dois números e mostre a soma entre eles.

class SomadorDeNumeros():
    '''Calculadora de soma de dois números.'''

    def __init__(self):
        self.primeiro_numero = 0
        self.segundo_numero = 0
        self.soma = 0

    def iniciar(self):
        '''Começa o programa.'''
        print(f'{" SOMADOR DE NÚMEROS ":=^30}')
        self.receber_numeros()
        self.somar_numeros()
        self.mostrar_resultado()
        print('\nTenha um bom dia!')

    def receber_numeros(self):
        '''Recebe os números a serem calculados.'''
        print('Digite o primeiro número:')
        while True:
            try:
                self.primeiro_numero = int(input())
                break
            except ValueError:
                print('Digite apenas números inteiros, sem espaços.')
        print('Digite o segundo número:')
        while True:
            try:
                self.segundo_numero = int(input())
                break
            except ValueError:
                print('Digite apenas números inteiros, sem espaços.')
        return None

    def somar_numeros(self):
        '''Soma os dois números indicados pelo usuário.'''
        self.soma = self.primeiro_numero + self.segundo_numero
        return None

    def mostrar_resultado(self):
        '''Exibe o resultado da somas.'''
        primeiro = self.primeiro_numero
        segundo = self.segundo_numero
        soma = self.soma
        print(f'\nA soma de {primeiro} com {segundo} é {soma}.')

somador = SomadorDeNumeros()
somador.iniciar()
