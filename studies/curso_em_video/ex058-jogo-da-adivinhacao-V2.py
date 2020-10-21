# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
print()
print(f'{" JOGO DA ADIVINHAÇÃO V2 ":*^40}')
print()
'''print('Pense em um número de 0 a 10, ')
from random import randint
somatenta = 0
n = int(input('Digite um número: '))
comp = randint(0, 10)
while n != comp:
    if n > comp:
        n = int(input(f'\033[:31mMenos\033[:m, tente novamente: '))
    elif n < comp:
        n = int(input(f'\033[:32mMais\033[m, tente novamente: '))
    somatenta += 1
if n == comp:
    print(f'Acertou! O número é {comp} e você precisou de {somatenta + 1} tentativas!')'''

# Acima, a forma que fiz. Não está errada, mas abaixo está a que o professor indicou, com a novidade do raciocínio
# "True" e "False".
from random import randint
somatenta = 0
comp = randint(0, 10)
acertou = False # Novidade! Aqui, estamos indicando que quando o objetivo for atingido, no caso quando o número for
# acertado, encerrar o laço e consequentemente, o jogo. A condição do laço será satisfeita.

while not acertou:  # Ou seja, enquanto a condição não é satisfeita, alcançando o estado de False e terminando o jogo...
    n = int(input('Digite o número: '))
    somatenta += 1
    if n == comp:
        acertou = True  # Quando os números são iguais, a condição de "acertou = False" criada lá em cima é ativada
        # (acertou = True), o "while not" foi desativado, a leitura vai para o print final e termina o jogo.
    else:
        if n > comp:
            print('\033[:31mMenos\033[m... Tente de novo!')
            print()
        elif n < comp:
            print('\033[:32mMais\033[m... Tente de novo!')
            print()
print()
print(f'\033[4:36:43mACERTOU!\033[m O número era {comp} e você precisou de {somatenta} tentativa(s)!')