# Nº 9 - Tabuada
# Descrição: Faça um programa que leia um número Inteiro qualquer e mostre na tela a
# sua tabuada.

class CalculadoraDeTabuada():
    '''Calcula um número indicado pelo usuário multiplicado de 1 a 10.'''
    def __init__(self):
        self.numero = 0
        self.resultados = []

    def iniciar(self):
        '''Função inicial do programa.'''
        print(f'{" CALCULADORA DE TABUADA ":*^40}')
        self.receber_numero()
        self.calcular_tabuada()
        self.mostrar_resultados()
        print('\nTenha um bom dia!')

    def receber_numero(self):
        '''Recebe número indicado pelo usuário para cálculo de tabuada.'''
        print('Indique o número que deseja calcular a tabuada:')
        while True:
            try:
                self.numero = int(input())
                break
            except ValueError:
                print('Digite um número inteiro, sem espaços ou letras.')

    def calcular_tabuada(self):
        '''Calcula a tabuada de um número indicado pelo usuário.'''
        for i in range(1, 11):
            self.resultados.append(self.numero * i)  # Resultados armazenados em uma lista.
        return None

    def mostrar_resultados(self):
        '''Exibe os cálculos e resultados.'''
        print('-' * 20)
        for i in range(1, 11):
            print(f'{self.numero} X {i : >2} = {self.resultados[i - 1]}')
        print('-' * 20)
        return None


tabuada = CalculadoraDeTabuada()
tabuada.iniciar()
