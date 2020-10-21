# Crie um programa que simule o funcionamento de um caixa eletrônico. No
# início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
print()
print('=' * 30)
print(f'{"BANCO BANCO":^30}')
print('=' * 30)
total_a_sacar = int(input('Digite o valor a sacar: R$'))
# cont50 = cont10 = cont1 = soma_cedulas = 0
cedula = 50
total_de_cedulas = 0
while True:
    # Abaixo, é montado o algoritmo que, depois, vai receber as alternativas
    # de cédulas. O raciocínio escolhido foi entender que o valor pedido no
    # saque é um montante total, que vai sendo descontado as cédulas nos
    # valores disponíveis (50,20,10,1).
    if total_a_sacar >= cedula:
        total_a_sacar -= cedula
        total_de_cedulas += 1
    else:
        if total_de_cedulas > 0:  # Essa linha foi colocada para que quando
            # forem "0" cédulas do valor, não seja
            # mostrado o print  da quantidade de cédulas.
            print(f'Total de {total_de_cedulas} cédulas de R${cedula}')
            # Para cada vez que a condição do laço é completamente
            # satisfeita, termina-se com o print do total. Isso vai se
            # repetir pra cada iteração com os valores diferentes de cédula
            # (50,20,10,1).

        # Abaixo, as alternativas para cada valor de cédula. Imagine o
        # programa pegando o número da cédula, passando pelo algoritmo lá em
        # cima, depois que a condição foi atingida, a variável "cédula"
        # assume o número seguinte.
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_de_cedulas = 0  # Muito importante! O contador de cédulas
        # precisa ser zerado ao final de cada iteração!
        if total_a_sacar == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO BANCO! Tenha um bom dia!')
