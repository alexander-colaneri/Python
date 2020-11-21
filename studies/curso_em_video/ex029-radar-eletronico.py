# Descrição: Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai
# custar R$7,00 por cada Km acima do limite.

from random import randint

class RadarEletronico():
    '''Verifica velocidade e calcula multa se ultrapassado limite.'''
    limite = 80
    multa_por_km = 7

    def __init__(self):
        self.velocidade = 0
        self.multado = False
        
    def iniciar(self):
        '''Inicia o programa.'''
        print(f'{" RADAR ELETRÔNICO DE VELOCIDADE ":=^44}')
        self.indicar_velocidade()
        self.verificar_infracao()
        self.calcular_multa()
        self.mostrar_resultado()
        print('\nTenha um bom dia!')
    
    def indicar_velocidade(self):
        '''Randomicamente, indica a velocidade do veículo.'''
        self.velocidade = randint(0, 250)
        return None
    
    def verificar_infracao(self):
        '''Verifica se o motorista passou acima dos 80km/h.'''
        velocidade = self.velocidade
        if velocidade > radar.limite:
            self.multado = True
        return None

    def calcular_multa(self):
        '''Calcula R$7,00 por km acima do limite de velocidade.'''
        velocidade = self.velocidade
        if self.multado:
            calculo = (velocidade - radar.limite) * radar.multa_por_km
            return calculo
        else:
            return None

    def mostrar_resultado(self):
        '''Exibe se motorista foi multado ou não, e caso positivo, o valor da multa.'''
        velocidade = self.velocidade
        calculo = self.calcular_multa()
        if calculo:
            print(f'\n\033[1;33mO motorista passou a {velocidade}km/h ({velocidade - 80}km/h excedidos) e a multa é de R${calculo:.2f}.\033[m')
        else:
            print(f'\n\033[1;32mO motorista passou a {velocidade}km/h e não foi multado.\033[m')

radar = RadarEletronico()
radar.iniciar()
