# escolha de ordem de apresentacao; 

import random

nome1 = str(input('Informe o nome: '))
nome2 = str(input('Informe o nome: '))
nome3 = str(input('Informe o nome: '))
nome4 = str(input('Informe o nome: '))

lista = [nome1, nome2, nome3, nome4]

random.shuffle(lista)

print(f'A ordem de apresentacao sera: ')
print(lista)