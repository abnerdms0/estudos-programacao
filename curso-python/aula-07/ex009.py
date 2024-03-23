#escreva um algoritimo que leia um valor em metros e exiba convertido em centimetros e milimetros

value = int(input('informe um valor em metros: '))

centimetros = value * 100
milimetros = value * 1000

print(
    f'O valor {value} convertido para centimetros é {centimetros}; \n'
    f'O valor {value} convertido para milimetros é {milimetros}'
)#forma com mais gasto de memoria; 

print(40 * '-')

print(
    f'O valor {value} convertido para centrimentros é de {value * 100} \ne de centimetros é {value * 1000}'
)