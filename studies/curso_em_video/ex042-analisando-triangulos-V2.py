# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

class ClassificadorDeTriangulos():
    '''Verifica se com os valores dados se forma um triângulo. Caso sim, indica o tipo.'''

    def __init__(self):
        self.valores_lados = []

    def iniciar(self):
        '''Área principal.'''
        print(f'{"CLASSIFICADOR DE TRIÂNGULOS":*^40}\n')
        self.receber_valores()
        if self.analisar_valores():
            print('\nForma triângulo!')
            self.indicar_tipo()
        else:
            print('\nNão forma triângulo!')
        print('\nTenha um bom dia!')

    def receber_valores(self):
        '''Recebe os valores dos 3 lados do triângulo.'''
        for i in range(1, 4):
            print(f'Digite o valor do lado {i}:')
            self.valores_lados.append(int(input()))
            return None

    def analisar_valores(self):
        '''Analisa se é possível formar um triângulo com os valores dados.'''
        a, b, c = self.valores_lados[0], self.valores_lados[1], self.valores_lados[2]
        if a < b + c and b < c + a and c < a + b:
            return True

    def indicar_tipo(self):
        '''Indica o tipo de triângulo.'''
        a, b, c = self.valores_lados[0], self.valores_lados[1], self.valores_lados[2]
        if a != b != c != a:
            print('Tipo: escaleno')
        elif a == b == c:
            print('Tipo: equilátero')
        else:
            print('Tipo: isósceles')


classificador = ClassificadorDeTriangulos()
classificador.iniciar()
