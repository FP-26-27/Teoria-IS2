from collections import Counter, defaultdict, namedtuple
from csv import reader
from datetime import datetime, date, time, timedelta
from statistics import mean

Vuelo=namedtuple('Vuelo', 'destino, precio, numero_plazas, numero_pasajeros, codigo, fecha, duracion')

def lee_vuelos(ruta:str)->list[Vuelo]:
    result = []
    with open(ruta) as f:
        lector = reader(f)
        for destino, precio, numero_plazas, numero_pasajeros, codigo, dia, mes, anyo, horas, minutos in lector:
            destino = destino.strip()
            precio = float(precio)
            numero_plazas = int(numero_plazas)
            numero_pasajeros = int(numero_pasajeros)
            codigo = codigo.strip()
            dia = int(dia)
            mes = int(mes)
            anyo = int(anyo)
            horas = int(horas)
            minutos = int(minutos)
            fecha = date(anyo, mes, dia)
            duracion = timedelta(hours=horas, minutes=minutos)
            vuelo = Vuelo(destino, precio, numero_plazas, numero_pasajeros, codigo, fecha, duracion)
            result.append(vuelo)

    return result

def filtra_vuelos_completos(vuelos:list[Vuelo])->list[Vuelo]:
    result = []
    for v in vuelos:
        if v.numero_plazas<= v.numero_pasajeros:
            result.append(v)
    return result

def transforma_a_codigos(vuelos:list[Vuelo])->list[str]:
    return [v.codigo for v in vuelos]

def codigo_vuelos_completos(vuelos:list[Vuelo])->list[str]:
    filtrado = filtra_vuelos_completos(vuelos)
    return transforma_a_codigos(filtrado)


def filtra_vuelos_a_destino(vuelos:list[Vuelo], destino:str)->list[Vuelo]:
    result = []
    for v in vuelos:
        if v.destino == destino:
            result.append(v)
    return result

def transforma_a_plazas_libres(vuelos:list[Vuelo])->list[str]:
        return [v.numero_plazas-v.numero_pasajeros for v in vuelos]
        
def total_plazas_libres_a_destino(vuelos:list[Vuelo], destino:str)->int:
    vuelos_a_destino = filtra_vuelos_a_destino(vuelos, destino)
    listado_plazas_libres_a_destino:list[int] = transforma_a_plazas_libres(vuelos_a_destino)
    return sum(listado_plazas_libres_a_destino)

def duracion_vuelos_fecha_2(vuelos:list[Vuelo], fecha:date)->timedelta:
    filtro = [v for v in vuelos if v.fecha == fecha]
    transformacion = [v.duracion for v in filtro]
    result = timedelta()
    for duracion in transformacion:
        result += duracion
    return result

def duracion_vuelos_fecha(vuelos:list[Vuelo], fecha:date)->timedelta:
    result = timedelta()
    for v in vuelos:
        if v.fecha == fecha:
            result += v.duracion
    return result

def total_pasajeros_por_destino(vuelos: list[Vuelo])->dict[str, int]:
    '''`total_pasajeros_por_destino`: Dada una lista de tuplas 
    de tipo `Vuelo` devuelve un diccionario que relaciona cada destino
      con el número de pasajeros a ese destino.'''
    result = dict()
    for v in vuelos:
        clave = v.destino
        if clave in result:
            result[clave] += v.numero_pasajeros
        else:
            result[clave] = v.numero_pasajeros
    return result    

def total_pasajeros_por_destino(vuelos: list[Vuelo])->dict[str, int]:
    '''`total_pasajeros_por_destino`: Dada una lista de tuplas 
    de tipo `Vuelo` devuelve un diccionario que relaciona cada destino
      con el número de pasajeros a ese destino.'''
    result = dict()
    for v in vuelos:
        clave = v.destino
        if clave in result:
            result[clave] += v.numero_pasajeros
        else:
            result[clave] = v.numero_pasajeros
    return result    


def total_pasajeros_por_destino_2(vuelos: list[Vuelo])->dict[str, int]:
    '''`total_pasajeros_por_destino`: Dada una lista de tuplas 
    de tipo `Vuelo` devuelve un diccionario que relaciona cada destino
      con el número de pasajeros a ese destino.'''
    agregador = dict()
    for v in vuelos:
        clave = v.destino
        if clave in agregador:
            agregador[clave].append(v)
        else:
            agregador[clave] = [v]
    transformado = dict()
    for destino, lista_vuelos in agregador.items():
        transformado[destino] = sum([v.numero_pasajeros for v in lista_vuelos])
    return transformado    

def codigo_vuelo_mas_barato_por_destino_2(vuelos:list[Vuelo])->dict[str, str]:
    '''Ejercicio 29. codigo_vuelo_mas_barato_por_destino: 
    Dada una lista de tuplas de tipo Vuelo devuelve un diccionario 
    que relaciona cada destino con el código del vuelo 
    más barato a ese destino.'''
    agregador = dict()
    for v in vuelos:
        clave = v.destino #editar
        if clave in agregador:
            agregador[clave].append(v)
        else:
            agregador[clave] = [v]
    transformado = dict()
    for destino, lista_vuelos in agregador.items():
        minimo = min(lista_vuelos, key = lambda v: v.precio)
        transformado[destino] =  minimo.codigo#editar
    return transformado  #editar

def codigo_vuelo_mas_barato_por_destino(vuelos:list[Vuelo])->dict[str, str]:
    '''Ejercicio 29. codigo_vuelo_mas_barato_por_destino: 
    Dada una lista de tuplas de tipo Vuelo devuelve un diccionario 
    que relaciona cada destino con el código del vuelo 
    más barato a ese destino.'''
    result = dict()
    for v in vuelos:
        clave = v.destino
        if clave in result:
            if result[clave].precio > v.precio:
                result[clave] = v
        else:
            result[clave] = v
    return {clave: vuelo.precio for clave, vuelo in result.items()}    


def total_pasajeros_por_destino(vuelos: list[Vuelo])->dict[str, int]:
    '''`total_pasajeros_por_destino`: Dada una lista de tuplas 
    de tipo `Vuelo` devuelve un diccionario que relaciona cada destino
      con el número de pasajeros a ese destino.'''
    result = dict()
    for v in vuelos:
        clave = v.destino
        if clave in result:
            result[clave] += v.numero_pasajeros
        else:
            result[clave] = v.numero_pasajeros
    return result    

def precio_medio_por_destino(vuelos: list[Vuelo])->dict[str, float]:
    '''Ejercicio 27. precio_medio_por_destino: Dada una lista de tuplas 
    de tipo Vuelo devuelve un diccionario tal que relaciona cada destino 
    con el precio medio de los vuelos a ese destino. Resultados esperados'''
    agregador = dict()
    for v in vuelos:
        clave = v.destino #editar
        if clave in agregador:
            agregador[clave].append(v)
        else:
            agregador[clave] = [v]
    transformado = dict()
    for destino, lista_vuelos in agregador.items():
        transformado[destino] = calcula_media(lista_vuelos)#editar
    return transformado  #editar

def calcula_media(lista:list[Vuelo])->float:
    result = 0
    for v in lista:
        result += v.precio/len(lista)
    return result

def fecha_mayor_incremento_pasajeros(vuelos: list[Vuelo])->date:
    '''Ejercicio 39. fecha_mayor_incremento_pasajeros: Dada una lista de tuplas de tipo Vuelo
      devuelve cuál es la fecha con mayor incremento del número de pasajeros 
      respecto del día anterior. 
      El concepto del día anterior se refiere al anterior que hubo vuelos.'''
    agregador = dict()
    for v in vuelos:
        clave = v.fecha #editar
        if clave in agregador:
            agregador[clave].append(v)
        else:
            agregador[clave] = [v]
    transformado = dict()
    for clave, lista_vuelos in agregador.items():
        transformado[clave] = sum([v.numero_pasajeros for v in lista_vuelos])#editar
    return mayor_incremento(transformado)  #editar

def mayor_incremento(transformado: dict[date, int])->date:
    lista = sorted(transformado.items())
    cremallera = zip(lista, lista[1:]) #[((dia1, valor_1), (dia2, valor_2))...]
    result = None
    mayor = None
    for (_, pasajeros_anterior), (dia, pasajeros) in cremallera:
        incremento = pasajeros - pasajeros_anterior
        if mayor is None or incremento > mayor:
            mayor = incremento
            result = dia
    return result


def codigos_por_destino(vuelos: list[Vuelo])->dict[str, list[str]]:
    '''Ejercicio 25'''
    agregador = dict()
    for v in vuelos:
        clave = v.destino #editar
        if clave in agregador:
            agregador[clave].append(v)
        else:
            agregador[clave] = [v]
    transformado = dict()
    for destino, lista_vuelos in agregador.items():
        transformado[destino] = [v.codigo for v in lista_vuelos]#editar
    return transformado  #editar

# Ejercicio 31. destino_mas_vuelos: Dada una lista de tuplas de tipo 
# Vuelo devuelve el destino con mayor número de vuelos.

def destino_mas_vuelos(vuelos:list[Vuelo])->str:
    diccionario = defaultdict(int)
    for v in vuelos:
        clave = v.destino
        diccionario[clave] += 1

    return max(diccionario.keys(), key = lambda destino: diccionario[destino])

def destino_mas_vuelos_2(vuelos:list[Vuelo])->str:
    destinos = [v.destino for v in vuelos]
    counter = Counter(destinos)
    return counter.most_common()[0][0]


#Ejercicio 34. destino_mas_viajeros_por_mes: 
# Dada una lista de tuplas de tipo Vuelo devuelve 
# un diccionario en el que las claves sean los meses 
# y como valor el destino con más viajeros de cada mes.

def destino_mas_viajeros(vuelos:list[Vuelo])->str:
    result = defaultdict(int)
    for v in vuelos:
        result[v.destino] += v.numero_pasajeros
    #result["sevilla"] <-> result.get("sevilla")
    return max(result, key = result.get) #lambda destino: result[destino])

def destino_mas_viajeros_por_mes(vuelos:list[Vuelo])->dict[int, str]:
    agregador = defaultdict(list)
    for v in vuelos:
        clave = v.fecha.month
        agregador[clave].append(v)

    transformador = dict()
    for mes, lista_vuelos in agregador.items():
        transformador[mes] = destino_mas_viajeros(lista_vuelos)
    return transformador