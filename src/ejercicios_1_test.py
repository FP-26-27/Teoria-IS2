from ejercicios_1 import *

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
