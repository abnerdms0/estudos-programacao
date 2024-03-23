#cire um algoritimo que leia um numero e mostre seu, seu triplo e a raiz quadrada

numero = int(input('Digite um numero: '))

dobro = numero * 2 
triplo = numero * 3 
raiz = numero ** 0.5

print(f'O dobro de {numero} é {numero * 2}, o triple o {numero * 3} e a raiz é {numero ** 0.5}') #primeira forma 

print(f'O dobro de {numero} é {dobro}, o triplo é {triplo} e a raiz é {raiz}') #segunda forma com mais uso de memoria 
