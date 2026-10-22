from collections import namedtuple
from csv import reader
from datetime import datetime, date, time, timedelta

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