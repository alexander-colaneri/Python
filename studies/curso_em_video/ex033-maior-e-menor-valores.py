# Nº 33 - Maior e Menor Valores
# Descrição: Faça um programa que leia três números e mostre qual é o maior e qual
# é o menor.

class MaiorMenorNumero():
    '''Entre três números indicados pelo usuário, exibe o maior e o menor.'''

    def __init__(self):
        self.maior = 0
        self.menor = 0
        self.lista_de_numeros = []

    def iniciar(self):
        '''Inicia o programa e exibe mensagens de boas vindas e despedida.'''
        print(f'{" INDICADOR DE MAIOR E MENOR NÚMEROS ":*^60}')
        self.recebe_numeros()
        self.classifica_numeros()
        self.exibe_numeros()
        print('\nTenha um bom dia!')

    def recebe_numeros(self):
        '''Recebe os 3 números que farão parte da análise.'''
        for c in range (1, 4):
            print(f'Digite o {c}º número:')
            while True:
                try:
                    self.lista_de_numeros.append(int(input()))
                    break
                except ValueError:
                    print('Digite números inteiros apenas, sem espaços.')
        return None

    def classifica_numeros(self):
        '''Separa o maior e o menor número da lista.'''
        self.maior = max(self.lista_de_numeros)
        self.menor = min(self.lista_de_numeros)
        return None

    def exibe_numeros(self):
        '''Exibe o maior e o menor número.'''
        print('=' * 50)
        print(f'O maior número é {self.maior} e o menor é {self.menor}.')

        
maiormenor = MaiorMenorNumero()
maiormenor.iniciar()
