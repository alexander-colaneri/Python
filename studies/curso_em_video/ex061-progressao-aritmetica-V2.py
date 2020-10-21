# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura "while".
print(f'{" Gerador de PA ":*^40}')
print()
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro  # Poderia ter continuado usando o nome "primeiro" durante
# o código, mas poderia casar confusão, por isso ele assume o nome "termo".
cont = 1  # Tentei começar o contador em 0, mas deu um total de 11 números,
# e não 10.
while cont <= 10:  # "Enquanto o contador for menor ou igual a 10,
    # ir fazendo o laço"
    print(termo, ' - ', end='')
    termo = termo + razao
    cont += 1  # "Soma mais um, sobe pra o 'while' e recomeça o processo."
print('Fim')
