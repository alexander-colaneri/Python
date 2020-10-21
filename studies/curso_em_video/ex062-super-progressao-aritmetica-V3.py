# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerrará quando ele disser que quer mostrar 0
# termos.
print()
print(f'{" Gerador de PA v3.0 ":*^40}')
print()
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0  # Total corresponde à soma da quantidade de termos que foi pedida
# no total, ao final do programa.
mais = 10  # No primeiro momento, mostramos os 10 primeiros termos, por isso
# começa com 10. Lá embaixo, ao colocar um
# número novo, ele retoma o início do laço e faz toda a passagem novamente.
while mais != 0:
    total = total + mais
    while cont <= total:  # Percebe que o contador NUNCA será menor ou igual
        # a 1, pois ele começa com 1 e depois é necessariamente de 2 para
        # cima? Isso faz com que este laço sempre avance.
        print(termo, ' - ', end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos.')
