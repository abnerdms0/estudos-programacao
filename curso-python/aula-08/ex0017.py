#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipoteenusa; 

import math

catOp = float(input('Informe o valor do cateto oposto do triangulo: '))

catAdj = float(input('Informe o valor do cateto adjacente: '))

hipot = math.hypot(catOp, catAdj)

print(f'A hipotenusa do triangulo cujo o cateto oposto é {catOp}, e o cateto adjacente é {catAdj} é {hipot :.2f}')



