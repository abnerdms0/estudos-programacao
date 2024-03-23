print('operadores aritmeticos: ')

print(
    'soma: + \n'
    'subtracao: - \n'
    'multiplicacao: * \n'
    'divisao: / \n'
    'exponenciacao: ** \n'
    'divisao inteira: // \n'
    'resto da divisao: % \n'
    )

print('-----------------------------')

print(
    'Ordem de precedencia: \n'
    '----------------------- \n'
    'parenteses: () \n'
    'exponenciacao: ** - que tambem pode ser feita com: pow(numer, potencia) \n'
    'multiplicao, divisao, div. inteira e resto da div: *, /, // e % \n'
    'soma e subtracao: +, - \n'
)

print('exemplos trabalhando com str')
nome = input('Qual seu nome? ')
print(f'muito prazer {nome :=^20}!')

print('----------------')

num1 = int(input('primeiro valor: '))
num2 = int(input('segundo valo: '))
soma = num1 + num2
multi = num1 * num2
divi = num1 / num2
divint = num1 // num2
restodiv = num1 % num2
pot = num1 ** num2 

print(
    f'A soma vale {soma} \n'
    f'A multiplicacao é {multi} \n'
    f'A divisao é {divi :.2f} \n'
    f'A divisao inteira é {divint} \n'
    f'O resto da divi é {restodiv} \n'
    f'A potencia é {pot} \n'
)

