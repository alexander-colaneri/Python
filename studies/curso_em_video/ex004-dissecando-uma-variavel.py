# Exercício 4:
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

def receber_caracteres():
    '''Recebe números ou strings para serem analisados'''
    print(f'{" ANALISADOR DE CARACTERES ":=^40}')
    print('Digite algo (palavra ou números) para ser analisado:')
    a = input()
    return a

def analisar_caracteres():
    '''Analisa os dados recebidos e avalia diversas características.'''
    a = receber_caracteres()
    print('O tipo primitivo desse valor é', type(a))
    print('É um número?', a.isnumeric())
    print('É um texto?', a.isalpha())
    print('É em somente em maiúsculas?', a.isupper())
    print('É somente em minúsculas?', a.islower())
    print('É capitalizado?', a.istitle())
    print('É alfanumérico?', a.isalnum())
    print('Está somente com espaço?', a.isspace())
    print('É um dígito?', a.isdigit())
    print('É sem caracteres especiais? ',a.isidentifier())
    print('É imprimível?', a.isprintable())
    print('\nIsso é tudo, tenha um bom dia!')


analisar_caracteres()
