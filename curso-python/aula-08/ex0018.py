# crie um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo;

import math


angulo = float(input('Informe o valor de um angulo qualquer: '))

sen0 = math.sin(angulo)

cos0 = math.cos(angulo)

tang0 = math.tan(angulo)

print(f'O seno de {angulo} é {sen0:.2f} \n'
      f'O coseno de {angulo} é {cos0 :.2f} \n'
      f'E a tangente de {angulo} é {tang0 :.2f}'
      )
