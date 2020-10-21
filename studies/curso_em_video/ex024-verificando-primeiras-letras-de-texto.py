# Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "São".
print()
cid = str(input('Digite o nome da cidade: ')).replace('-', ' ').split()
print(f'A cidade tem a palavra "São", isoladamente, no primeiro nome? {cid[0].upper() == "SÃO"}')
# Assim, ele divide o nome da cidade em itens de lista, para ver se o item 0 (o primeiro) é equivalente a "São" em
# maiúsculas. Caso a cidade tenha hífen, trocá-lo por um espaço ANTES de dar um split.

# Outra alternativa (até mais simples) exigindo que o nome tenha "São" e um espaço em seguida.
# Se for tudo junto, dará "False".

print()
cid2 = str(input('Digite o nome da cidade: ')).strip().replace('-', ' ')
print('A cidade começa com "São"?', cid2[:4].lower() == 'são ')
