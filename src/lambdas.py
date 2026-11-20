VALORES = [('Jorge', 45), ('Germán', 41), ('Diego', 72)]
'''def transforma_a_nombre(listado:list[tuple[str, int]])->list[str]:
    #x->f(x)
    result = []
    for x in listado:
        result.append(x[0])
    return result

def transforma_a_edad(listado:list[tuple[str, int]])->list[str]:
    #x->f'(x)
    result = []
    for x in listado:
        result.append(x[1])
    return result
'''

def transforma(listado:list, funcion: callable):
    result = []
    for x in listado:
        result.append(funcion(x))
    return result

nombres = transforma(VALORES, lambda x:x[0])
edades = transforma(VALORES, lambda x:x[1])

def filtra_mayor_de_18(listado: list):
    result = []
    for x in listado:
        if x[1]>18:
            result.append(x)
    return result

def filtra_nombre_largo(listado: list):
    result = []
    for x in listado:
        if len(x[0])<10:
            result.append(x)
    return result

def filtra(listado:list, funcion:callable):
    result = []
    for x in listado:
        if funcion(x):
            result.append(x)
    return result

nombres = filtra(VALORES, lambda x:len(x[0])<10)
edades = filtra(VALORES, lambda x:x[1]>18)


def transforma_a_nombres(listado):
    lambda_nombre = lambda x: x[0]
    return list(map(lambda_nombre, listado))

def transforma_a_edades(listado):
    lambda_nombre = lambda x: x[1]
    return list(map(lambda_nombre, listado))

#print(transforma_a_nombres(VALORES))
#print(transforma_a_edades(VALORES))

print(max(VALORES, key = lambda x: x[1]))