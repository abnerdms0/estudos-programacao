#aluguel de carros: escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R% 60 por dia e R$ 0.15 por Km rodado; 

distancia = float(input('Qual a quantidade de quilometros usados: '))

dias = int(input('Informe a quantidade de dias do aluguel: '))

totalDias = dias * 60.0
totalKm = distancia * 0.15

print(f'O total do aluguel ficará R$ {totalKm + totalDias}, sendo R$ {totalDias} o valor referente aos dias de locacao, e R$ {totalKm} referente aos quilometros rodados')