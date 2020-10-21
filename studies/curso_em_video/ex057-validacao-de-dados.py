# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
print()
sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo not in 'MF':
    sexo = str(input('Opção inválida. Digite novamente: ')).upper()
print(f'Opção {sexo} registrada com sucesso!')
