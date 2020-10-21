print()
print('* Analisador de Nomes Completos *')
print()
nome = str(input('Digite o nome completo: ').strip())
# Já colocado a funcionalidade "strip" na variável, para limpar possíveis espaços antes e depois da digitação.
print()
print(f'1 - O nome em maiúsculas é {nome.upper()}.')
print(f'2 - O nome em minúsculas é {nome.lower()}.')
print(f'3 - O total de letras do nome (sem espaços) é {len(nome) - nome.count(" ")}.')
# Foi preciso usar aspas duplas para indicar o espaço, já que as aspas simples estavam sendo usadas para delimitar
# o texto do print.
print(f'4 - O primeiro nome é {nome.split()[0]} e tem um total de {len(nome.split()[0])} letras.')
# Para não precisar digitar códigos mais de uma vez como acima (nome.split()[0}), pode-se antes separar essa parte em
# uma nova variável.
primeironome = nome.split()[0]
print()
print(f'4b - O primeiro nome é {primeironome} e tem um total de {len(primeironome)} letras.')
print()
from emoji import emojize

print(emojize('Muito bem :smile:!', use_aliases=True))
