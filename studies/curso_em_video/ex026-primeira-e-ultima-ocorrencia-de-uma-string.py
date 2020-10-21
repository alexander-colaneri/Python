# Primeira e última ocorrência de uma string
# Enunciado: Faça um programa que leia uma frase e mostre:
# 1 - Quantas vezes aparece a letra "A"
# 2 - Em que posição ela aparece a primeira vez.
# 3 - Em que posição ela aparece a última vez.
print()
frase = str(input('Digite a frase: ')).strip().upper().replace('', "").replace('Ç', 'C').replace('Â', 'A').replace('Ã', 'A').replace('Á', 'A').replace('À', 'A').replace('É','E').replace('Ê', 'E').replace('Í', 'I').replace('Õ', 'O'). replace('Ô', 'O').replace('Ó', 'O').replace('Ú', 'U')
# O "replace" foi adicionado como um extra, para localizar vogais com acentos e cedilha. Foi preciso adicionar
# replace('', ""), não sei ainda o raciocínio mas funcionou.
letra = str(input('Digite a letra a ser encontrada: ')).strip().upper()
print()
# A escolha da letra não era parte do exercício, mas resolvi colocar após ver um comentário.
print(f'A letra "{letra}" apareceu {frase.count(letra)} vez(es).')
print(f'A letra "{letra}" apareceu pela primeira vez na posição {frase.find(letra) + 1}.')
# Foi colocado um "+1" acima para indicar a posição da letra na língua portuguesa, não na linguagem Python.
print(f'A letra "{letra}" apareceu pela última vez na posição {frase.rfind(letra) + 1}.')
# A funcionalidade rfind procura da direita (right) para a esquerda, mantendo a contagem da esquerda para direita.
