# Ejercicio: Avistamientos
**Autores**: Daniel Mateos, Mariano González, Toñi Reina   **Revisores**: Fermín Cruz, Toñi Reina, José C. Riquelme.     **Última modificación:** 10/11/2022

En este ejercicio vamos a trabajar con un conjunto de datos con información sobre avistamientos de objetos voladores no identificados (OVNIs) en los Estados Unidos. El objetivo del ejercicio es leer estos datos y realizar distintas operaciones con ellos. Cada operación se implementará en una función distinta.

Antes de comenzar, importaremos los módulos que necesitamos para realizar el ejercicio:


```python
import csv
from datetime import datetime
from math import radians, sin, cos, asin, sqrt
from collections import namedtuple, Counter, defaultdict
import locale
import statistics
```

## 1. Carga de datos
Los datos se encuentran almacenados en un fichero en formato CSV codificado en UTF-8. Cada registro del fichero ocupa una línea y contiene los datos correspondientes a un avistamiento: fecha y hora en la que se produjo del avistamiento, ciudad y acrónimo del estado donde se produjo, forma observada del avistamiento, duración en segundos, una descripción textual del avistamiento y la latitud y longitud del lugar donde se produjo.

Estas son las primeras líneas del fichero (acortando la descripción del avistamiento). La primera línea es una cabecera que contiene los nombres de los campos del registro:

    datetime,city,state,shape,duration,comments,latitude,longitude
    07/04/2011 22:00,muncie,in,light,240, ((HOAX??)) 4th  of July ufo...,40.1933333,-85.3863889
    04/07/2005 17:01,deming (somewhere near),nm,changing,1200, ((NUFORC...,32.2686111,-107.7580556
    03/12/2010 19:56,erie,pa,changing,300, 3/12/10Viewed a comet like...,42.1291667,-80.0852778
    07/04/2013 22:25,seattle,wa,unknown,600, A RED Light was seen over...,47.6063889,-122.3308333

### 1.1 Función de lectura de datos

Nuestra primera función será la encargada de leer el fichero con los avistamientos y construir a partir de él una estructura de datos en memoria, que será una lista de tuplas. Cada avistamiento se representará por una tupla a la cual daremos el nombre 'Avistamiento'. Esta tupla se apoyará en una tupla 'Coordenadas' que servirá para trabajar con las coordenadas y que mejorará el diseño de tipos. Define el tipo 'Coordenadas' en un módulo 'coordenadas.py' y el tipo 'Avistamiento' en un módulo 'avistamientos.py'


```python
# Creación de una tupla con nombre para las coordenadas
Coordenadas = NamedTuple('Coordenadas', [
    ('latitud', float), ('longitud', float)
])

# Creación de una tupla con nombre para los avistamientos
Avistamiento = NamedTuple('Avistamiento', [
    ('fechahora', datetime),
    ('ciudad', str),
    ('estado', str),
    ('forma', str),
    ('duracion', int),
    ('comentarios', str),
    ('ubicacion', Coordenadas)
])

def lee_avistamientos(fichero:str)->list[Avistamiento]:
    '''
    Lee un fichero de entrada y devuelve una lista de tuplas. 
    Para convertir la cadena con la fecha y la hora al tipo datetime, usar
        datetime.strptime(fecha_hora,'%m/%d/%Y %H:%M'). Define una funcion parse_fecha en un módulo parsers para parsear la fecha.    
    
    :param fichero: ruta del fichero csv que contiene los datos en codificación utf-8 
    :return: lista de tuplas con la información de los avistamientos 
    '''
    pass
```

El resultado de leer los cinco primeros avistamientos debe ser: 
 ```python
# Test de la función lee_avistamientos (incluye este trozo de código en una función de test en el módulo avistamientos_test)
avistamientos = lee_avistamientos('../data/ovnis.csv')
print(avistamientos[:5])
```
```
    [Avistamiento(fechahora=datetime.datetime(2011, 7, 4, 22, 0), ciudad='muncie', estado='in', forma='light', duracion=240, comentarios='((HOAX??))  4th  of July ufo and a image of a ghostly alien face very disturbing.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889)), Avistamiento(fechahora=datetime.datetime(2005, 4, 7, 17, 1), ciudad='deming (somewhere near)', estado='nm', forma='changing', duracion=1200, comentarios='((NUFORC Note:  Helium-filled heliostat.  PD)) The shape-shifting object danced around at various speed  height and direction.', ubicacion=Coordenadas(latitud=32.2686111, longitud=-107.7580556)), Avistamiento(fechahora=datetime.datetime(2010, 3, 12, 19, 56), ciudad='erie', estado='pa', forma='changing', duracion=300, comentarios='3/12/10Viewed a comet like object very bright fall out of the sky about 1 mile.', ubicacion=Coordenadas(latitud=42.1291667, longitud=-80.0852778)), Avistamiento(fechahora=datetime.datetime(2013, 7, 4, 22, 25), ciudad='seattle', estado='wa', forma='unknown', duracion=600, comentarios='A RED Light was seen over the Highland Park area of Seattle (((Drone?))).', ubicacion=Coordenadas(latitud=47.6063889, longitud=-122.3308333)), Avistamiento(fechahora=datetime.datetime(2003, 9, 9, 0, 40), ciudad='clearwater', estado='fl', forma='triangle', duracion=120, comentarios='bright light to east split to 3 triangle 1 hovered and 2 dropped.  ((NUFORC Note:  Titan 4 launch from Cape Canaveral.  PD))', ubicacion=Coordenadas(latitud=27.9655556, longitud=-82.8002778))]
 ```   

Una vez leídos los datos, vamos a realizar diversas operaciones con ellos. Dividiremos estas operaciones en tres bloques.

## 2. Operaciones de filtrado, conteo y suma

### 2.1 Número de avistamientos producidos en una fecha

Función que obtiene el número total de avistamientos que se han producido en una fecha determinada, dada por su día, mes y año. Se contarán, por tanto, los avistamientos que hayan tenido lugar a cualquier hora del día.

Vamos a implementar esta función tanto con bucles, como usando una definición por compresión.


```python
def numero_avistamientos_fecha(avistamientos: list[Avistamiento], fecha: datetime.date)->int:
    ''' Avistamientos que se han producido en una fecha
    
    Toma como entrada una lista de avistamientos y una fecha.
    Devuelve el número de avistamientos que se han producido en esa fecha.

    :param avistamientos: lista de avistamientos
    :param fecha: fecha del avistamiento 
    :return:  Número de avistamientos producidos en la fecha 
    '''
    # Implementación con bucles
    pass 
```


```python
def numero_avistamientos_fecha2(avistamientos: list[Avistamiento], fecha: datetime.date)->int:
    #Implementación usando una defición por compresión
    pass
```


```python
# Test de la función numero_avistamientos_fecha (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)

fecha = datetime(2005, 5, 1).date()
numero_avistamientos = numero_avistamientos_fecha(avistamientos, fecha)
fecha_str=datetime.strftime(fecha, '%d/%m/%Y')
print(f"El día {fecha_str} se produjeron {numero_avistamientos} avistamientos")
```
```
    El día 01/05/2005 se produjeron 5 avistamientos
```    

### 2.2 Número de formas observadas en un conjunto de estados

Función que obtiene el número de formas distintas que presentaron los avistamientos observados en uno o varios estados. Implementa dos versiones de esta función, una usando bucles, y otra usando definiciones por compresión.


```python
def formas_estados(avistamientos:list[Avistamiento], estados:set[str])->int:
    ''' 
    Devuelve el número de formas distintas observadas en avistamientos 
    producidos en alguno de los estados especificados.
    :param avistamientos: lista de tuplas con la información de los avistamientos
    :param estados: conjunto de estados para los que se quiere hacer el cálculo 
    :return: Número de formas distintas observadas en los avistamientos producidos en alguno de los estados indicados por el parámetro "estados"
    '''
    #Implementación con bucles
    pass
```


```python
def formas_estados2(avistamientos:list[Avistamiento], estados:set[str])->int:
    # Por comprensión
    pass
```


```python
# Test de la función formas_estados incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test
conjunto_estados = {'in', 'nm', 'pa', 'wa'}
estados_str= ', '.join(conjunto_estados)
formas = formas_estados(avistamientos, conjunto_estados)
print(f"Número de formas distintas observadas en los estados {estados_str}: {formas}")

```
El resultado del test debe ser:
```
    Número de formas distintas observadas en los estados nm, in, pa, wa: 23
````    

### 2.3 Duración total de los avistamientos en un estado

Función que devuelve la duración total en segundos de los avistamientos que se han observado en un estado. Implementa una versión con bucles, y otra usando una definició por compresión.


```python
def duracion_total(avistamientos:list[Avistamiento], estado:str)->int:
    ''' 
    Devuelve la duración total de los avistamientos de un estado. 
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param estado: estado para el que se quiere hacer el cálculo
    :return: duración total en segundos de todos los avistamientos del estado 
    '''
    # Implementación con bucles
    pass
```


```python
def duracion_total2(avistamientos:list[Avistamiento], estado:str)->int:
    ## Por compresión
    pass
```


```python
# Test de la función duracion_total incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test
for estado in ['in', 'nm', 'pa', 'wa']:
    duracion = duracion_total(avistamientos, estado)
    print(f"Duración total de los avistamientos en {estado}: {duracion} segundos.")
```
El resultado del test debe ser:
```
    Duración total de los avistamientos en in: 3318305 segundos.
    Duración total de los avistamientos en nm: 3211887 segundos.
    Duración total de los avistamientos en pa: 1241235 segundos.
    Duración total de los avistamientos en wa: 1822712 segundos.
```    

### 2.4 Avistamientos cercanos a una ubicación

Función que calcula un conjunto con los avistamientos cercanos a una ubicacion dada. Concretamente, vamos a obtener los avistamientos que se encuentren dentro de un determinado radio de distancia de la ubicación.

Para calcular distancias terrestres, se utiliza la distancia harvesine, en lugar de la distancia euclídea, ya que hay que tener en cuenta la curvatura de la tierra. La [distancia haversine](https://en.wikipedia.org/wiki/Haversine_formula) entre dos puntos, con coordenadas en radianes $(lat1, lon1)$ y $(lat2, lon2)$, se calcula con la siguiente fórmula, donde $R$ es el radio de la tierra en kilómetros, cuyo valor es $6371$. 

$Δlat = lat2− lat1$

$Δlon = lon2− lon1$

$a = sin²(Δlat/2) + cos(lat1) · cos(lat2) · sin²(Δlon/2)$

$d = 2 · R · asin(\sqrt {a})$


Como las coordenadas en nuestro dataset vienen en grados y el cálculo de la distancia Haversine requiere que las coordenadas estén en radianes, vamos a definir una función auxiliar que permita la conversión a radianes de unas coordenadas en grados.


```python
# Implementa esta función en el módulo coordenadas.py
def a_radianes(coordenadas:Coordenadas)->Coordenadas:
    '''Convierte unas coordenadas en grados a radianes

    :param coordenadas: Coordenadas que se quieren convertir a radianes
    :return: Las coordenadas convertidas a radianes
    '''
    pass

```

También definimos la función auxiliar que calcula la distancia Haversine y usamos la función anterior para convertir las coordenadas.


```python
# Función auxiliar para el cálculo de la distancia entre dos coordenadas
# Implementa esta función en el módulo coordenadas.py
def distancia_haversine(coordenadas1:Coordenadas, coordenadas2:Coordenadas)->float:
    '''Devuelve la distancia de harvesine entre dos coordenadas

    :param coordenadas1: Coordenadas del primer punto
    :param coordenadas2: Coordenadas del segundo punto
    :return: La distancia harvesine entre las dos coordenadas dadas como parámetro
    '''
    pass
```

Ahora usamos esta función para calcular la distancia de cada avistamiento a la ubicación, y nos quedamos con aquellos que estén situados dentro de un radio de distancia $radio$ de la ubicación. Implementa dos versiones de la función, una con bucles y otra usando una definición por compresión.


```python
def avistamientos_cercanos_ubicacion(avistamientos:list[Avistamiento], ubicacion:Coordenadas, radio:float)->set[Avistamiento]:
    ''' 
    Devuelve el conjunto de avistamientos cercanos a una ubicación.
    :param avistamientos: lista de tuplas con la información de los avistamientos
    :param ubicacion: coordenadas de la ubicación para la cual queremos encontrar avistamientos cercanos 
    :param radio: radio de distancia
    :return:Conjunto de avistamientos que se encuentran a una distancia
         inferior al valor "radio" de la ubicación dada por el parámetro "ubicacion" 
    '''
    #Implementación con bucles
    pass
```

```python
def avistamientos_cercanos_ubicacion2(avistamientos:list[Avistamiento], ubicacion:Coordenadas, radio:float)->set[Avistamiento]:
    # Por compresión
    pass

```


```python
# Test de la función avistamientos_cercanos_ubicacion (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
coordenadas = Coordenadas(40.1933333,-85.3863889)
radio = 0.5     
conjunto_av_cercanos = avistamientos_cercanos_ubicacion(avistamientos, coordenadas, radio)
print(f"Avistamientos cercanos a ({coordenadas.latitud}, {coordenadas.longitud}): {len(conjunto_av_cercanos)}" )
for ind, av in enumerate(conjunto_av_cercanos, 1):
    print(f"{ind} -{conjunto_av_cercanos}")
```
El resultado del test debería ser:
```
 Avistamientos cercanos a (40.1933333, -85.3863889):
	1-Avistamiento(fechahora=datetime.datetime(2007, 6, 20, 22, 30), ciudad='muncie', estado='in', forma='triangle', duracion=120, comentarios='Black triangle with 2 bright white lights on back 2 points floated by  no sound.  paused lights turned to orange  craft disappeared', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	2-Avistamiento(fechahora=datetime.datetime(2002, 5, 21, 22, 0), ciudad='muncie', estado='in', forma='changing', duracion=360, comentarios='It was the shape of a brihgte star than it Kinda turned recktangular shape and started flying. The center was rad and the ends yellow.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	3-Avistamiento(fechahora=datetime.datetime(2011, 12, 2, 23, 0), ciudad='muncie', estado='in', forma='fireball', duracion=3600, comentarios='1 orb hovering in sky and exploding in a ball of blue light before disappearing.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	4-Avistamiento(fechahora=datetime.datetime(2010, 11, 8, 23, 30), ciudad='muncie', estado='in', forma='light', duracion=2700, comentarios='Strobing Star like objects in the sky being observed by aircraft', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	5-Avistamiento(fechahora=datetime.datetime(1958, 7, 1, 21, 0), ciudad='muncie', estado='in', forma='unknown', duracion=300, comentarios='A star sized object circled the sky and then shot straight out of sight at very great speed.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	6-Avistamiento(fechahora=datetime.datetime(2012, 9, 26, 20, 40), ciudad='muncie', estado='in', forma='circle', duracion=300, comentarios='Glowing Fire Colored Orb in the Sky', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	7-Avistamiento(fechahora=datetime.datetime(2009, 9, 1, 22, 0), ciudad='muncie', estado='in', forma='sphere', duracion=300, comentarios='Bright orange light in the northwest sky near the Muncie airport.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	8-Avistamiento(fechahora=datetime.datetime(2011, 7, 4, 22, 0), ciudad='muncie', estado='in', forma='light', duracion=180, comentarios='saw glowing orange ball of light and ghostly face', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	9-Avistamiento(fechahora=datetime.datetime(2011, 7, 4, 22, 0), ciudad='muncie', estado='in', forma='light', duracion=240, comentarios='((HOAX??))  4th  of July ufo and a image of a ghostly alien face very disturbing.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
	10-Avistamiento(fechahora=datetime.datetime(2007, 2, 24, 16, 0), ciudad='muncie', estado='in', forma='rectangle', duracion=120, comentarios='((HOAX??))  Red  Rectangle object at constant speed that could not be described as a known thing in the air.', ubicacion=Coordenadas(latitud=40.1933333, longitud=-85.3863889))
```    

## 3 Operaciones con máximos, mínimos y ordenación

### 3.1 Avistamiento de una forma con mayor duración

Función que obtiene el avistamiento de mayor duración de entre todos los avistamientos que tienen una forma determinada. Implemente la función usando un bucle y usando una definición por compresión.


```python
def avistamiento_mayor_duracion(avistamientos: list[Avistamiento], forma:str)->Avistamiento:
    '''
    Devuelve el avistamiento de mayor duración de entre todos los
    avistamientos de una forma dada.
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param forma: forma del avistamiento 
    :return:  avistamiento más largo de la forma dada
    '''
    #Implementación con bucles
    pass
```


```python
def avistamiento_mayor_duracion2(avistamientos: list[Avistamiento], forma:str)->Avistamiento:
    # Por comprension
    pass
                
```


```python
# Test de la función avistamiento_mayor_duracion (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
forma = 'circle'
av_mayor_d=avistamiento_mayor_duracion(avistamientos, forma)
print(f"Avistamiento de forma \'{forma}\' de mayor duración: {av_mayor_d}")
```
El resultado del test debe ser:
```
    Avistamiento de forma 'circle' de mayor duración: Avistamiento(fechahora=datetime.datetime(1984, 3, 15, 20, 0), ciudad='griffin', estado='ga', forma='circle', duracion=7894800, comentarios='7 large yellow lights with red center  estimated by distance to be at least 400 feet across  seen form top of hill just above tree line', ubicacion=Coordenadas(latitud=33.2466667, longitud=-84.2641667))
```    

### 3.2 Avistamiento cercano a un punto con mayor duración

Función que devuelve el avistamiento que más tiempo ha durado de aquellos situados dentro de un radio de distancia de una ubicación dada; es decir, la distancia entre la ubicación del avistamiento y las coordenadas que se pasan como parámetro de entrada debe ser menor al radio que también aparece como parámetro de la función. El resultado debe ser una tupla de la forma (duración, comentarios). Implementa la función usando bucles y con definiciones por compresión.


```python
def avistamiento_cercano_mayor_duracion(avistamientos:list[Avistamiento], coordenadas:Coordenadas, radio:float=0.5)->tuple[int, str]:
    '''
    Devuelve la duración y los comentarios del avistamiento que más 
    tiempo ha durado de aquellos situados en el entorno de las
    coordenadas que se pasan como parámetro de entrada.
    El resultado debe ser una tupla de la forma (duración, comentarios)
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param coordenadas: tupla con latitud y longitud
    :param radio: radio de búsqueda
    :return: duración y comentarios del avistamiento más largo en el entorno de las coordenadas comentarios del avistamiento más largo
    '''
    #Con bucles
    pass
```


```python
def avistamiento_cercano_mayor_duracion2(avistamientos:list[Avistamiento], coordenadas:Coordenadas, radio:float=0.5)->tuple[int, str]:
    # Por comprensión
    pass
```


```python
# Test de la función avistamiento_cercano_mayor_duracion (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
coordenadas = Coordenadas(40.19,-85.38)
radio = 0.5
duracion, comentario = avistamiento_cercano_mayor_duracion(avistamientos, coordenadas)
print(f"Duración del avistamiento más largo en un entorno de radio {radio} sobre las coordenadas ({coordenadas.latitud},{coordenadas.longitud}): {duracion} segundos")
print("Comentario:", comentario)
```
El resultado del test debe ser:
```
    Duración del avistamiento más largo en un entorno de radio 0.5 sobre las coordenadas (40.1933333, -85.3863889): 3600
    Comentario: 1 orb hovering in sky and exploding in a ball of blue light before disappearing.
```    

### 3.3 Avistamientos producidos entre dos fechas

Función que devuelve una lista con los avistamientos observados entre una fecha inicial y una fecha final, ambas inclusive. La lista devuelta estará ordenada de los avistamientos más recientes a los más antiguos. Si la fecha inicial es None, se devolverán todos los avistamientos desde el más antiguo hasta la fecha final. Si la fecha final es None, se devolverán todos los avistamientos desde la fecha inicial hasta el más reciente. Si ambas fechas son None, se devolverá la lista de avistamientos completa. Usa definiciones por compresión para resolver el ejercicio.


```python
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
    :return: lista de tuplas con la información de los avistamientos en el rango de fechas
    '''
    pass
```


```python
# Test de la función avistamientos_fechas (incluye este trozo de código en una función de test e invcoa a la función de test con los distintos valores de los parámetros)
avistamientos_fec = avistamientos_fechas(avistamientos,
                                         datetime(2005,5,1).date(), datetime(2005,5,1).date())
print("Mostrando los avistamientos entre el 1 de mayo de 2005 y el 1 de mayo de 2005: ")
for a in avistamientos_fec:
    print("\t", a)
    
print(f"\tTotal: {len(avistamientos_fec)} avistamientos.")
avistamientos_hasta_mayo = avistamientos_fechas(avistamientos,
                                       fecha_final=datetime(2005,5,1).date())
print(f"Avistamientos hasta el 1 de mayo de 2005: {len(avistamientos_hasta_mayo)} avistamientos")
avistamientos_desde_mayo = avistamientos_fechas(avistamientos,
                                       fecha_inicial=datetime(2005,5,1).date())
print(f"Avistamientos desde el 1 de mayo de 2005: {len(avistamientos_desde_mayo)} avistamientos")
```
El resultado del test debe ser:
```
    Mostrando los avistamientos entre el 1 de mayo de 2005 y el 1 de mayo de 2005: 
    	 Avistamiento(fechahora=datetime.datetime(2005, 5, 1, 23, 0), ciudad='palmdale', estado='ca', forma='sphere', duracion=300, comentarios='dancing light above lancaster', ubicacion=Coordenadas(latitud=34.5794444, longitud=-118.1155556))
    	 Avistamiento(fechahora=datetime.datetime(2005, 5, 1, 16, 11), ciudad='fallbrook', estado='ca', forma='changing', duracion=30, comentarios='Huge bright liigt', ubicacion=Coordenadas(latitud=33.3763889, longitud=-117.2502778))
    	 Avistamiento(fechahora=datetime.datetime(2005, 5, 1, 6, 20), ciudad='independence', estado='ky', forma='other', duracion=300, comentarios='stationary disk-like object seen near I-75/Independence  KY', ubicacion=Coordenadas(latitud=38.9430556, longitud=-84.5441667))
    	 Avistamiento(fechahora=datetime.datetime(2005, 5, 1, 1, 0), ciudad='portland', estado='or', forma='oval', duracion=420, comentarios='Three amber/orange objects patrol Portland skyline', ubicacion=Coordenadas(latitud=45.5236111, longitud=-122.675))
    	 Avistamiento(fechahora=datetime.datetime(2005, 5, 1, 1, 0), ciudad='portland', estado='or', forma='disk', duracion=300, comentarios='Orange disk-like orbs over Downtown Portland.  ((NUFORC Note:  Student report.  PD))', ubicacion=Coordenadas(latitud=45.5236111, longitud=-122.675))
    	Total: 5 avistamientos.
    Avistamientos hasta el 1 de mayo de 2005: 12639 avistamientos
    Avistamientos desde el 1 de mayo de 2005: 19048 avistamientos
```    

### 3.4 Avistamiento de un año con el comentario más largo

Función que devuelve el avistamiento con el comentario más largo, de entre todos los avistamientos observados en un año dado y cuyo comentario incluye una palabra concreta. Resuelve este ejercicio con bucles y usando definiciones por compresión.


```python
def comentario_mas_largo(avistamientos:list[Avistamiento], anyo:int, palabra:str)->Avistamiento:
    ''' 
    Devuelve el avistamiento cuyo comentario es el más largo, de entre
    los avistamientos observados en el año dado por el parámetro "anyo"
    y cuyo comentario incluya la palabra recibida en el parámetro "palabra".
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param anyo: año para el que se hará la búsqueda 
    :param palabra: palabra que debe incluir el comentario del avistamiento buscado 
    :return: avistamiento con el comentario más largo
    '''    
    # Con bucles
    pass
```


```python
def comentario_mas_largo2(avistamientos:list[Avistamiento], anyo:int, palabra:str)->Avistamiento:
    # Por comprensión
    pass

```


```python
# Test de la función comentario_mas_largo (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
print('El avistamiento con el comentario más largo de 2015 incluyendo la palabra "ufo" es:')     
print(comentario_mas_largo(avistamientos, 2005, "ufo"))
```
El resultado del test debe ser:
```
    El avistamiento con el comentario más largo de 2015 incluyendo la palabra "ufo" es:
    Avistamiento(fechahora=datetime.datetime(2005, 6, 15, 12, 0), ciudad='fort myers', estado='fl', forma='disk', duracion=1200, comentarios="hey all you ufo peeps i am only writing this to verify another guys sighting here in swf there here alot ufo's and there disturbing the", ubicacion=Coordenadas(latitud=26.6402778, longitud=-81.8725))
```    

### 3.5 Media de días entre avistamientos consecutivos

Función que devuelve la media de días transcurridos entre dos avistamientos consecutivos en el tiempo. La función permite hacer el cálculo para todos los avistamientos, o solo para los de un año concreto.


```python
def media_dias_entre_avistamientos(avistamientos:list[Avistamiento], anyo:int|None=None)->float|None:
    ''' 
    Devuelve la media de días transcurridos entre dos avistamientos consecutivos.
    Si año es distinto de None, solo se contemplarán los avistamientos del año
    especificado para hacer el cálculo.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 

    :param anyo: año para el que se hará la búsqueda 
    :type anyo: int
    :return: media de días transcurridos entre avistamientos. Si no se puede realizar el cálculo, devuelve None 
    '''    
    pass

```


```python
# Test de la función media_dias_entre_avistamientos (incluye este trozo de código en una función de test con parámetros y prueba con los distintos valores de los parámetros)
print('La media de días entre dos avistamientos consecutivos es:',
      media_dias_entre_avistamientos(avistamientos))
print('La media de días entre dos avistamientos consecutivos del año 1979 es:',
      media_dias_entre_avistamientos(avistamientos, 1979))
```
El resultado del test debe ser:
```
    La media de días entre dos avistamientos consecutivos es: 1.1982576307566049
    La media de días entre dos avistamientos consecutivos del año 1979 es: 4.089887640449438
```    

## 4 Operaciones con diccionarios

### 4.1 Avistamientos por fecha

Función que crea un diccionario que relaciona las fechas con los avistamientos observados en dichas fechas. Es decir, un diccionario cuyas claves son las fechas y cuyos valores son los conjuntos de avistamientos observados en cada fecha. Haz dos implementaciones de esta función, una usando un diccionario y otra usando defaultdict.


```python
def avistamientos_por_fecha(avistamientos:list[Avistamiento])->dict[datetime.date, set[Avistamiento]]:
    ''' 
    Devuelve un diccionario que indexa los avistamientos por fechas
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return diccionario en el que las claves son las fechas de los avistamientos 
         y los valores son conjuntos con los avistamientos observados en esa fecha
    '''
    # Con dict
    pass
```


```python
def avistamientos_por_fecha2(avistamientos:list[Avistamiento])->dict[datetime.date, list[Avistamiento]]:
    # Con defaultdict
    pass
```


```python
# Test de la función avistamientos_por_fecha (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = avistamientos_por_fecha(avistamientos)
print("Avistamientos por fecha (se muestran solo dos fechas):", )
for f in [datetime(1986, 9, 18).date(), datetime(1986, 7, 20).date()]:
    print(f"\t{f}: {indice[f]}") 
```
El resultado del test debe ser:
```
    Avistamientos por fecha (se muestran solo dos fechas):
    	1986-09-18: {Avistamiento(fechahora=datetime.datetime(1986, 9, 18, 16, 0), ciudad='owensboro', estado='ky', forma='cylinder', duracion=180, comentarios='Baton-shaped object moving end-over-end in clear afternoon sky.', ubicacion=Coordenadas(latitud=37.7741667, longitud=-87.1133333))}
    	1986-07-20: {Avistamiento(fechahora=datetime.datetime(1986, 7, 20, 3, 30), ciudad='san marcos', estado='tx', forma='rectangle', duracion=600, comentarios='Was looking at all kinds of sites that came up on the Yahoo web site.  It talked about how people are looking at UFO sites.  It reminde', ubicacion=Coordenadas(latitud=29.8830556, longitud=-97.9411111)), Avistamiento(fechahora=datetime.datetime(1986, 7, 20, 23, 30), ciudad='new haven', estado='ct', forma='triangle', duracion=600, comentarios='Black Triangle spotted in CT back in mid-eighties', ubicacion=Coordenadas(latitud=41.3080556, longitud=-72.9286111)), Avistamiento(fechahora=datetime.datetime(1986, 7, 20, 1, 0), ciudad='tucson', estado='az', forma='light', duracion=900, comentarios='Lights and beems over AZ desert', ubicacion=Coordenadas(latitud=32.2216667, longitud=-110.9258333))}
```    

### 4.2 Formas de avistamientos por mes

Función que devuelve un diccionario que indexa las distintas formas de avistamientos por los nombres de los meses en que se observaron. Por ejemplo, para el mes "Enero" se tendrá un conjunto con todas las formas distintas observadas en dicho mes. Implementa una versión con `dict`y otra con `defaultdict`.

_Ayuda_:

Para trabajar con los meses en la configuración que tenga el usuario que está usando el progrma en su ordenador se usa lo que se llama la configuración local. Para ello, en la sección de importaciones importamos el módulo ```locale```, y en la función usamos la siguiente sentencia para indicar que vamos a configurar la fecha y hora a la configuración local del usuario:
```
 locale.setlocale(locale.LC_TIME, '')
``` 
Usa también ```fh.strftime("%B").capitalize()``` para obtener el nombre del mes en el formato local del usuario, y escrito con la primera letra en mayúsculas. ```fh``` debe ser un objeto de tipo ```date``` o ```datetime```.


```python
def formas_por_mes(avistamientos:list[Avistamiento])->dict[str, set[str]]:
    ''' 
    Devuelve un diccionario que indexa las distintas formas de avistamientos
    por los nombres de los meses en que se observan.
    Por ejemplo, para el mes "Enero" se asociará un conjunto con todas las
    formas distintas observadas en dicho mes.
        
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario en el que las claves son los nombres de los meses 
         y los valores son conjuntos con las formas observadas en cada mes
    '''
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    # Con dict
    pass

```


```python
def formas_por_mes2(avistamientos:list[Avistamiento])->dict[str, set[str]]:
    # Con defaultdict    
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    pass
```


```python
# Test de la función formas_por_mes (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = formas_por_mes(avistamientos)
print("Índice de formas por mes (se muestran las formas para enero, julio y noviembre:")
for mes in ["Enero", "Julio", "Noviembre"]:
    print("\t{} ({} formas distintas): {}"
          .format(mes, len(indice[mes]), ', '.join(sorted(indice[mes]))))
```
El resultado del test debe ser:
```
    Índice de formas por mes (se muestran las formas para enero, julio y noviembre:
    	Enero (21 formas distintas): changing, chevron, cigar, circle, cone, cross, cylinder, diamond, disk, egg, fireball, flash, formation, light, other, oval, rectangle, sphere, teardrop, triangle, unknown
    	Julio (22 formas distintas): changing, chevron, cigar, circle, cone, cross, cylinder, delta, diamond, disk, egg, fireball, flash, formation, light, other, oval, rectangle, sphere, teardrop, triangle, unknown
    	Noviembre (23 formas distintas): changing, chevron, cigar, circle, cone, cross, cylinder, delta, diamond, disk, egg, fireball, flash, formation, light, other, oval, rectangle, round, sphere, teardrop, triangle, unknown
```    

### 4.3 Número de avistamientos por año

Función que crea un diccionario que relaciona cada año con el número de avistamientos observados en dicho año. Es decir, un diccionario cuyas claves son los años y cuyos valores son el número de avistamientos observados en cada año. Implementa 3 versiones de esta función: con `dict`, con `Counter` y con `defaultdict`.


```python
def numero_avistamientos_por_año(avistamientos:list[Avistamiento])->dict[int, int]:
    '''
    Devuelve el número de avistamientos observados en cada año.
             
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario en el que las claves son los años
         y los valores son el número de avistamientos observados en ese año
    '''
    # Con dict
    pass
```


```python
def numero_avistamientos_por_año2(avistamientos:list[Avistamiento])->dict[int, int]:
    # Con Counter
    pass
```


```python
def numero_avistamientos_por_año3(avistamientos:list[Avistamiento])->dict[int, int]:
    # Con defaultdict
    num_av_por_anyo = defaultdict(lambda:0)
    pass
```


```python
# Test de la función numero_avistamientos_por_año (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = numero_avistamientos_por_año(avistamientos)
print("Número de avistamientos por año:")
for clave, valor in indice.items():
    print(f"\t{clave}: {valor}")
```
El resultado del test debe ser:
```
    Número de avistamientos por año:
    	2011: 2200
    	2005: 1582
    	2010: 1731
    	2013: 2940
    	2003: 1505
    	2007: 1685
    	1964: 35
    	2004: 1591
    	2014: 978
    	2008: 1978
    	2000: 1072
    	1986: 69
    	1997: 513
    	1983: 48
    	2006: 1450
    	1991: 84
    	1985: 82
    	1999: 1122
    	1990: 98
    	2001: 1214
    	2012: 3139
    	1981: 71
    	2002: 1169
    	1993: 98
    	1994: 167
    	2009: 1790
    	1996: 206
    	1989: 97
    	1984: 70
    	1965: 70
    	1978: 123
    	1971: 38
    	1969: 49
    	1976: 117
    	1998: 704
    	1987: 85
    	1920: 1
    	1966: 76
    	1951: 9
    	1967: 79
    	1961: 18
    	1959: 26
    	1995: 210
    	1992: 94
    	1974: 103
    	1975: 108
    	1979: 90
    	1954: 20
    	1973: 83
    	1945: 4
    	1947: 13
    	1952: 19
    	1955: 7
    	1963: 33
    	1968: 85
    	1970: 40
    	1972: 58
    	1980: 97
    	1957: 30
    	1953: 15
    	1950: 5
    	1958: 21
    	1988: 100
    	1982: 74
    	1960: 24
    	1956: 18
    	1977: 102
    	1937: 2
    	1948: 4
    	1962: 28
    	1946: 4
    	1949: 6
    	1910: 1
    	1939: 1
    	1944: 1
    	1934: 1
    	1936: 1
    	1925: 1
```     

### 4.4 Número de avistamientos por mes del año

Función que devuelve el número de avistamientos observados en cada mes del año. Implementa 3 versiones de esta función: con `dict`, con `Counter` y con `defaultdict`.


```python
def num_avistamientos_por_mes(avistamientos:list[Avistamiento])->dict[int, int]:
    '''
    Devuelve el número de avistamientos observados en cada mes del año.
    
    Usar la expresión .date().month para obtener el número del mes de un objeto datetime.
    
    Usar como claves los nombres de los doce meses con la inicial en mayúsculas:

    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:diccionario en el que las claves son los nombres de los meses y 
         los valores son el número de avistamientos observados en ese mes
    '''
    # Con dict
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')
    pass
```


```python
def num_avistamientos_por_mes2(avistamientos:list[Avistamiento])->dict[int, int]:
    # Con Counter
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')

    pass
```


```python
def num_avistamientos_por_mes3(avistamientos:list[Avistamiento])->dict[int, int]:
    # Con defaultdict
    # Establecemos la configuración local de la hora al formato
    # que esté definido en el ordenador del usuario
    locale.setlocale(locale.LC_TIME, '')
    pass   
```


```python
# Test de la función num_avistamientos_por_mes (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = num_avistamientos_por_mes(avistamientos)
print("Número de avistamientos por mes (sólo se muestran enero, febrero y marzo):")
for mes in ["Enero", "Febrero", "Marzo"]:
    print(f"\t{mes}: {indice[mes]}") 
```
El resultado del test debe ser:
```
    Número de avistamientos por mes (sólo se muestran enero, febrero y marzo):
    	Enero: 2185
    	Febrero: 1825
    	Marzo: 2132
```    

### 4.5 Coordenadas con mayor número de avistamientos

Función que devuelve las coordenadas redondeadas que se corresponden con la zona donde más avistamientos se han observado. Por ejemplo, si hay avistamientos en las coordenadas (40.1, -85.3), (41.13, -85.1) y (40.2, -85.4), la zona con más avistamientos corresponde a las coordenadas (40, -8) con 2 avistamientos. Implementa 3 versiones de esta función: con `dict`, con `Counter` y con `defaultdict`.

Define también una función auxiliar que tome una coordenada y devuelva esa coordenada redondeada. Usa la función 'round' para redondear.


```python
# Añade esta función al módulo coordenadas.py
def redondear(coordenadas:Coordenadas)->Coordenadas:
    '''Devuelve unas coordenadas cuya latitud y longitud son 
    el redondeo de la latitud y la longitud de las coordenadas originales

    :param coordenadas: Coordenadas que se quieren convertir a radianes
    :return: Las coordenadas redondeadas
    '''
    pass
```


```python
def coordenadas_mas_avistamientos(avistamientos:list[Avistamiento])->Coordenadas:
    '''
    Devuelve las coordenadas enteras que se corresponden con 
    la zona donde más avistamientos se han observado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: Coordenadas (sin decimales) que acumulan más avistamientos

    En primer lugar construiremos un diccionario cuyas claves sean las coordenadas 
    enteras obtenidas a partir de las coordenadas de los avistamientos, y
    cuyos valores sean el número de avistamientos observados en esas coordenadas.
    Después obtendremos el máximo de los elementos del diccionario según el valor
    del elemento.
    '''   
    pass
```


```python
def coordenadas_mas_avistamientos2(avistamientos:list[Avistamiento])->Coordenadas:
    #Alternativa con Counter
    pass
```


```python

def coordenadas_mas_avistamientos3(avistamientos:list[Avistamiento])->Coordenadas:
    #Con defaultdict e items para el cálculo del max
    pass
```


```python
# Test de la función coordenadas_mas_avistamientos (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
print("Coordenadas enteras de la región en la que se observaron más avistamientos:", 
      coordenadas_mas_avistamientos(avistamientos))
```
El resultado del test debe ser:
```
    Coordenadas enteras de la región en la que se observaron más avistamientos: Coordenadas(latitud=34, longitud=-118)
```    

### 4.6 Hora del día con mayor número de avistamientos

Función que devuelve la hora del día (de 0 a 23) en la que se han observado un mayor número de avistamientos. Implementa 2 versiones, una con 'dict' y otra con 'Counter'.


```python
def hora_mas_avistamientos(avistamientos:list[Avistamiento])->int:
    ''' 
    Devuelve la hora del día (de 0 a 23) con mayor número de avistamientos
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: hora del día en la que se producen más avistamientos
       
    En primer lugar construiremos un diccionario cuyas claves sean las horas del
    día en las que se han observado avistamientos, y cuyos valores sean el número
    de avistamientos observados en esa hora.
    Después obtendremos el máximo de los elementos del diccionario según el valor
    del elemento.
    '''
    pass
```


```python
def hora_mas_avistamientos2(avistamientos:list[Avistamiento])->int:
    # Alternativa usando Counter
    pass
```


```python
# Test de la función hora_mas_avistamientos (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
print("Hora en la que se han observado más avistamientos:",
      hora_mas_avistamientos(avistamientos))
```
El resultado del test debe ser:
```
    Hora en la que se han observado más avistamientos: 21
```    

### 4.7 Longitud media de los comentarios por estado

Función que devuelve un diccionario en el que las claves son los estados donde se producen los avistamientos, y los valores son la longitud media de los comentarios de los avistamientos observados en cada estado. Define dos funciones auxiliares para implementar la función `agrupa_avistamientos_por_estado` y `longitud_media_comentarios`.


```python
def longitud_media_comentarios_por_estado(avistamientos:list[Avistamiento])->dict[str,float]:
    '''
    Devuelve un diccionario en el que las claves son los estados donde se
    producen los avistamientos y los valores son la longitud media de los
    comentarios de los avistamientos en cada estado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: diccionario que almacena la longitud media de los comentarios (valores) por estado (claves)

            
    En primer lugar creamos un diccionario que agrupe los avistamientos por estado.
    Esto lo hacemos usando una función auxiliar.
    En segundo lugar, creamos un diccionario a partir del primero, en el que se
    calcule la media. Para definir este diccionario usamos una función
    auxiliar que calcule la media de una lista de Avistamientos
    '''
    pass
```


```python
def agrupa_avistamientos_por_estado(avistamientos:list[Avistamiento])->dict[str,list[Avistamiento]]:
    '''Devuelve un diccionario en el que las claves son los estados, 
    y los valores listas de avistamientos de ese estado

    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: Un diccionario con estados y listas de avistamientos de ese estado
    '''
    pass

```


```python
def longitud_media_comentarios(avistamientos:list[Avistamiento])->dict[str,float]:
    '''Dada una lista de avistamientos, devuelve la longitud media de los
    comentarios de esa lista

    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return: La longitud media de los comentarios de la lista
    '''
    pass

```


```python
# Test de la función longitud_media_comentarios_por_estado (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = longitud_media_comentarios_por_estado(avistamientos)
print("Mostrando la media del tamaño de los comentarios de los avistamientos de los estados 'in','nm', 'pa' y 'wa':")
for estado in ['in', 'nm', 'pa', 'wa']:
    print(f"\t{estado}: {indice[estado]}")
```
El resultado del test debe ser:
```
    Mostrando la media del tamaño de los comentarios de los avistamientos de los estados 'in','nm', 'pa' y 'wa':
    	in: 82.87873754152824
    	nm: 79.51461988304094
    	pa: 78.50746268656717
    	wa: 82.73590021691975
```    

### 4.8 Porcentaje de avistamientos por forma

Función que devuelve un diccionario en el que las claves son las formas de los avistamientos, y los valores son el porcentaje de avistamientos de cada forma con respecto al número total de avistamientos. Implementa dos versiones, una con `dict` y otra con `Counter`.


```python
def porc_avistamientos_por_forma(avistamientos:list[Avistamiento])->dict[str,float]:  
    '''
    Devuelve un diccionario en el que las claves son las formas de los
    avistamientos, y los valores los porcentajes de avistamientos con cada forma.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:  diccionario que almacena los porcentajes de avistamientos (valores)
         por forma (claves)
            
    En primer lugar crearemos un diccionario cuyas claves sean las formas
    y cuyos valores sean el número de avistamientos de esa forma.
    Después crearemos un segundo diccionario con las mismas claves y cuyos valores
    resulten de dividir los valores del diccionario anterior por el número
    total de avistamientos, para obtener los porcentajes.
    '''  
    pass
```


```python
def porc_avistamientos_por_forma2(avistamientos:list[Avistamiento])->dict[str,float]:
    # Solución alternativa con Counter
    pass

```


```python
# Test de la función porc_avistamientos_por_forma (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
porcentajes = porc_avistamientos_por_forma(avistamientos)
print("Porcentajes de avistamientos de las distintas formas (sólo se muestran las formas 'changing', 'chevron', 'cigar' y 'circle'):")
for forma in ['changing', 'chevron', 'cigar', 'circle']:
    print(f"\t{forma}: {porcentajes[forma]:.2f}%")
```
El resultado del test debe ser:
```
    Porcentajes de avistamientos de las distintas formas (sólo se muestran las formas 'changing', 'chevron', 'cigar' y 'circle'):
    	changing: 2.47%
    	chevron: 1.29%
    	cigar: 2.59%
    	circle: 9.54%
```    

### 4.9 Avistamientos de mayor duración por estado

Función que devuelve un diccionario que relaciona los estados con los avistamientos de mayor duración observados en dicho estado, ordenados de mayor a menor duración. Si no se indica nada, se obtendrán los tres avistamientos de mayor duración. Implementa dos versiones, una con bucles y otra con definiciones por compresión.

_Ayuda_:
Resusa la función `agrupa_avistamientos_por_estado` definida anteriormente.


```python
def avistamientos_mayor_duracion_por_estado(avistamientos:list[Avistamiento], n:int=3)->dict[str,Avistamiento]:
    '''
    Devuelve un diccionario que almacena los n avistamientos de mayor duración 
    en cada estado, ordenados de mayor a menor duración.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param n: número de avistamientos a almacenar por cada estado 
    :return: diccionario en el que las claves son los estados y los valores son listas con los "n" avistamientos de mayor duración de cada estado, ordenados de mayor a menor duración
            
    En primer lugar crearemos un diccionario de agrupación cuyas claves sean los estados
    y cuyos valores sean listas con los avistamientos observados en ese estado.
    Para ello usamos la función auxiliar que definimos en el apartado 4.7.
    Después crearemos un segundo diccionario cuyas claves sean los estados
    y cuyos valores sean las mismas listas, pero en orden de mayor a menor
    duración y recortadas a "n" elementos.
    '''
    #con bucles
    pass

```


```python
def avistamientos_mayor_duracion_por_estado2(avistamientos:list[Avistamiento], n:int=3)->dict[str,Avistamiento]
    # Usando una definición por compresión
   pass
```


```python
# Test de la función avistamientos_mayor_duracion_por_estado (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = avistamientos_mayor_duracion_por_estado(avistamientos)
print("Mostrando los 3 avistamientos de mayor duración de los estados 'in' y 'nm':")
for estado in ['in', 'nm']:
    print("\t", estado)
    for a in indice[estado]:
        print("\t\t", a)
```
El resultado del test debe ser:
```
    Mostrando los 3 avistamientos de mayor duración de los estados 'in' y 'nm':
    	 in
    		 Avistamiento(fechahora=datetime.datetime(2012, 4, 22, 21, 0), ciudad='cedar lake', estado='in', forma='light', duracion=2631600, comentarios='I have seen the same object in the sky for the past month. It always appears around 21:00pm and usually stays there until 23:00. It mov', ubicacion=Coordenadas(latitud=41.3647222, longitud=-87.4411111))
    		 Avistamiento(fechahora=datetime.datetime(1968, 5, 12, 9, 0), ciudad='valparaiso', estado='in', forma='unknown', duracion=109800, comentarios="1968  Grey Squares in Sky  I'll take you with me cuz you're my friend  9 o'clock past bozo circus noon  scary man  doll burning", ubicacion=Coordenadas(latitud=41.4730556, longitud=-87.0611111))
    		 Avistamiento(fechahora=datetime.datetime(2001, 2, 19, 19, 0), ciudad='carmel', estado='in', forma='light', duracion=37800, comentarios='Carmel  Indiana on US 31.  On several occasions have noticed a bright light to the south west.  Thought it was venus  however  this eve', ubicacion=Coordenadas(latitud=39.9783333, longitud=-86.1180556))
    	 nm
    		 Avistamiento(fechahora=datetime.datetime(2011, 5, 4, 9, 0), ciudad='albuquerque', estado='nm', forma='other', duracion=2102400, comentarios='((HOAX??))  Get the metal out of my body', ubicacion=Coordenadas(latitud=35.0844444, longitud=-106.6505556))
    		 Avistamiento(fechahora=datetime.datetime(1945, 8, 16, 11, 30), ciudad='san antonio', estado='nm', forma='oval', duracion=777600, comentarios="THE CRAFT APPEARED TO HAVE DECENDED AT AN ANGL  SKIDDED OVER A HUNDRED YARDS PUSHING THE DIRT IN FRONT OF IT AND BURIED IT'S SELF", ubicacion=Coordenadas(latitud=33.9177778, longitud=-106.8652778))
    		 Avistamiento(fechahora=datetime.datetime(1997, 3, 20, 13, 0), ciudad='santa fe', estado='nm', forma='triangle', duracion=28800, comentarios='Was MACHINED by ME ((name deleted)) at LOS ALAMOS NATIONAL labs.  Triangle of BERYLIUM METAL.', ubicacion=Coordenadas(latitud=35.6869444, longitud=-105.9372222))
```    

### 4.10 Año con más avistamientos de una forma

Función que devuelve el año en el que se han observado más avistamientos de una forma dada. Implementa dos versiones, una con 'dict' y otra con 'Counter'.


```python
def año_mas_avistamientos_forma(avistamientos:list[Avistamiento], forma:str)->int:
    '''
    Devuelve el año en el que se han observado más avistamientos
    de una forma dada.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param forma: forma del avistamiento 
    :return: año con mayor número de avistamientos de la forma dada
         
    
    En primer lugar se crea un diccionario con filtro cuyas claves sean los años
    y cuyos valores sean el número de avistamientos observados en ese año,
    utilizando la función ya definida numero_avistamientos_por_año.
    Luego, se calcula el máximo del diccionario según los valores.
    '''
    ## Con dict
    pass
```


```python
def año_mas_avistamientos_forma2(avistamientos:list[Avistamiento], forma:str)->int:
    # con Counter
    pass
```


```python
# Test de la función año_mas_avistamientos_forma (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
forma = 'circle'
año = año_mas_avistamientos_forma(avistamientos, forma)
print(f"Año con más avistamientos de tipo '{forma}': {año}")
```
El resultado del test debe ser:
```
    Año con más avistamientos de tipo 'circle': 2013
```    

### 4.11 Estados con mayor número de avistamientos

Función que devuelve una lista con el nombre y el número de avistamientos de los estados con mayor número de avistamientos, ordenados de mayor a menor número de avistamientos. Si no se indica nada, se obtendrán los cinco estados con más avistamientos.


```python
def estados_mas_avistamientos(avistamientos:list[Avistamiento], n:int=5)->list[tuple[str,int]]:
    '''
    Devuelve una lista con los estados en los que se han observado
    más avistamientos, junto con el número de avistamientos,
    ordenados de mayor a menor número de avistamientos.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :type avistamientos: [Avistamiento(datetime, str, str, str, int, str, Coordenadas(float, float))]
    :param n: número de estados a devolver 
    :return: lista con los estados donde se han observado más avistamientos,
         junto con el número de avistamientos, en orden decreciente
         del número de avistamientos y con un máximo de "limite" estados.
           
    En primer lugar crearemos un diccionario cuyas claves sean los estados
    y cuyos valores sean el número de avistamientos observados en ese estado.
    Después crearemos una lista con las claves del diccionario, ordenadas según
    sus respectivos valores en orden decreciente. Finalmente, recortaremos
    esta lista a "limite" elementos.
    '''
    pass
```


```python
# Test de la función estados_mas_avistamientos
estados = estados_mas_avistamientos(avistamientos)
print(f"Estados con más avistamientos, de mayor a menor nº de avistamientos: {estados}")
```

El resultado del test debe ser:

```
Estados con más avistamientos, de mayor a menor nº de avistamientos: [('ca', 4286), ('fl', 1867), ('wa', 1844), ('tx', 1693), ('ny', 1459)]
``` 

### 4.12 Duración total de los avistamientos de cada año en un estado dado

Función que devuelve un diccionario que relaciona cada año con la suma de las duraciones de todos los avistamientos observados durante ese año en un estado dado. Implementa dos versiones, una con `dict` y otra con `defaultdict`.


```python
def duracion_total_avistamientos_año(avistamientos:list[Avistamiento], estado:str)-> dict[int, int]:
    '''
    Devuelve un diccionario que almacena la duración total de los avistamientos 
    en cada año, para un estado dado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :param estado: nombre del estado
    :return: diccionario en el que las claves son los años y los valores son números con la suma de las duraciones de los avistamientos observados ese año en el estado dado.
    Se crea un diccionario con filtro cuyas claves sean los años
    y cuyos valores sean la suma de las duraciones de todos los avistamientos
    observados en ese año.
    '''
    #Con dict
    pass
```


```python
def duracion_total_avistamientos_año2(avistamientos:list[Avistamiento], estado:str)-> dict[int, int]:
    #Con defaultdict
    pass

```


```python
# Test de la función duracion_total_avistamientos_año (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
estado = 'ca'
indice = duracion_total_avistamientos_año(avistamientos, estado)
print("Mostrando la duración total de los avistamientos entre 2000 y 2002:")
for año in [2000, 2001, 2002]:
    print(f"\tAño {año}: {indice[año]/3600} horas")
```
El resultado del test debe ser:
```
    Mostrando la duración total de los avistamientos entre 2000 y 2002:
    	Año 2000: 35.257222222222225 horas
    	Año 2001: 131.24277777777777 horas
    	Año 2002: 37.96055555555556 horas
```    

### 4.13 Fecha del avistamiento más reciente de cada estado

Función que devuelve un diccionario que relaciona cada estado con la fecha del último avistamiento observado en el estado.

_Ayuda_: 
Reutliza la función `agrupa_avistamientos_por_estado` definida anteriormente.


```python
def avistamiento_mas_reciente_por_estado(avistamientos:list[Avistamiento])->dict[str, datetime.datetime]:
    '''
    Devuelve un diccionario que almacena la fecha del último avistamiento
    observado en cada estado.
    
    :param avistamientos: lista de tuplas con la información de los avistamientos 
    :return:  diccionario en el que las claves son los estados y los valores son 
         las fechas del último avistamientos observado en ese estado.
            
    En primer lugar crearemos un diccionario cuyas claves sean los estados
    y cuyos valores sean listas con los avistamientos observados en ese estado.
    Para ello usamos la función auxiliar  definida en el apartado 4.7
    Después crearemos un segundo diccionario cuyas claves sean los estados y
    cuyos valores sean los valores máximos de las listas, según el campo fechahora.
    '''
    pass
```


```python
# Test de la función avistamiento_mas_reciente_estado (incluye este trozo de código en una función de test con parámetros en el módulo avistamientos_test)
indice = avistamiento_mas_reciente_por_estado(avistamientos)
print("Mostrando la fecha del último avistamiento de los estados in' y 'nm':")
for estado in ['in', 'nm']:
    print(f"\tFecha del último avistamiento en '{estado}': {indice[estado]}")
```
El resultado del test debe ser:

```
    Mostrando la fecha del último avistamiento de los estados in' y 'nm':
    	Fecha del último avistamiento en 'in': 2014-04-12 22:23:00
    	Fecha del último avistamiento en 'nm': 2014-04-24 08:45:00
```    
