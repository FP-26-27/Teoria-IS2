from csv import reader
from collections import namedtuple

Consumo = namedtuple("Consumo", "fecha, variacion")

def parsea_incremento(incremento_str:str)->float:
    return float(incremento_str)

def lectura_mensual(ruta_fichero:str)->list[tuple[str, float]]:
    result = []
    with open(ruta_fichero, encoding="UTF-8") as f:
        lector = reader(f)
        next(lector)
        for fecha_str, incremento_str  in lector:
            tupla = Consumo(fecha_str, parsea_incremento(incremento_str))
            result.append(tupla)
    return result

def media_incrementos(lista: list[Consumo[str, float]])->float:
    result = 0.
    dimension = len(lista)
    for dato in lista:
        result += dato.variacion/dimension
    return result

listado_datos = lectura_mensual("data/monthly_csv.csv")
print(listado_datos[0])
print(media_incrementos(listado_datos))