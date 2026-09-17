''''Ejercicio 1
Defina una función calcula_imc que reciba como entrada el peso 
y la estatura de una persona (en kilogramos y metros, respectivamente) 
y calcule su índice de masa corporal o IMC.

Para probar la función, lea del teclado dos valores que representen 
el peso y la altura, llame a la función para calcular el IMC, y muéstrelo en la consola.

NOTA: Use la función predefinida input(mensaje) para leer datos desde el teclado.
'''
def calcula_imc(peso, altura):
    return peso / (altura ** 2)


'''Ejercicio 2
Defina una función calcula_estado_nutricional que 
reciba como parámetros el peso y la estatura 
de una persona (en kilogramos y metros, respectivamente), 
y devuelva una cadena de texto con el estado nutricional de la persona de acuerdo con su IMC. El estado nutricional puede ser uno de los siguientes:

Bajo peso: imc < 18.5
Normal: 18.5 <= imc < 25
Sobrepeso: 25 <= imc < 30
Obesidad: imc >= 30

Para probar la función, lea del teclado dos valores que representen el peso y la altura, llame a la función para calcular el estado nutricional, y muéstrelo en la consola.
'''
def calcula_estado_nutricional(peso, estatura):
    result = ''
    imc = calcula_imc(peso, estatura)
    if imc < 18.5:
        result = 'Tienes bajo peso'
    elif 18.5 <= imc < 25:
        result = 'Estás perfecto'
    elif 25 <= imc < 30:
        result = 'Tienes que cuidarte un poco'
    else:
        result = 'Tienes que cuidarte un mucho'
    return result


'''
Ejercicio 3
Defina una función imprime_estados_nutricionales que reciba como parámetro una lista de tuplas, que representan el peso y la altura de una serie de personas, y muestre el IMC y el estado nutricional de cada una de ellas. La salida en consola de la ejecución de la función debe ser parecida a esta:

El IMC de la persona 1 es 23.543, y su estado nutricional es Normal.
El IMC de la persona 2 es 27.324, y su estado nutricional es Sobrepeso.
...

Para probar la función, utilice esta lista de tuplas:

personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]
'''
def genera_estados_nutricionales(personas):
    result = []
    for peso, altura in personas:
        imc = calcula_imc(peso, altura)
        estado = calcula_estado_nutricional(peso, altura)
        tupla = (peso, altura)
        result.append("La persona "+ str(tupla) + " tiene imc " + str(imc) + 
              " y su estado nutricional es " + estado)
    return result



'''Ejercicio 4
Defina una función lee_numeros que lea varios números enteros del teclado
 y los devuelva almacenados en una lista. 
 La cantidad de números a leer será un parámetro de la función.

Pruebe la función lee_numeros pidiéndole que lea tantos números como indique el usuario por el teclado, y mostrando en la consola la lista resultante. A continuación, implemente los siguientes cálculos sobre la lista obtenida, mostrando el resultado de cada uno por consola:

Mayor número de la lista 
(PISTA: Busque una función predefinida de Python que realiza este cálculo)
Media de los números de la lista (si la lista estuviera vacía, se mostraría "No es posible calcular la media")
Número de elementos pares en la lista
Nueva lista con aquellos elementos de la lista leída que sean mayores a 10

Ejercicio 5
Defina una función calcula_dia_semana que reciba una fecha, 
de tipo date, y devuelva el nombre del día de la semana que corresponde a la fecha. 
PISTA: busca información sobre el método weekday() del tipo date.

Para probar la función, solicite al usuario que introduzca por teclado el día, mes y año de su nacimiento, construya un objeto de tipo date, y páselo a la función. Informe al usuario del día de la semana en que nació.'''