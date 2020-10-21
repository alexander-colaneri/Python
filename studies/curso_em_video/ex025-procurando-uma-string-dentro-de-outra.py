# Crie um programa que leia o nome de uma pessoa e diga se tem "Silva" no nome dela.
print()
nome = str(input('Digite seu nome: ')).strip().lower().split()
print(f'Seu nome tem "Silva"? {"silva" in nome}')
