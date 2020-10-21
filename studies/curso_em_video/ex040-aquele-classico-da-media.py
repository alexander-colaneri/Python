# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print()
print('*' * 5, 'Calculadora de Notas V2', '*' * 5)
print()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print(f'Sua média foi {média:.1f} e está abaixo de 5,0: \033[1;31mREPROVADO\033[m.')
elif 5 <= média <= 6.9:
    print(f'Sua média foi {média:.1f}: \033[1;35mRECUPERAÇÃO\033[m.')
elif 7 <= média <= 10:
    print(f'Sua média foi {média:.1f}: \033[1;32mAPROVADO!\033[m')
else:
    print('Erro na inserção das notas, favor verificar.')
