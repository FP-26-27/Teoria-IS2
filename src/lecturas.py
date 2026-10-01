from csv import reader
from collections import namedtuple
from datetime import datetime

Consumo = namedtuple("Consumo", "fecha, variacion")

def parsea_incremento(incremento_str:str)->float:
    return float(incremento_str)

def parse_fecha(fecha_str:str)->datetime.date:
    fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y")
    return fecha_hora.date()

def lectura_mensual(ruta_fichero:str)->list[tuple[str, float]]:
    result = []
    with open(ruta_fichero, encoding="UTF-8") as f:
        lector = reader(f)
        next(lector)
        for fecha_str, incremento_str  in lector:
            tupla = Consumo(parse_fecha(fecha_str), 
                            parsea_incremento(incremento_str))
            result.append(tupla)
    return result

def media_incrementos(lista: list[Consumo[str, float]])->float:
    result = 0.
    dimension = len(lista)
    for dato in lista:
        result += dato.variacion/dimension
    return result


