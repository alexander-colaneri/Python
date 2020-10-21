# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
print()
numero = int(input('Digite um número entre 0 e 20: '))
while numero > 20:
    numero = int(input('Opção inválida, digite um número entre 0 e 20: '))
print(f'*** Por extenso, o número {numero} é "{extenso[numero]}". ***')
