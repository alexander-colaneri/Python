# Exercicio 15 - Aluguel de Carros
# Descrição: Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

class CalculadoraDeAluguel():
    '''Calcula o valor de acordo com quilometragem percorrida e dias de aluguel.'''
    valor_por_dia = 60
    valor_por_km = 0.15

    def __init__(self):
        self.km = 0
        self.dias = 0
        self.valor_total_km = 0
        self.valor_total_dias = 0
        self.valor_total = 0

    def iniciar(self):
        '''Inicia o programa e mostra mensagens de boas vindas e despedida.'''
        print(f'{" CALCULADORA DE ALUGUEL DE CARRO - BEM-VINDOS! ":*^59}')
        self.receber_dados()
        self.calcular_valores()
        self.exibir_resultados()
        print(f'\nTenha um bom dia!')

    def receber_dados(self):
        '''Recebe a quantidade de dias e quilometragem.'''
        print('Digite a quilometragem percorrida:')
        while True:
            try:
                self.km = float(input())
                break
            except ValueError:
                print('Digite apenas números, sem espaços.')

        print('Digite a quantidade de dias de aluguel do veículo:')
        while True:
            try:
                self.dias = int(input())
                break
            except ValueError:
                print('Digite apenas números inteiros, sem espaços.')

    def calcular_valores(self):
        '''Calcula os valores de acordo com o total percorrido e dias de aluguel.'''
        self.valor_total_km = self.km * calculadora.valor_por_km
        self.valor_total_dias = self.dias * calculadora.valor_por_dia
        self.valor_total = self.valor_total_km + self.valor_total_dias
        return None

    def exibir_resultados(self):
        '''Exibe de forma organizada os valores calculados.'''
        print('=' * 50)
        print(f'O total relacionado à quilometragem é R${self.valor_total_km:.2f}')
        print(f'O total relacionado a dias de aluguel é R${self.valor_total_dias:.2f}')
        print(f'O total a ser pago é R${self.valor_total:.2f}')
        print('=' * 50)


calculadora = CalculadoraDeAluguel()
calculadora.iniciar()
