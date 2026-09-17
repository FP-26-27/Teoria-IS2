from ejercicios_1 import *
'''
peso = input("Introduzca su peso: ")
peso = float(peso)
print(peso, " kgs")
altura = input("Introduzca su altura en metros: ")
altura = float(altura)
print(altura, " m")
imc = calcula_imc(peso, altura)
print(imc)

estado = calcula_estado_nutricional(peso, altura)
print('Tu estado es: ', estado)
'''

metricas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]

estados = genera_estados_nutricionales(metricas)
for estado in estados:
    print(estado)