#sorteio entre 4 alunos para apagar o quadro;

import random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1, n2, n3, n4]

sorteado = (f'O aluno escolhido foi {random.choice(lista)}')

print(sorteado)