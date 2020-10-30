# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

class JoKenPo():
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    menu = '''\nEscolha uma opção:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA\n'''

    def __init__(self):
        self.opcao_jogador = '' 
        self.opcao_cpu = ''

    def iniciar(self):
        '''Menu principal'''
        print(f'{" JO KEN PO ":*^40}')
        print(jokenpo.menu)
        if not self.receber_entrada_jogador():
            print('Opção Inválida. Comece novamente!')
        else:
            self.receber_entrada_cpu()
            self.fazer_contagem_regressiva()
            self.analisar_resultados()

    def receber_entrada_jogador(self):
        '''Recebimento da opção do jogador.'''
        jogador = input()
        if jogador == '1':
            self.opcao_jogador = jokenpo.opcoes[0]
            return self.opcao_jogador
        elif jogador == '2':
            self.opcao_jogador = jokenpo.opcoes[1]
            return self.opcao_jogador
        elif jogador == '3':
            self.opcao_jogador = jokenpo.opcoes[2]
            return self.opcao_jogador
        else:
            return False
        
    def receber_entrada_cpu(self):
        '''Recebimento da opção do CPU.'''
        self.opcao_cpu = choice(jokenpo.opcoes)
        return self.opcao_cpu

    def analisar_resultados(self):
        '''Comparação entre resultados e indicação do vencedor.'''
        jogador = self.opcao_jogador
        cpu = self.opcao_cpu
        if jogador == cpu:
            print(f'Você escolheu {jogador} e o computador {cpu}.\n***** Empate! *****\n')
        elif (jogador == 'PEDRA' and cpu == 'TESOURA') or (jogador == 'PAPEL' and cpu == 'PEDRA') or (jogador == 'TESOURA'  and cpu == 'PAPEL'):
            print(f'Você escolheu {jogador} e o computador {cpu}.\n***** Você venceu! *****\n')
        else:
            print(f'Você escolheu {jogador} e o computador {cpu}.\n***** Você perdeu! *****\n')

    def fazer_contagem_regressiva(self):
        '''Mostra timer para criar expectativa sobre resultado.'''
        sleep(0.5)
        print('\n*JO*')
        sleep(0.5)
        print('*KEM*')
        sleep(0.5)
        print('*PÔ!!!*\n')

jokenpo = JoKenPo()
jokenpo.iniciar()
