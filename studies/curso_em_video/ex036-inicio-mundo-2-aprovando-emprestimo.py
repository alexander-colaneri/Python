'''Aprovando Empréstimo
Descrição: Escreva um programa para aprovar o empréstimo bancário para a compra de
uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.'''

class AnalisadorDeEmprestimo():
    '''Analisa se, de acordo com o salário, empréstimo para compra de casa é 
    liberado. Prestação mensal não pode ultrapassar 30% do salário.'''
    porcentagem_de_aprovacao = 0.3

    def __init__(self):
        self.valor_casa = 0
        self.salario = 0
        self.meses_para_pagamento = 0
        self.valor_parcela = 0

    def iniciar(self):
        print(f'{" ANALISADOR DE EMPRÉSTIMO PARA COMPRA DE CASA ":*^60}')
        self.receber_informacoes()
        self.calcular_prestacao()
        self.analisar_viabilidade()
        self.indicar_resultado()

    def receber_informacoes(self):
        '''Recebe valor da casa, salário do comprador e anos para pagamento.'''
        print('Digite o valor da casa:')
        while True:
            try:
                self.valor_casa = float(input())
            except ValueError:
                print('Digite apenas números, sem espaços.')
            else:
                break
        print('Digite o valor do seu rendimento mensal:')
        while True:
            try:
                self.salario = float(input())
            except:
                print('Digite apens números, sem espaços.')
            else:
                break
        print('Digite a quantidade de anos para pagamento.')
        while True:
            try:
                anos_para_pagamento = int(input())
            except:
                print('Digite apenas números, sem espaços.')
            else:
                self.meses_para_pagamento = anos_para_pagamento * 12
                break
        return None

    def calcular_prestacao(self):
        '''Calcula vaor da casa pela quantidade de meses de pagamento.'''
        self.valor_parcela = self.valor_casa / self.meses_para_pagamento
        return None

    def analisar_viabilidade(self):
        '''Liberar o empréstimo caso valor da mensalidade não ultrapasse 30% do valor do salário.'''
        if self.valor_parcela <= self.salario * analisador.porcentagem_de_aprovacao:
            return True
        else:
            return False
    
    def indicar_resultado(self):
        if self.analisar_viabilidade():
            print(f'\nO valor da prestação é de {self.meses_para_pagamento} vezes de R${self.valor_parcela:.2f}')
            print(f'O valor de 30% de seu salário é R${self.salario * analisador.porcentagem_de_aprovacao:.2f}')
            print(f'Empréstimo APROVADO!')
        else:
            print(f'\nO valor da prestação é de {self.meses_para_pagamento} vezes de R${self.valor_parcela:.2f}')
            print(f'O valor de 30% de seu salário é R${self.salario * analisador.porcentagem_de_aprovacao:.2f}')
            print(f'Empréstimo REPROVADO!')


analisador = AnalisadorDeEmprestimo()
analisador.iniciar()
