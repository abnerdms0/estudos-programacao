#crie um exercicio que leia um numero Real qualque pelo teclado e mostre na tela a sua porcao inteira: 

import math

numero = float(input('Infome um numero real: '))

print(f'A parte inteira no numero {numero} é {math.trunc(numero)}')