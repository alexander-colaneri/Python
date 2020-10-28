# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

class GerenciadorPagamentos():
    '''Calculadora de pagamentos, de acordo com a forma de pagamento.'''
    desconto_vista = 0.1
    desconto_cartao = 0.05
    juros_parcelado = 0.2

    def __init__(self):
        self.menu = '''\nAs opções de pagamento são:
    [ 0 ] - À vista em dinheiro/cheque.
    [ 1 ] - À vista no cartão.
    [ 2 ] - Em 2x no cartão.
    [ 3 ] - Em 3x ou mais no cartão.\n
Digite a opção selecionada:'''
        self.valor = 0
        self.desconto_10 = 0
        self.desconto_5 = 0
        self.parcelas = 0

    def iniciar(self):
        '''Menu principal.'''
        print(f'{" SUPER LOJA ":*^40}')
        self.digitar_valor()
        print(self.menu)

        opcao = input()
        if opcao == '0':
            self.pagar_a_vista()
        elif opcao == '1':
            self.pagar_cartao()
        elif opcao == '2':
            self.pagar_2x()
        elif opcao == '3':
            self.pagar_3x_mais()
        else:
            print('Opção inválida!')

    def digitar_valor(self):
        '''Valor do produto a ser comprado.'''
        print('\nDigite o valor do produto:')
        self.valor = float(input())

    def pagar_a_vista(self):
        '''Calcula valor para pagamento à vista, com 10% de desconto.'''
        desconto = gerenciador.desconto_vista
        self.desconto_10 = self.valor * desconto
        total = self.valor - self.desconto_10
        print(f'\nDesconto de 10%: R${self.desconto_10:.2f}\nTOTAL: R${total:.2f}')
    
    def pagar_cartao(self):
        '''Calcula valor para pagamento à vista, com 5% de desconto.'''
        desconto = gerenciador.desconto_cartao
        self.desconto_5 = self.valor * desconto
        total = self.valor - self.desconto_5
        print(f'\nDesconto de 5%: R${self.desconto_5:.2f}\nTOTAL: R${total:.2f}')

    def pagar_2x(self):
        '''Calcula valor para pagamento em 2 parcelas iguais, sem desconto.'''
        parcela = self.valor / 2
        print(f'\nDuas parcelas iguais de R${parcela:.2f}')

    def pagar_3x_mais(self):
        '''Calcula valor para 3 ou mais parcelas, com 20% de juros no preço.'''
        print('Digite o total de parcelas: ')
        self.parcelas = int(input())
        juros = gerenciador.juros_parcelado
        parcela = (self.valor + (self.valor * juros)) / self.parcelas
        print(f'\n{self.parcelas} parcelas de R${parcela:.2f}\nTOTAL: R${parcela * self.parcelas:.2f}')


gerenciador = GerenciadorPagamentos()
gerenciador.iniciar()