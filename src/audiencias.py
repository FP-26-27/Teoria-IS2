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
    '[x]->[f(x)]'
    result = []
    for x in listado_audiencias:
        f_x = x.share
        result.append(f_x)
    return result

def ediciones_gh(listado_audiencias:list[Audiencia])->set[int]:
    result = []
    for audiencia in listado_audiencias:
        result.append(audiencia.edicion)
    return set(result)

def calcula_numero_ediciones(listado_audiencias:list[Audiencia])->int:
    result = ediciones_gh(listado_audiencias)
    return len(result)

def audiencias_mayoritarias(listado_audiencias:list[Audiencia])->list[Audiencia]:
    result = []
    for x in listado_audiencias:
        if x.share>=0.5:
            result.append(x)
    return result

def audiencias_en_intervalo_cerrado(listado_audiencias:list[Audiencia], 
                                    minimo:float, maximo:float)->list[Audiencia]:
    result = []
    for audiencia in listado_audiencias:
        if maximo>=audiencia.share>=minimo:
            result.append(audiencia)
    return result

def filtra_por_ediciones(audiencias:list[Audiencia], 
                         ediciones:list[int])->list[Audiencia]:
    result = []
    for x in audiencias:
        if x.edicion in ediciones:
            result.append(x)
    return result

def extrae_shares(audiencias:list[Audiencia]
                               )->list[float]:
    result = []
    for x in audiencias:
        y = x.share
        result.append(y)
    return result

def filtra_por_ediciones_pares(audiencias:list[Audiencia]
                               )->list[Audiencia]:
    result = []
    for x in audiencias:
        if x.edicion % 2==0:
            result.append(x)
    return result

def media_share(audiencias: list[Audiencia])->float:
    result=0
    for x in audiencias:
        result += x.share/len(audiencias)

    return result

def media_share_2(audiencias: list[Audiencia])->float:
    result = 0.0
    if(len(audiencias)>0):
        shares = shares_gh(audiencias)
        result = sum(shares)/len(audiencias)
    return result

def contar_audiencias_extremas(audiencias:list[Audiencia], 
                               bajo:float, alto:float)->int:
    '''result = []
    for x in audiencias:
        if x.share<bajo or x.share>alto:
            result.append(x)'''
    result = [x for x in audiencias if x.share<bajo or x.share>alto]
    return len(result)