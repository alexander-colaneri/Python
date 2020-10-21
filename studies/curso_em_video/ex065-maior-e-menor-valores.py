# Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.
print()

pergunta = 'S'
soma = contagem = media = 0
maior = menor = 0

# pergunta = str(input('Deseja continuar? ')).strip().upper()

while pergunta == 'S':
    n = int(input('Digite o número: '))
    soma = soma + n
    contagem += 1
    if contagem == 1:
        maior = menor = n  # Obs: No primeiro número inserido, não existe
        # número maior ou menor que ele. Logo, ele é, ao mesmo tempo,
        # o maior e o menor.
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    pergunta = str(input('Deseja continuar [S/N]? ')).strip().upper()
media = soma / contagem
print(f'A média final de todos os {contagem } valores é {media:.1f}')
print(f'O maior valor é {maior} e o menor é {menor}')
