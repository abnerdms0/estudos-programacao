#calculo de preco com desconto em porcentagem; 
preco = float(input('Informe o preço do produto desejado: '))

preco = preco - (preco * 0.05)

print(f'O preco do produto em questao possui 5% de desconto, ficando o total de R$ {preco :.2f}, a pagar!')