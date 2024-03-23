#desenvolva um programa que leia duas notas de um aluno e mostre sua media

nota = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))

media = (nota + nota2) / 2

print(f'A medida das notas {nota} e {nota2} é {media}') #mais uso de memoria 
print(f'A media das notas {nota} e {nota2} é {(nota + nota2) / 2}') #menos uso de memoria 
