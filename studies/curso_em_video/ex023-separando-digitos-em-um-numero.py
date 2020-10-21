print()
print('* Contagem de unidades, dezenas, centenas e milhares de um número de 0 a 9999 *')
print()
# n = str(input('Digite um número: '))
# print(f'O milhar é {n[0]}\n'
  #    f'A centena é {n[1]}.\n'
   #   f'A dezena é {n[2]}.\n'
    #  f'A unidade é {n[3]}.')
    # A forma acima é a que primeiramente pensamos, mas dará erro ao deixar alguma casa vazia (por exemplo, a casa
    # do milhar vazia em 231), além de permitir inserir letras. O ideal é utilizar o raciocínio matemático.
n = int(input('Digite um número entre 0 e 9999: '))
print()
print(f'A unidade é {n // 1 % 10}')
print(f'A dezena é {n // 10 % 10}')
print(f'A centena é {n // 100 % 10}')
print(f'O milhar é {n // 1000 % 10}')
# Entendendo o raciocínio acima: o número deve ter uma divisão inteira (por isso os dois //) por 1, 10, 100 ou 1000,
# dependendo da casa decimal que está fazendo referência. Depois disso, deve se indicar com o % qual é o resto
# da divisão. Por exemplo, 192/10 dá 19, e sobra 2. Logo, ao indicarmos com a % que queremos saber o resultado da
# do resto da divisão 192 por 10, o print indicará o número 2, ficando assim: 192 % 10 resulta em 2 (pois sobrou 2
# dessa divisão de 192 por 10).
