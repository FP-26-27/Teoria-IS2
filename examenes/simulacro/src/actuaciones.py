from csv import reader
from collections import Counter, defaultdict
from datetime import datetime, date
from typing import NamedTuple

Actuacion = NamedTuple("Actuacion",[
    ("id_actuacion",int),
    ("recinto",str),
    ("artista",str),
    ("promotora",str),
    ("fecha_actuacion",date),
    ("asistentes_totales",int),
    ("asistentes_por_zona",dict[str, int]),
    ("teloneros",list[str]),
    ("tasa_ocupacion",float)
])
DELIMITADOR = ','
def parsea_teloneros(teloneros: str) -> list[str]:
    lista_teloneros = teloneros.replace('[', '').replace(']', '').replace('\'', '').split(DELIMITADOR)
    return [telonero.strip() for telonero in lista_teloneros]

def parsea_asistentes_por_zona(asistentes_por_zona:str)->dict[str,int]:
    #"{'pista': 4566, 'grada': 3708, 'vip': 702}"
    result = dict()
    asistentes_zona = asistentes_por_zona.replace("{", "").replace("}", "").replace("'", "")
    trozos = asistentes_zona.split(DELIMITADOR)
    
    for trozo in trozos:
        clave, valor = trozo.split(":")
        clave = clave.strip()
        result[clave] = int(valor) 

    return result
    
def lee_actuaciones(ruta: str)->list[Actuacion]:
    result = []
    with open(ruta) as f:
        lector = reader(f)
        next(lector)
        for id_actuacion,recinto,artista,promotora,fecha_actuacion,asistentes_totales,asistentes_por_zona,teloneros,tasa_ocupacion in lector:
            id_actuacion = int(id_actuacion.strip())
            recinto = recinto.strip()
            artista = artista.strip()
            promotora = promotora.strip()
            fecha_actuacion = datetime.strptime(fecha_actuacion, "%d/%m/%Y")
            fecha_actuacion = fecha_actuacion.date()
            asistentes_totales = int(asistentes_totales.strip())
            asistentes_por_zona = parsea_asistentes_por_zona(asistentes_por_zona.strip())
            teloneros = parsea_teloneros(teloneros.strip())
            tasa_ocupacion = float(tasa_ocupacion.strip()) 
            result.append(Actuacion(id_actuacion,recinto,artista,promotora,fecha_actuacion,asistentes_totales,asistentes_por_zona,teloneros,tasa_ocupacion))        

    return result

def telonero_mas_frecuente(actuaciones: list[Actuacion])->str:
    teloneros = []
    for a in actuaciones:
        teloneros += a.teloneros
    frecuencia_teloneros = dict()
    for telonero in teloneros:
        clave = telonero 
        if clave in frecuencia_teloneros:
            frecuencia_teloneros[clave] += 1
        else:
            frecuencia_teloneros[clave] = 1
    return max(frecuencia_teloneros, key = lambda telonero: frecuencia_teloneros[telonero]) 

def telonero_mas_frecuente_por_recinto(actuaciones:list[Actuacion],
                           ocupacion_minima: float = 0.0) -> dict[str,str]:
    filtrado = filter(lambda a: a.tasa_ocupacion>ocupacion_minima, actuaciones)

    agregador = dict()
    for a in filtrado:
        clave = a.recinto
        if not clave in agregador:
            agregador[clave] = [a]
        else:
            agregador[clave].append(a)

    transformado = dict()
    for recinto, lista_actuaciones in agregador.items():
        transformado[recinto] = telonero_mas_frecuente(lista_actuaciones)
    return transformado