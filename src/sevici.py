
from csv import reader
from math import sqrt 
from collections import namedtuple

# Creación de un tipo de namedtuple para las coordenadas
# type: Coordenadas(float, float)
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
# Creación de un tipo de namedtuple para las estaciones
# type: Estacion(str, int, int, int, Coordenadas(float, float))
Estacion = namedtuple('Estacion', 'nombre, bornetas, ' \
'bornetas_vacias, bicis_disponibles, ubicacion')

def lee_datos(path:str, codificacion:str)->list[Estacion]:
    '''name,slots,empty_slots,free_bikes,latitude,longitude
    149_CALLE ARROYO,20,11,9,37.397829929383,-5.97567172039552
    257_TORRES ALBARRACIN,20,16,4,37.38376948792722,-5.908921914235877
    243_GLORIETA DEL PRIMERO DE MAYO,15,6,9,37.380439481169994,-5.953481197462845
    109_AVENIDA SAN FRANCISCO JAVIER,15,1,14,37.37988413609134,-5.974382770011586
    073_PLAZA SAN AGUSTIN,15,10,4,37.38951386231434,-5.984362789545622'''
    result = []
    with open(path, encoding=codificacion) as f:
        lector = reader(f)
        next(lector)
        for name,slots,empty_slots,free_bikes,latitude,longitude in lector:
            ubicacion = Coordenadas(float(latitude),
                                float(longitude))
            estacion = Estacion(name,int(slots),int(empty_slots),
                                int(free_bikes),ubicacion)
            result.append(estacion)
    return result

def filtra_estaciones_con_bicis_disponibles(estaciones:list[Estacion], 
                            k:int=5):
  result = []
  for x in estaciones:
      if x.bicis_disponibles >= k:
          result.append(x)
  return result

def estaciones_bicis_libres(estaciones:list[Estacion], 
                            k:int=5)->list[tuple[int, str]]:
    ''' Estaciones que tienen bicicletas libres
    
    ENTRADA: 
      :param estaciones: lista de estaciones disponibles 
      :type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      :param k: número mínimo requerido de bicicletas
      :type k: int
    SALIDA: 
      :return: lista de estaciones seleccionadas
      :rtype: [(int, str)] 
    
    Toma como entrada una lista de estaciones y un número k.
    Crea una lista formada por tuplas (número de bicicletas libres, nombre)
    de las estaciones que tienen al menos k bicicletas libres. La lista
    estará ordenada de mayor a menor por el número de bicicletas libres.
    '''
    result = filtra_estaciones_con_bicis_disponibles(estaciones, k)
    return [(x.bicis_disponibles, x.nombre) for x in result]

def calcula_distancia(coordenadas1: Coordenadas, coordenadas2: Coordenadas)->float:
    ''' Distancia entre un punto y una estación
    ENTRADA: 
    :param coordenadas1: coordenadas del primer punto
    :type coordenadas1: Coordenadas(float, float)
    :param coordenadas2: coordenadas del segundo punto
    :type coordenadas2: Coordenadas(float, float)
      
    SALIDA: 
    :return: distancia entre dos coordenadas
    :rtype: float 
    
    Toma como entrada dos coordenadas y calcula la distancia entre ambas aplicando la fórmula
    
        distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
    '''
    return sqrt((coordenadas2.longitud-coordenadas1.longitud)**2 + 
                (coordenadas2.latitud-coordenadas1.latitud)**2)


def estaciones_cercanas(estaciones:list[Estacion], coordenadas:Coordenadas, k:int=5)->tuple[float, str, int]:
    ''' Estaciones cercanas a un punto dado
    
    ENTRADA: 
      :param estaciones: lista de estaciones disponibles
      :type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      :param coordenadas: coordenadas formada por la latitud y la longitud de un punto
      :type coordenadas: Coordenadas(float, float)
      :param k: número de estaciones cercanas a calcular 
      :type k: int
    SALIDA: 
      :return: Una lista de tuplas con la distancia, nombre y bicicletas libres de las estaciones seleccionadas 
      :rtype: [(float, str, int)] 
    
    Toma como entrada una lista de estaciones,  las coordenadas de  un punto y
    un valor k.
    Crea una lista formada por tuplas (distancia, nombre de estación, bicicletas libres)
    con las k estaciones con bicicletas libres más cercanas al punto dado, ordenadas por
    su distancia a las coordenadas dadas como parámetro.
    '''
    result = []
    estaciones_con_bicis:list[Estacion] = filtra_estaciones_con_bicis_disponibles(estaciones, 1)
    for x in estaciones_con_bicis:
        distancia = calcula_distancia(x.ubicacion, coordenadas)
        tupla = (distancia, x.nombre, x.bicis_disponibles)
        result.append(tupla)
    return result


def media_coordenadas (coordenadas:list[Coordenadas])->Coordenadas:
    '''Devuelve una coordenada cuya latitud es la media de las latitudes y
    cuya longitud es la media de las longitudes.
    ENTRADA
        :param coordenadas: lista de coordeandas
        :ptype estaciones: [Coordenadas(float, float)]
    SALIDA
        :return: Una coordenada cuya longitud es la media de las longitudes, y la 
             latitud la media de las latitudes
        :rtype: Coordenadas(float, float)
    '''
    result_latitud, result_longitud = 0,0
    total = len(coordenadas)
    for x in coordenadas:
        result_latitud +=x.latitud/total
        result_longitud += x.longitud/total

    return Coordenadas(result_latitud, result_longitud)

def media_coordenadas_2 (coordenadas:list[Coordenadas])->Coordenadas:
    '''Devuelve una coordenada cuya latitud es la media de las latitudes y
    cuya longitud es la media de las longitudes.
    ENTRADA
        :param coordenadas: lista de coordeandas
        :ptype estaciones: [Coordenadas(float, float)]
    SALIDA
        :return: Una coordenada cuya longitud es la media de las longitudes, y la 
             latitud la media de las latitudes
        :rtype: Coordenadas(float, float)
    '''
    result = None
    total = len(coordenadas)
    if total>0:
      result_latitud, result_longitud = [],[]
      for x in coordenadas:
          result_latitud.append(x.latitud)
          result_longitud.append(x.longitud)
      result = Coordenadas(sum(result_latitud)/total, sum(result_longitud)/total)
    return result
