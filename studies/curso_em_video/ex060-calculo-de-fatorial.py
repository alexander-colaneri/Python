# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

class CalculadoraFatorial():

    def __init__(self):
        self.numeros = []
        self.resultado = ''

    def iniciar(self):
        print('*** Cálculo de fatorial ***\nIndique o número: ')
        n = int(input())
        self.calcular_fatorial(n)
        self.exibir_resultado()

    def calcular_fatorial(self, n):
        '''Cálculo de fatorial em "n" vezes.'''
        fatorial = 1  # Deve começar em "1", pois se for "0" o resultado será "0".
        for i in range(n, 0, -1):
            fatorial *= i
            self.numeros.append(i)
        self.resultado = fatorial
        return self.resultado

    def exibir_resultado(self):
        '''Exibir os resultados calculados.'''
        print(str(self.numeros[0]) + '! = ', end='')
        for c in self.numeros:
            print(c, 'x ' if c != 1 else '= ', end='')
        print(self.resultado)
        

calculadora = CalculadoraFatorial()
calculadora.iniciar()
