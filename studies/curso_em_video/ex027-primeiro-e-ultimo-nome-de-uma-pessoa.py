# * Primeiro e último nome de uma pessoa *
# Enunciado: Faça um programa que leia o nome de uma pessoa, mostrando o primeiro e o segundo nomes separadamente.
print()
n = str(input('Digite seu nome completo: ')).strip().title().split()
print('Seja bem vindo!')
print(f'Seu primeiro nome é {n[0]} e seu último sobrenome é {n[-1]}.')
# Quando fazemos referência aos itens da lista do primeiro ao último, usamos números positivos, e do último ao
# primeiro, números negativos. Por isso o [-1] faz referência ao último item da lista.
