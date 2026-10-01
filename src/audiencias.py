from collections import namedtuple
from csv import reader

Audiencia = namedtuple("Audiencia", "edicion, share")

def lectura_gh(nombre_fichero:str)->list[Audiencia]:
    result = []
    with open(nombre_fichero, encoding="UTF-8") as fichero:
        lector = reader(fichero)
        next(lector)
        for edicion, share in lector:
            audiencia = Audiencia(int(edicion), float(share))
            result.append(audiencia)
    return result

def shares_gh(listado_audiencias:list[Audiencia])->list[float]:
    'Listado de shares de todo GH'
    result = []
    for audiencia in listado_audiencias:
        result.append(audiencia.share)
    return result

def ediciones_gh(listado_audiencias:list[Audiencia])->list[int]:
    result = []
    for audiencia in listado_audiencias:
        result.append(audiencia.edicion)
    return list(set(result))

def audiencias_mayoritarias(listado_audiencias:list[Audiencia])->list[Audiencia]:
    result = []
    for audiencia in listado_audiencias:
        if audiencia.share>=0.5:
            result.append(audiencia)
    return result

def audiencias_en_intervalo_cerrado(listado_audiencias:list[Audiencia], 
                                    minimo:float, maximo:float)->list[Audiencia]:
    result = []
    for audiencia in listado_audiencias:
        if maximo>=audiencia.share>=minimo:
            result.append(audiencia)
    return result
