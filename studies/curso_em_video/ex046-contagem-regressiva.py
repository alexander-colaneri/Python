# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep

class ContagemRegressiva():
    fogos = '*** FELIZ ANO NOVO!!!! ***'

    def __init__(self):
        pass

    def iniciar(self):
        '''Menu principal.'''
        print(f'{" CONTAGEM REGRESSIVA ":=^40}')
        self.contar_tempo()
        print(contagem.fogos)
        
    def contar_tempo(self):
        '''Contagem regressiva de 10 segundos'''
        for i in range(10, 0, -1):
            print(i)
            sleep(1)
            

contagem = ContagemRegressiva()
contagem.iniciar()
