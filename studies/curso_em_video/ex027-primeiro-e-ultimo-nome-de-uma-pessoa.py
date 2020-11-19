# Primeiro e Último Nome de Uma Pessoa.
# Descrição: Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.

class AnalisadorDeNomes():
    '''Indica separadamente qual é o primeiro e o último sobrenome no nome completo indicado.'''
    
    def _init__(self):
        self.nome_completo = ''
        self.nome = ''
        self.sobrenome = ''

    def iniciar(self):
        '''Início do programa.'''
        print(f'{" ANALISADOR DE NOMES COMPLETOS ":*^41}')
        self.receber_nome_completo()
        self.analisar_nome_completo()
        self.mostrar_resultados()
        print('\nTenha um bom dia!')

    def receber_nome_completo(self):
        '''Recebe o nome completo a ser analisado.'''
        print('Digite o nome completo:')
        self.nome_completo = input()
        return None

    def analisar_nome_completo(self):
        '''Separa o nome e o último sobrenome do nome completo indicado.'''
        nome_completo = self.nome_completo.title().strip().split()
        self.nome = nome_completo[0]
        self.sobrenome = nome_completo[-1]
        return None

    def mostrar_resultados(self):
        '''Exibe o nome e o último sobrenome.'''
        nome = self.nome
        sobrenome = self.sobrenome
        print(f'\nO primeiro nome é {nome} e o último sobrenome é {sobrenome}.')


analisador = AnalisadorDeNomes()
analisador.iniciar()
