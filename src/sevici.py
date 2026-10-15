
from csv import reader
import math 
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
    result = []
    for x in estaciones:
        if x.bicis_disponibles >= k:
            result.append(x)

    return [(x.bicis_disponibles, x.nombre) for x in result]

