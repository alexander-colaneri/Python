# Números Primos
# Descrição: Faça um programa que leia um número inteiro e diga se ele é ou não
# um número primo.

class AnalisadorNumeroPrimo():
    def __init__(self):
        self.numero = ''
        self.validador_se_primo = False
        self.quantas_vezes_divisivel = 0

    def iniciar(self):
        '''Parte inicial do programa.'''
        print(f'{" ANALISADOR DE NÚMEROS PRIMOS ":=^40}')
        self.receber_numero()
        self.analisar_numero()
        self.exibir_resultado()
        print('\nTenha um bom dia!')

    def receber_numero(self):
        '''Recebe o número para ser analisado se é ou não primo.'''
        print('Digite um número inteiro a ser analisado:')
        while True:
            try:
                self.numero = int(input())
                break
            except ValueError:
                print('Digite um número inteiro, sem espaços ou letras.')
        return None
    
    def analisar_numero(self):
        '''Analisa se o número é primo e exibe sequência colorizada indicando os números divisíveis.'''
        contador = 0
        numero = self.numero
        for c in range(1, numero + 1):
            if numero % c == 0:
                print('\033[33m', end=' ')
                contador += 1
            else:
                print('\033[31m', end=' ')
            print(f'{c}', end=' ')
        if contador == 2:
            self.validador_se_primo = True
        self.quantas_vezes_divisivel = contador

    def exibir_resultado(self):
        '''Mostra os resultados finais.'''
        validador = self.validador_se_primo
        numero = self.numero
        vezes = self.quantas_vezes_divisivel
        print(f'\n\033[37mO número {numero} é divisível {vezes} vezes.')
        if validador:
            print(f'\nÉ PRIMO!')
        else:
            print(f'\nNÃO É PRIMO!')


analisador = AnalisadorNumeroPrimo()
analisador.iniciar()
