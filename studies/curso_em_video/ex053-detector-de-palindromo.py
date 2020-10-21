# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junção = ''.join(palavras)
inverso = junção[::-1] # Aqui, estamos pegando tudo o que foi juntado na frase, do início ao fim (por isso os :
# vazios indicando nenhuma posição específica, invertido (-1).
if inverso == junção:
    print(f'O inverso de {junção} é {inverso}')
    print('Temos um palíndromo!')
else:
    print(f'O inverso de {junção} é {inverso}.')
    print('Não temos um palíndromo...')
