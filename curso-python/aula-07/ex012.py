#escreva um programa que calcule a area de uma sala, e em seguida calcule quantos litros de tintas serao necessarias para pinta-la sabendo que o 1 litro de tinta pinta 2m^2

largura = float(input('Informe em metros a largura do espaco que deseja pintar: '))

altura = float(input('Informe em metros o valor da altura do espaco que deseja pintar: '))

metrosQuadrado = largura * altura 

tinta = metrosQuadrado / 2

print(
    f'A parede que deseja pintar possui {metrosQuadrado} metros quadrados\n'
    f'Serão necessários {tinta} litros de tinta para cobrir a área' 
)