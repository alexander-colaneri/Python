# Descrição: Desenvolva um programa que pergunte a distância de uma viagem 
# em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 
# até 200Km e R$0,45 para viagens mais longas.

class CalculadoraCustoViagem():
    '''Calcula valor da passagem de acordo com quilometragem indicada.'''
    valor_km_200 = 0.5
    valor_km_alem_200 = 0.45
    
    def __init__(self):
        self.km = 0
        self.valor_total = 0

    def iniciar(self):
        '''Inicia o programa.'''
        print(f'{" CALCULADORA DE VALOR DE PASSAGEM ":*^44}')
        self.receber_distancia()
        self.calcular_valor()
        self.indicar_valor()

    def receber_distancia(self):
        '''Recebe a quilometragem da distância até o destino da viagem.'''
        print('Indique a quilometragem até o destino:')
        while True:
            try:
                km = float(input())
            except ValueError:
                print('Indique a distância apenas por números, sem espaços.')
            else:
                self.km = km
                break
        return self.km
        
    def calcular_valor(self):
        '''Calcula valor total por relação entre distância do destino e 
        valor fixo por quilômetro rodado.'''
        if self.km <= 200:
            self.valor_total = self.km * calculadora.valor_km_200
            return self.valor_total
        else:
            self.valor_total = self.km * calculadora.valor_km_alem_200
            return self.valor_total
    
    def indicar_valor(self):
        '''Indica o cálculo final do valor da passagem.'''
        print(f'\nO valor da passagem a ser pago por {self.km}km de distância é'\
            f' de R${self.valor_total:.2f}.\n***** Tenha um bom dia! *****')


calculadora = CalculadoraCustoViagem()
calculadora.iniciar()
