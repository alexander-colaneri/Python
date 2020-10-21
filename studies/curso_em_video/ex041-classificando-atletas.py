# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
print()
print('*' * 5, 'Classificador de Atletas', '*' * 5)
print()
ano = int(input('Digite o ano de nascimento do atleta: '))
from datetime import date
anoatual = date.today().year
idade = anoatual - ano
print()
if idade <= 9:
    print('O atleta está na categoria MIRIM.')
# elif 10 <= idade <= 14: Normalmente isso seria o raciocínio, mas não tem necessidade de repetir a condição
# colocada anteriormente.
elif idade <= 14:
    print('O atleta está na categoria INFANTIL.')
elif idade <= 19:
    print('O atleta está na categoria JUNIOR.')
elif idade <= 25:
    print('O atleta está na categoria SÊNIOR.')
elif idade > 25:
    print('O atleta está na categoria MASTER.')
