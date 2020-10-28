from random import shuffle

def ordenar_alunos():
    ''' Ordem de apresentação de alunos.'''
    print('Ordem de apresentação de alunos:\n')
    alunos = [input('Estudante: ') for a in range(4)]
    shuffle(alunos)
    ordem = ', '.join(alunos)
    print('\nA ordem de apresentação é:', ordem)

ordenar_alunos()


""" 
Versão anterior:

print()
print('* Seleção da ordem de apresentação de alunos em aula *')
print()
import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}.')
from random import shuffle

shuffle(lista)
print(lista) """
