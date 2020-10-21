# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
print()

# Novidade: novo conceito: "acumuladores". Crie uma variável indicando o que será a soma, e ela começa com 0.
# Mais para o final, indique que você quer que todos os números vão sendo acrescentados a esse 0.

soma = 0 # começando com a criação da variável "soma", indicando que ela é, incialmente, um número 0.
cont = 0 # como um extra, também vamos contar quantos números são no final
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c #Agora, vamos indicar que a soma deste "range" é o que ela é agora (0)
        # mais os números do contador "c".
        cont = cont + 1 # vamos indicar a quantidade de números que estão dentro da regra.

        #soma += c
        #cont += 1 (formas simplificadas de escrever esta função. Indica, por exemplo, que "cont é igual a
        # ele mesmo mais um").

print(f'São {cont} valores que são ímpares e divididos por 3, e sua soma é {soma}')
