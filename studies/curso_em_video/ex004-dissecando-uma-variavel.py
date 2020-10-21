# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

# Obs: o que vem antes de um . , é chamado de "objeto". Ou seja, em "a.isnumeric", o "a" é um objeto e o "isnumeric"
# método (por que tem () no final)

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('É um número?', a.isnumeric())
print('É um texto?', a.isalpha())
print('É em somente em maiúsculas?', a.isupper())
print('É somente em minúsculas?', a.islower())
print('É capitalizado?', a.istitle())
print('É alfanumérico?', a.isalnum())
print('Está somente com espaço?', a.isspace())
#  o trecho abaixo não faz parte do exercício, foi apenas um teste a mais.
print('É um ASCII, (texto alfabetico sem ser ideogramas ou escrita arábica ou acentuado)?', a.isascii())
print('É um dígito?', a.isdigit())
print('É sem caracteres especiais? ',a.isidentifier())
print('É imprimível?', a.isprintable())
print('Bem-vindo {}, como está? Espero que esteja bem!'.format(a))
