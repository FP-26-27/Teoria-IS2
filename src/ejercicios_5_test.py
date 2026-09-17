from ejercicios_5 import *

def test_sumar_pares(inicio, fin):
    suma = sumar_pares(inicio,fin)
    print(suma)

def test_factorial(numero):
    print(factorial(numero))

def test_suma_digitos(numero):
    print('El valor para ', numero, ' es ', suma_digitos(numero))

def test_contar_vocales(cadena):
    print(contar_vocales(cadena))

#test_sumar_pares(1,4)
#test_sumar_pares(1,5)

#test_factorial(0)
#test_factorial(5)

#test_suma_digitos(1001)

test_contar_vocales("AEIOUaeiou")
test_contar_vocales("bcdfg")