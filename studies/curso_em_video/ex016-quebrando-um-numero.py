# Quebrando um Número:
# Descrição: Crie um programa que leia um número Real qualquer pelo teclado e mostre
# na tela a sua porção inteira.

def separar_inteiro_de_real():
    '''Recebe um número flutuante ou inteiro, e mostra a parte inteira.'''
    print(f'{" SEPARADOR DE PARTE INTEIRA DE NÚMERO REAL ":*^53}')
    print('Digite um número inteiro ou inteiro com decimais:')
    try:
        n = float(input())
    except ValueError:
        print("Somente números são aceitos. Tente novamente.")
    else:
        print(f'\nO número digitado foi {n} e {int(n)} é a parte inteira do número.\n')
    finally:
        print('Tenha um bom dia!')


separar_inteiro_de_real()
