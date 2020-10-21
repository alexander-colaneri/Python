# Ano bissexto
# Digite um ano e veja se é bissexto.
print()
ano = int(input('Digite o ano ou 0 para o ano atual: '))
# Um ano bissexto ocorre a cada 4 anos, porém há mais regras: se o ano for múltiplo de 100 e não múltiplo de 400,
# ele não é bissexto. Ou seja: SE ano % 4 for 0(zero) E ano % 100 diferente de 0(zero) o ano será bissexto.
# CASO CONTRÁRIO ano % 400 deve ser 0 para que o ano seja bissexto.
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
