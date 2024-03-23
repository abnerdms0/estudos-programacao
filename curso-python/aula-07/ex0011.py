#crie um programa que leia quanto de dinheiro uma pessoa tem e quantos dolares ela pode compar; 

dinheiro = float(input('Informe a quantidade de dinheiro em reais que você possui: R$ '))

print(f'Com o saldo de {dinheiro} é possível comprar {dinheiro // 3.27} dollar(es), mais precisamente {dinheiro / 3.27 :.2f} dollar(es)')