# Descrição: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

def calcular_ano_bissexto():
    '''Indicar se o ano inserido é bissexto ou não.'''
    print(f'{" INDICADOR DE ANO BISSEXTO ":*^37}')
    print('Digite o ano a ser analisado ou "0" para o ano atual:')
    try:
        ano = int(input())
    except ValueError:
        print('Digite o número do ano. Não utilize letras ou espaços. O programa precisa ser reiniciado.')
    else:
        if ano == 0:
            ano = date.today().year
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print(f'O ano {ano} é bissexto!')
        else:
            print(f'O ano {ano} não é bissexto!')
    finally:
        print('Tenha um bom dia!')
        

calcular_ano_bissexto()
