class Calculadora():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.menu = '''Escolha uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa'''

    def iniciar(self):
        '''Menu principal do programa'''
        self.definir_argumentos()
        while True:
            print(self.menu)
            opcao = input()
            if opcao == '1':
                print(f'Soma de {self.x} por {self.y} é {self.somar(self.x, self.y)}\n')
            elif opcao == '2':
                print(f'Multiplicação de {self.x} por {self.y} é {self.multiplicar(self.x, self.y)}\n')
            elif opcao =='3':
                print(f'O maior número entre {self.x} e {self.y} é {self.indicar_maior_numero(self.x, self.y)}\n')
            elif opcao == '4':
                self.definir_argumentos()
            elif opcao == '5':
                print('Tenha um bom dia!')
                break
            else:
                print('Opção Inválida!')

    def definir_argumentos(self):
        '''Menu principal do programa.'''
        print('Digite os números: ')
        self.x = int(input())
        self.y = int(input())

    def somar(self, x, y):
        '''Soma de dois números.'''
        return x + y

    def multiplicar(self, x, y):
        '''Multiplicação de dois números.'''
        return x * y

    def indicar_maior_numero(self, x, y):
        '''Indica qual o maior entre os dois números.'''
        if x > y:
            return x
        elif x < y:
            return y
        else:
            return 'nenhum dos dois.'


calculadora = Calculadora()
calculadora.iniciar()