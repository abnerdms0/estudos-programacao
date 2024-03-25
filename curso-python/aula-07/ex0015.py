#calculo de conversao de temperatura de celcius para fahrenheit; 

tempUs = float(input('Informe o valor da temperatura em fahrenheit: '))

tempCelcius = (tempUs - 32) / 1.8

print(f'A temperatura que em Celcius é de {tempCelcius :.2f}º.')

print(40 * '=')

gCelcius = float(input('Informe o valor em °C: '))

gCelcius = (gCelcius * 9/5) + 32

print(f'A temperatura informada em °F é de: {gCelcius :.2f}')
