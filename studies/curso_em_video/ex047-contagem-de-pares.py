# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print()
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

# Importante: para evitar forçar o processador e economizar memória, importante conseguir o melhor resultado com menos
# iterações. Observe o mesmo abaixo:

print()
# for c in range(1, 51): nesta situação, estamos pedindo 2 trabalhos do processador: que seria mostrar
# todos os números para, em seguida, esconder os que não vai usar, com o "if" logo abaixo. Para verificar,
# colocamos um "print('.', end='') e vemos que cada operação feita pelo computador exibiu um ponto.
for c in range(1, 51):
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

# Sendo assim, o melhor é sempre que possível "poupar" o processador com menos cálculos. Neste caso, o melhor é
# já no laço de repetição mandar "limpar" os números que não precisam ser puxados. Observe que, agora, ficou apenas
# um ponto, indicando uma utilização apenas de pedido ao processador.
print()
for c in range(2, 51, 2):
    print('.', end='')
    print(c, end=' ')
print('FIM')
# Concluindo, a melhor forma deste exercício poupando mais o processador é:
print()
for c in range(2, 51, 2):
    print(c, end=' ')
print('FIM')

