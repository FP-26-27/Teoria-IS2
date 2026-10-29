VALORES = [('Jorge', 45), ('Germán', 41), ('Diego', 72)]

'''def transforma(listado, aplica_transformacion: callable):
    result = []
    for x in listado:
        result.append(aplica_transformacion(x))
    return result'''

def transforma_a_nombres(listado):
    lambda_nombre = lambda x: x[0]
    return list(map(lambda_nombre, listado))

def transforma_a_edades(listado):
    lambda_nombre = lambda x: x[1]
    return list(map(lambda_nombre, listado))

print(transforma_a_nombres(VALORES))
print(transforma_a_edades(VALORES))

 