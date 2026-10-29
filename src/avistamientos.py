from csv import reader
from datetime import datetime
from math import radians, sin, cos, asin, sqrt
from collections import Counter, defaultdict
from typing import NamedTuple
import locale
import statistics

#datetime,city,state,shape,duration,comments,latitude,longitude
Avistamiento=NamedTuple('Avistamiento', [('fechahora', datetime), 
                                         ('city', str),
                                         ('state', str),
                                         ('shape', str),
                                         ('duration', int),
                                         ('comments', str),
                                         ('latitude', float),
                                         ('longitude', float)])

def lee_avistamientos(ruta:str)->list[Avistamiento]:
    result = []
    with open(ruta) as f:
        lector = reader(f)
        next(lector)
        for fechahora,city,state,shape,duration,comments,latitude,longitude in lector:
            fechahora = datetime.strptime(fechahora.strip(), '%m/%d/%Y %H:%M')  #07/04/2011 22:00
            city = city.strip()
            shape = shape.strip()
            comments = comments.strip()
            duration = int(duration.strip())
            latitude = float(latitude)
            longitude = float(longitude)
            result.append(Avistamiento(fechahora,city,state,shape,
                                       duration,comments,latitude,longitude))
    return result


def avistamiento_mayor_duracion(avistamientos: list[Avistamiento], forma:str)->Avistamiento:
    '''
    Devuelve el avistamiento de mayor duración de entre todos los
    avistamientos de una forma dada.
    :param avistamientos: lista de tuplas con la información de 
    los avistamientos 
    :param forma: forma del avistamiento 
    :return:  avistamiento más largo de la forma dada
    '''
    #Implementación con bucles
    filtrado = []
    for x in avistamientos:
        if x.shape == forma:
            filtrado.append(x)

    return max(filtrado, key= lambda a: a.duration)


def avistamientos_fechas(avistamientos:list[Avistamiento], fecha_inicial:datetime.date|None=None, fecha_final:datetime.date|None=None)->list[Avistamiento]:
    '''
    Devuelve una lista con los avistamientos que han tenido lugar
    entre fecha_inicial y fecha_final (ambas inclusive). La lista devuelta
    estará ordenada de los avistamientos más recientes a los más antiguos.
    
    Si fecha_inicial es None se devolverán todos los avistamientos
    hasta fecha_final.
    Si fecha_final es None se devolverán todos los avistamientos desde
    fecha_inicial.
    Si ambas fechas son None se devolverá la lista de 
    avistamientos completa. 
    
    Usar el método date() para obtener la fecha de un objeto datetime.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param fecha_inicial: fecha a partir de la cual se devuelven los avistamientos
    :param fecha_final: fecha hasta la cual se devuelven los avistamientos
    :return: lista de tuplas con la información de los avistamientos en el rango
      de fechas
    '''
    fecha_f = datetime.max
    fecha_i = datetime.min
    if fecha_inicial is not None:
        fecha_i = fecha_inicial
    if fecha_final is not None:
        fecha_f = fecha_final
    filtrado = filter(lambda a: fecha_final>=a.fechahora.date()>=fecha_inicial , 
                      avistamientos)
    return sorted(filtrado, key = lambda a: a.fechahora)
