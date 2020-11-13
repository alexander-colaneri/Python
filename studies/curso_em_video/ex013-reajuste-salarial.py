# Exercício 13: Reajuste Salarial
# Descrição: Faça um programa que leia o salário de um funcionário e mostre seu
# novo salário, com 15% de aumento.

class ReajustadorDeSalario():
    porcentagem_de_reajuste = 0.15

    def __init(self):
        self.salario_atual = 0
        self.aumento = 0
        self.novo_salario = 0

    def iniciar(self):
        '''Área inicial do programa.'''
        print(f'{" CALCULADORA DE AUMENTO SALARIAL ":*^43}')
        self.receber_valor_salario()
        self.reajustar_salario()
        self.exibir_novo_salario()

    def receber_valor_salario(self):
        '''Recebe o valor do salário atual.'''
        print('Digite o valor do salário atual:')
        while True:
            try:
                salario_atual = float(input())
                break
            except ValueError:
                print('\nDigite o valor em números, sem espaços.')
        self.salario_atual = salario_atual
        return None

    def reajustar_salario(self):
        '''Calcula e reajusta salário atual com 15% de aumento.'''
        salario = self.salario_atual
        reajuste = reajustador.porcentagem_de_reajuste
        aumento = salario * reajuste
        self.novo_salario = salario + aumento
        self.aumento = aumento
        return None

    def exibir_novo_salario(self):
        '''Recebe o valor reajustado e mostra o resultado.'''
        print(f'\nO salário de R${self.salario_atual:.2f} será reajustado em R${self.aumento:.2f}.')
        print(f'Novo salário = R${self.novo_salario:.2f}')
        print('\nTenha um bom dia!')

reajustador = ReajustadorDeSalario()
reajustador.iniciar()
