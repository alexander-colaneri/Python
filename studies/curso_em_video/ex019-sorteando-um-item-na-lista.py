print()
print('*Sorteio de alunos*')
print()
# Obs: Estou especificando que é um string (str), mas por questão de exercício, não é necessário.
import random
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
# * Conceito novo: LISTAS. Para razer uma lista, colocamos os itens ENTRE COLCHETES [] *
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}!')
print()
print('Usando a segunda forma, importando a funcionalidade por antecedência:')
print()
from random import choice
escolhido2 = choice(lista)
print(f'O escolhido foi {escolhido2}!')
