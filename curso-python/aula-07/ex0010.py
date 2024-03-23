#faça um programa que leia um numero inteiro qualquer e mostre sua tabuada; 

numero = int(input('Informe um numero: '))

for i in range(11):
    print(f'{numero} x {i} = {numero * i}')