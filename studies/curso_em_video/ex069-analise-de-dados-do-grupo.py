# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

contador_18 = 0
contador_h = 0
contador_m_20 = 0
while True:
    print()
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida, '
                         'digite novamente [M/F]: ')).strip().upper()
    if idade >= 18:
        contador_18 += 1
    if sexo == 'M':
        contador_h += 1
    if sexo == 'F' and idade < 20:
        contador_m_20 += 1
    print()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida, '
                              'digite novamente [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print()
print(f'{" RESULTADOS ":*^20}')
print(f'* Pessoas com mais de 18 anos: {contador_18}\n* Homens: {contador_h}\n'
      f'* Mulheres com menos de 20 anos: {contador_m_20}')
print()
print('*** Tenha um bom dia! ***')
