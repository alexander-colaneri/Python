# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
print()
print('*' * 5, 'Calculadora de Alistamento Miliar', '*' * 5)
print()
print('''Por favor, escolha a opção que indica seu sexo:
[ 1 ] para MASCULINO
[ 2 ] para FEMININO''')
sexo = int(input('Digite a opção escolhida: '))
print()
if sexo == 2:
    print('Obrigado pelo interesse no serviço militar. No seu caso, não é obrigatório. Obrigado!')
elif sexo == 1:
    from datetime import date
    anonascimento = int(input('Digite o ano do seu nascimento: '))
    print()
    anoatual = date.today().year
    idade = anoatual - anonascimento
    if idade < 18:
        saldo = 18 - idade
        ano = anoatual + saldo
        # Obs: lembre-se que tudo o que está identado corresponde a um bloco isolado. Logo, a palavra "saldo" vai ser
        # também utilizada na identação seguinte, mas ficará restrito ao bloco onde foi identado apenas.
        print(f'Você está com {idade} anos e ainda faltam {saldo} anos para o alistamento, que será em {ano}!')
    elif idade == 18:
        print(f'Você está com {idade} anos. Chegou a hora de se alistar!')
    else:
        saldo = idade - 18
        ano = anoatual - saldo
        print(f'Você está com {idade} anos. Já ultrapassou {saldo} anos do prazo para alistamento, que foi em {ano}!')
else:
    print('Opção inválida, digite novamente.')
