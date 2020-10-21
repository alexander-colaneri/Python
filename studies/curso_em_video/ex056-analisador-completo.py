print()
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
médiaidade = 0
idadevelho = 0
nomevelho = ''
mulheres20 = 0
for contador in range(1, 5):
    print(f'-----{contador}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade  # A cada inserção de idade no questionário, ele vai somar
    if contador == 1 and sexo in 'Mm':  # Raciocínio: Apesar de estar escrito que o contador tem de estar na posição
        # 1 e tem que cumprir a exigência seguinte (após o "and"), vamos entender que se a regra não é satisfeita,
        # ela começa, então, a procurar a partir da posição 1, e segue nas repetições seguintes, até a regra ser
        # satisfeita. Isso, pois, verifiquei que se a posição 1 é uma mulher, ele não dá erro, mas continua a
        # procurar nas repetições seguintes.
        idadevelho = idade # Lembre-se: a leitura aqui do sinal de "=" é "recebe"!. Ou seja, se a condição "if" é
        # satisfeita, a variável "idadevelho", que até então era "0", recebe o que foi inserido na variável "idade".
        nomevelho = nome # O mesmo vale aqui: se a condição "if" é satisfeita, a variável "nomevelho", que até então
        # estava vazia (''), recebe o que foi digitado em "nome".

    elif sexo in 'Mm' and idade > idadevelho: # Descrição: "se o digitado em "sexo" possui M ou m, e o dado digitado
        # em "idade" é maior do que o encontrado em "idadevelho", então dar prosseguimento."
        idadevelho = idade
        nomevelho = nome
    elif sexo in "Ff" and idade < 20:
        mulheres20 += 1

médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade:.0f}.')
print(f'O homem mais velho tem {idadevelho} e se chama {nomevelho}.')
print(f'Há {mulheres20} mulher(es) abaixo de 20 anos.')
