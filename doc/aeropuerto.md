# Aeropuertos

Autor: José C. Riquelme

Revisores: Jorge García, Toñi Reina

Disponemos de un fichero de texto con la información de los vuelos que salen de un determinado aeropuerto, de forma que cada vuelo ocupa una línea del fichero separándose los campos por comas. Es decir, la típica estructura CSV. Las primeras líneas del fichero son las siguientes:

```python
Madrid,12.37,155,100,IB1123,22,11,2007,1,5
Barcelona,19.56,200,150,VLG256,22,11,2007,1,20
Valencia,2.1,150,150,RYA803,22,11,2007,1,10
Paris,10.0,85,85,UA894,23,11,2007,2,30
Madrid,22.37,155,154,IB2365,23,11,2007,1,10
```
Cada línea del archivo contiene la siguiente información:  
  - __Destino__,  de tipo cadena de caracteres, que representa el destino del vuelo.  
  - __Precio__,  de tipo numérico real, precio del vuelo. 
  - __Número de plazas__, de tipo entero, número de plazas disponibles en el vuelo. 
  - __Número de pasajeros__, de tipo entero, número de pasajeros del vuelo.  
  - __Código del vuelo__, de tipo cadena de caracteres, código del vuelo.  
  - __Día__, de tipo entero, día en que sale el vuelo.
  - __Mes__, de tipo entero, mes en que sale el vuelo.
  - __Año__, de tipo entero, año en que sale el vuelo.
  - __Horas__, de tipo entero, horas que dura el vuelo.
  - __Minutos__, de tipo entero, minutos que dura el vuelo.   

Por ejemplo, la primera línea representa un vuelo cuyo destino es `Madrid`, cuyo precio es 12.37, tiene 155 plazas y 100 pasajeros, su código es `IB1123`, salió el 22/11/2007 y tuvo una duración de 1 hora y 5 minutos.

Implementa los ejercicios de cada parte en un módulo distinto, teniendo en cuenta las consideraciones indicadas en cada parte.

## Parte 0: NamedTuple y lectura de fichero

Implementa los siguientes ejercicios en el módulo `vuelos.py` y sus test en el módulo `vuelos_test.py`.

__Ejercicio 1__. Defina una estructura NamedTuple para guardar en una tupla los valores de cada línea del fichero. Use el tipo `datetime` para trabajar con las fechas y el tipo `timedelta` para trabajar con las duraciones.

__Ejercicio 2__. 
Defina una función `lee_vuelos` que recibe el nombre de un fichero con una estructura como la descrita y devuelve una lista de tuplas de tipo `Vuelo` con la información leída del fichero.

_Resultados esperados_
```python
Se han leido 43 vuelos
Los tres primeros son
        Vuelo(destino='Madrid', precio=12.37, num_plazas=155, num_pasajeros=100, codigo='IB1123', fecha=datetime.date(2007, 11, 22), duracion=datetime.timedelta(seconds=3900))
        Vuelo(destino='Barcelona', precio=19.56, num_plazas=200, num_pasajeros=150, codigo='VLG256', fecha=datetime.date(2007, 11, 22), duracion=datetime.timedelta(seconds=4800))
        Vuelo(destino='Valencia', precio=2.1, num_plazas=150, num_pasajeros=150, codigo='RYA803', fecha=datetime.date(2007, 11, 22), duracion=datetime.timedelta(seconds=4200))
Los tres últimos son
        Vuelo(destino='Winnipeg', precio=30.0, num_plazas=90, num_pasajeros=70, codigo='IB123', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=27000))
        Vuelo(destino='Quebec', precio=20.0, num_plazas=80, num_pasajeros=60, codigo='EAS678', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=31500))
        Vuelo(destino='Edmonton', precio=10.0, num_plazas=70, num_pasajeros=50, codigo='VLG098', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=32400))
```

## Parte 1: Tratamientos secuenciales

Implementa una función por cada ejercicio en el módulo `vuelos01.py` y sus test en el módulo `vuelos01_test.py`. Haz dos implementaciones por cada ejercicio, una usando bucles y los esquemas de tratamientos secuenciales vistos en clase, y otra usando definiciones por compresión.

__Ejercicio 3__. 
`codigos_vuelos_completos`: Dada una lista de tuplas de tipo `Vuelo`, devuelve una lista con los códigos de los vuelos que están completos.

_Resultados esperados_
```python
codigos_vuelos_completos
    ['RYA803', 'UA894', 'VLG127', 'AIF389', 'RYA212', 'UA894', 'EAS348', 'AIF389', 'UA7810']        
```

__Ejercicio 4__. 
`vuelos_a_destino`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve una lista con los códigos y las fechas de los vuelos que vayan a ese destino.

_Resultados esperados_
```python
vuelos_a_destino -> Madrid
        ('IB1123', datetime.date(2007, 11, 22))
        ('IB2365', datetime.date(2007, 11, 23))
        ('AIF389', datetime.date(2007, 11, 24))
        ('IB1123', datetime.date(2007, 11, 24))
        ('IB2365', datetime.date(2007, 11, 25))
        ('AIF389', datetime.date(2007, 11, 26))
vuelos_a_destino -> Londres
        ('IB6511', datetime.date(2007, 11, 25))
        ('IB6511', datetime.date(2007, 11, 26))
```

__Ejercicio 5__. 
`destinos_de_fecha`: Dadas una lista de tuplas de tipo `Vuelo` y una fecha, devuelve los distintos destinos de los vuelos del aeropuerto en esa fecha.

_Resultados esperados_
```python
destinos_de_fecha -> 2007-11-22
  ['Madrid', 'Barcelona', 'Valencia']
destinos_de_fecha -> 2007-12-01
  ['Boston', 'Chicago', 'Dallas', 'Toronto', 'Vancouver']
```
__Ejercicio 6__. 
`total_plazas_libres_a_destino`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve el número de plazas libres en los vuelos a ese destino.

_Resultados esperados_
```python
total_plazas_libres_a_destino -> Madrid
        Total plazas libres: 82
total_plazas_libres_a_destino -> Londres
        Total plazas libres: 30
```

__Ejercicio 7__. 
`duracion_vuelos_fecha`: Dados una lista de tuplas de tipo `Vuelo` y una fecha, devuelve la duración total de los vuelos de esa fecha.

_Resultados esperados_
```python
duracion_vuelos_fecha -> 2007-11-22
        Duración total: 3:35:00
duracion_vuelos_fecha -> 2007-12-01
        Duración total: 1 day, 16:30:00
```

__Ejercicio 8__. 
`recaudacion_total_destino`: Dados una lista de tuplas de tipo `Vuelo`y un destino, devuelve la recaudación total a ese destino.

_Resultados esperados_
```python
recaudacion_total_destino -> Madrid
        Recaudación total: 27468.359999999997
recaudacion_total_destino -> Londres
        Recaudación total: 5202.0
```

__Ejercicio 9__. 
`precio_medio_destino`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve el precio medio de los vuelos a ese destino.

_Resultados esperados_
```python
precio_medio_destino -> Madrid
        Precio medio: 24.036666666666665
precio_medio_destino -> Londres
        Precio medio: 28.9
```

__Ejercicio 10__. 
`num_vuelos_anteriores_a`: Dadas una lista de tuplas de tipo `Vuelo`y una fecha, devuelve el número de vuelos anteriores a esa fecha.

_Resultados esperados_
```python
num_vuelos_anteriores_a -> 2007-11-23
        Número vuelos: 3
num_vuelos_anteriores_a -> 2007-12-01
        Número vuelos: 24
```

__Ejercicio 11__. 
`existe_vuelo_overbooking`: Dada una lista de tuplas de tipo `Vuelo`, devuelve cierto si existe algún vuelo con _overbooking_ (tiene más pasajeros que plazas) y falso en caso contrario. 

_Resultados esperados_
```python
existe_vuelo_overbooking
        Resultado: True
```

__Ejercicio 12__. 
Dados una lista de tuplas de tipo `Vuelo` y un número n, devuelve cierto si todos los vuelos tienen al menos n pasajeros, y falso en caso contrario.

_Resultados esperados_
```python
todos_los_vuelos_tienen_al_menos_n_pasajeros -> 100
        Resultado: False
todos_los_vuelos_tienen_al_menos_n_pasajeros -> 50
        Resultado: True
```

## Parte 2: Máximos/mínimos y ordenaciones

Implementa los siguientes ejercicios en el módulo `vuelos02.py` y sus test en el módulo `vuelos02_test.py`. 

__Ejercicio 14__. 
`vuelos_plazas_libres_a_destino`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve los códigos de los vuelos con plazas libres para ese destino, ordenados de fecha más antigua a más reciente.
_Resultados esperados_
```python
vuelos_plazas_libres_a_destino -> Madrid
         ['IB1123', 'IB2365', 'IB1123', 'IB2365']
vuelos_plazas_libres_a_destino -> Londres
         ['IB6511', 'IB6511']

```

__Ejercicio 15__. 
`destinos_mas_baratos`: Tengo vacaciones a partir de una fecha y no me importa el destino del viaje siempre que el vuelo sea barato (y haya plazas). Dados una lista de tuplas de tipo `Vuelo`, una fecha, y un número entero, n,devuelve una lista con los nombres de los n destinos más baratos de los vuelos a partir de la fecha dada.
_Resultados esperados_
```python
destinos_mas_baratos -> fecha=2007-11-22, n=3
         ['Washington DC', 'Edmonton', 'Valencia']
destinos_mas_baratos -> fecha=2007-12-01, n=3
         ['Washington DC', 'Edmonton', 'San Francisco']
```

__Ejercicio 16__. 
`vuelos_mas_ocupados`:  Dados una lista de tuplas de tipo `Vuelo`y un valor entero n, devuelve una lista con los destinos y el porcentaje de ocupación de los n vuelos con mayor porcentaje de ocupación.
_Resultados esperados_
```python
vuelos_mas_ocupados -> n=5
        ('Paris', 113.33333333333333)
        ('Valencia', 100.0)
        ('Paris', 100.0)
        ('Valencia', 100.0)
        ('Madrid', 100.0)
vuelos_mas_ocupados -> n=10
        ('Paris', 113.33333333333333)
        ('Valencia', 100.0)
        ('Paris', 100.0)
        ('Valencia', 100.0)
        ('Madrid', 100.0)
        ('Paris', 100.0)
        ('Paris', 100.0)
        ('Madrid', 100.0)
        ('Barcelona', 100.0)
        ('Madrid', 99.35483870967742)
```

__Ejercicio 17__. 
`fechas_vuelos_destino`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve las fechas (sin repetir) en las que hay vuelos a ese destino ordenadas de más cercana a más lejana en el tiempo.
_Resultados esperados_
```python
fechas_vuelos_destino -> Paris
         [datetime.date(2007, 11, 23), datetime.date(2007, 11, 24), datetime.date(2007, 11, 25), datetime.date(2007, 11, 26), datetime.date(2007, 11, 27)]
fechas_vuelos_destino -> Madrid
         [datetime.date(2007, 11, 22), datetime.date(2007, 11, 23), datetime.date(2007, 11, 24), datetime.date(2007, 11, 25), datetime.date(2007, 11, 26)]
```

__Ejercicio 18__. 
`vuelos_destino_ordenados`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve una lista de tuplas con la fecha, el código y el precio de los vuelos libres a ese destino ordenados de menor a mayor precio.
_Resultados esperados_
```python
============================================================
vuelos_destino_ordenados -> Madrid
        (datetime.date(2007, 11, 22), 'IB1123', 12.37)
        (datetime.date(2007, 11, 24), 'IB1123', 12.37)
        (datetime.date(2007, 11, 23), 'IB2365', 22.37)
        (datetime.date(2007, 11, 25), 'IB2365', 25.37)
vuelos_destino_ordenados -> Londres
        (datetime.date(2007, 11, 25), 'IB6511', 28.4)
        (datetime.date(2007, 11, 26), 'IB6511', 29.4)
```

__Ejercicio 19__. 
`vuelo_mas_barato_destino`: Dados una lista de tuplas de tipo `Vuelo`, una fecha y un destino, devuelve el vuelo de menor precio a ese destino partir de la fecha.
_Resultados esperados_
```python
vuelo_mas_barato_destino -> fecha=2007-11-22, destino=Madrid
        Vuelo(destino='Madrid', precio=12.37, num_plazas=155, num_pasajeros=100, codigo='IB1123', fecha=datetime.date(2007, 11, 22), duracion=datetime.timedelta(seconds=3900))
vuelo_mas_barato_destino -> fecha=2007-12-01, destino=Londres
        None
```

## Parte 3: Combinaciones de tratamientos secuenciales

Implementa los siguientes ejercicios en el módulo `vuelos03.py` y sus test en el módulo `vuelos03_test.py`. 


__Ejercicio 20__. 
`media_dias_entre_vuelos_destino`: Dados una lista de tuplas de tipo `Vuelo` y un destino, devuelve el número medio de días que transcurren entre dos vuelos a ese destino.

_Resultados esperados_
media_dias_entre_vuelos_destino -->Destino: Madrid
        1.0
media_dias_entre_vuelos_destino -->Destino: Valencia
        1.5
```

__Ejercicio 21__. 
`vuelos_menos_plazas`: Dada una lista de tuplas de tipo `Vuelo`, devuelve una lista con los códigos de todos los vuelos con el mínimo número de plazas[^1].

[^1]: Puede haber empates en el valor mínimo, en cuyo caso se devuelven todos.

_Resultados esperados_
```python
EJERCICIO 21 ============================================================
vuelos_menos_plazas
        ['VLG098']
```

## Parte 4: Esquemas de diccionarios simples

Implementa los siguientes ejercicios en el módulo `vuelos04.py` y sus test en el módulo `vuelos04_test.py`.

__Ejercicio 22__. 
`numero_vuelos_por_fecha`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario que relaciona cada fecha con el número de vuelos de ese día.
_Resultados esperados_
```python
TEST: numero_vuelos_por_fecha
        2007-11-22 -> 3
        2007-11-23 -> 4
        2007-11-24 -> 7
        2007-11-25 -> 5
        2007-11-26 -> 4
        2007-11-27 -> 1
        2007-12-01 -> 5
        2007-12-02 -> 4
        2007-12-03 -> 5
        2007-12-04 -> 5
```

__Ejercicio 23__. 
`total_pasajeros_por_destino`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario que relaciona cada destino con el número de pasajeros a ese destino.
_Resultados esperados_
```python
TEST: total_pasajeros_por_destino
        Barcelona -> 670
        Bilbao -> 330
        Boston -> 170
        Calgary -> 100
        Chicago -> 130
        Dallas -> 150
        Edmonton -> 50
        Halifax -> 80
        Houston -> 140
        Londres -> 180
        Los Angeles -> 130
        Madrid -> 1028
        Miami -> 120
        Montreal -> 110
        New York -> 110
        Ottawa -> 90
        Paris -> 475
        Philadelphia -> 100
        Quebec -> 60
        San Francisco -> 90
        Toronto -> 130
        Valencia -> 490
        Vancouver -> 120
        Washington DC -> 80
        Winnipeg -> 70
```

__Ejercicio 24__. 
`recaudacion_vuelos_por_destino`: Dada una lista de tuplas de tipo `Vuelo`, devuelve un diccionario que relaciona cada destino con la recaudación de los vuelos a ese destino.
_Resultados esperados_
```python
TEST: recaudacion_vuelos_por_destino
        Barcelona -> 22105.20
        Bilbao -> 11554.80
        Boston -> 18700.00
        Calgary -> 6000.00
        Chicago -> 11700.00
        Dallas -> 12000.00
        Edmonton -> 500.00
        Halifax -> 3200.00
        Houston -> 9800.00
        Londres -> 5202.00
        Los Angeles -> 7800.00
        Madrid -> 27468.36
        Miami -> 6000.00
        Montreal -> 7700.00
        New York -> 4400.00
        Ottawa -> 4500.00
        Paris -> 23120.00
        Philadelphia -> 3000.00
        Quebec -> 1200.00
        San Francisco -> 1800.00
        Toronto -> 11700.00
        Valencia -> 8489.00
        Vancouver -> 9600.00
        Washington DC -> 800.00
        Winnipeg -> 2100.00
```

__Ejercicio 25__. 
`codigos_por_destino`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario que relaciona cada destino con la lista de códigos de los vuelos a ese destino.

_Resultados esperados_
```python
TEST: codigos_por_destino
        Barcelona ->['VLG256', 'UA7810', 'VLG256', 'UA7810']
        Bilbao ->['EAS286', 'EAS286']
        Boston ->['RYA123']
        Calgary ->['EAS654']
        Chicago ->['VLG456']
        Dallas ->['IB678']
        Edmonton ->['VLG098']
        Halifax ->['UA456']
        Houston ->['EAS321']
        Londres ->['IB6511', 'IB6511']
        Los Angeles ->['VLG654']
        Madrid ->['IB1123', 'IB2365', 'AIF389', 'IB1123', 'IB2365', 'AIF389']
        Miami ->['UA908']
        Montreal ->['IB987']
        New York ->['IB321']
        Ottawa ->['VLG321']
        Paris ->['UA894', 'EAS348', 'RYA212', 'UA894', 'EAS348', 'RYA212']
        Philadelphia ->['EAS765']
        Quebec ->['EAS678']
        San Francisco ->['VLG987']
        Toronto ->['RYA321']
        Valencia ->['RYA803', 'VLG127', 'RYA803', 'VLG127']
        Vancouver ->['VLG765']
        Washington DC ->['RYA456']
        Winnipeg ->['IB123']
```

__Ejercicio 26__. 
`destinos_por_fecha`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario que relaciona cada fecha con el conjunto de destinos de los vuelos de esa fecha.

_Resultados esperados_
```python
TEST: destinos_por_fecha
        2007-11-22 -> ['Barcelona', 'Madrid', 'Valencia']
        2007-11-23 -> ['Bilbao', 'Madrid', 'Paris']
        2007-11-24 -> ['Barcelona', 'Madrid', 'Paris', 'Valencia']
        2007-11-25 -> ['Londres', 'Madrid', 'Paris', 'Valencia']
        2007-11-26 -> ['Barcelona', 'Londres', 'Madrid', 'Paris']
        2007-11-27 -> ['Paris']
        2007-12-01 -> ['Boston', 'Chicago', 'Dallas', 'Toronto', 'Vancouver']
        2007-12-02 -> ['Calgary', 'Houston', 'Los Angeles', 'Montreal']
        2007-12-03 -> ['Halifax', 'Miami', 'New York', 'Ottawa', 'Philadelphia']       
        2007-12-04 -> ['Edmonton', 'Quebec', 'San Francisco', 'Washington DC', 'Winnipeg']
```

__Ejercicio 27__. 
`precio_medio_por_destino`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario tal que relaciona cada destino con el precio medio de los vuelos a ese destino.
_Resultados esperados_
```python
TEST: precio_medio_por_destino
        Barcelona -> 32.06
        Bilbao -> 34.56
        Boston -> 110.00
        Calgary -> 60.00
        Chicago -> 90.00
        Dallas -> 80.00
        Edmonton -> 10.00
        Halifax -> 40.00
        Houston -> 70.00
        Londres -> 28.90
        Los Angeles -> 60.00
        Madrid -> 24.04
        Miami -> 50.00
        Montreal -> 70.00
        New York -> 40.00
        Ottawa -> 50.00
        Paris -> 50.33
        Philadelphia -> 30.00
        Quebec -> 20.00
        San Francisco -> 20.00
        Toronto -> 90.00
        Valencia -> 19.75
        Vancouver -> 80.00
        Washington DC -> 10.00
        Winnipeg -> 30.00
```


## Parte 5: Máximos/mínimos y ordenaciones con diccionarios

Implementa los siguientes ejercicios en el módulo `vuelos05.py` y sus test en el módulo `vuelos05_test.py`.

__Ejercicio 28__. 
`vuelo_mas_barato_por_destino`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario que relaciona cada destino con el vuelo más barato a ese destino.
_Resultados esperados_
```python
TEST: vuelo_mas_barato_por_destino
        Barcelona: Vuelo(destino='Barcelona', precio=19.56, num_plazas=200, num_pasajeros=170, codigo='VLG256', fecha=datetime.date(2007, 11, 24), duracion=datetime.timedelta(seconds=4800))
        Bilbao: Vuelo(destino='Bilbao', precio=29.56, num_plazas=200, num_pasajeros=150, codigo='EAS286', fecha=datetime.date(2007, 11, 23), duracion=datetime.timedelta(seconds=5100))     
        Boston: Vuelo(destino='Boston', precio=110.0, num_plazas=190, num_pasajeros=170, codigo='RYA123', fecha=datetime.date(2007, 12, 1), duracion=datetime.timedelta(seconds=34200))     
        Calgary: Vuelo(destino='Calgary', precio=60.0, num_plazas=120, num_pasajeros=100, codigo='EAS654', fecha=datetime.date(2007, 12, 2), duracion=datetime.timedelta(seconds=20700))    
        Chicago: Vuelo(destino='Chicago', precio=90.0, num_plazas=140, num_pasajeros=130, codigo='VLG456', fecha=datetime.date(2007, 12, 1), duracion=datetime.timedelta(seconds=31500))    
        Dallas: Vuelo(destino='Dallas', precio=80.0, num_plazas=180, num_pasajeros=150, codigo='IB678', fecha=datetime.date(2007, 12, 1), duracion=datetime.timedelta(seconds=25200))       
        Edmonton: Vuelo(destino='Edmonton', precio=10.0, num_plazas=70, num_pasajeros=50, codigo='VLG098', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=32400))    
        Halifax: Vuelo(destino='Halifax', precio=40.0, num_plazas=100, num_pasajeros=80, codigo='UA456', fecha=datetime.date(2007, 12, 3), duracion=datetime.timedelta(seconds=22500))      
        Houston: Vuelo(destino='Houston', precio=70.0, num_plazas=170, num_pasajeros=140, codigo='EAS321', fecha=datetime.date(2007, 12, 2), duracion=datetime.timedelta(seconds=22500))    
        Londres: Vuelo(destino='Londres', precio=28.4, num_plazas=100, num_pasajeros=90, codigo='IB6511', fecha=datetime.date(2007, 11, 25), duracion=datetime.timedelta(seconds=10200))    
        Los Angeles: Vuelo(destino='Los Angeles', precio=60.0, num_plazas=160, num_pasajeros=130, codigo='VLG654', fecha=datetime.date(2007, 12, 2), duracion=datetime.timedelta(seconds=30600))
        Madrid: Vuelo(destino='Madrid', precio=12.37, num_plazas=155, num_pasajeros=140, codigo='IB1123', fecha=datetime.date(2007, 11, 24), duracion=datetime.timedelta(seconds=3900))     
        Miami: Vuelo(destino='Miami', precio=50.0, num_plazas=150, num_pasajeros=120, codigo='UA908', fecha=datetime.date(2007, 12, 3), duracion=datetime.timedelta(seconds=27900))
        Montreal: Vuelo(destino='Montreal', precio=70.0, num_plazas=130, num_pasajeros=110, codigo='IB987', fecha=datetime.date(2007, 12, 2), duracion=datetime.timedelta(seconds=23400))   
        New York: Vuelo(destino='New York', precio=40.0, num_plazas=140, num_pasajeros=110, codigo='IB321', fecha=datetime.date(2007, 12, 3), duracion=datetime.timedelta(seconds=28800))   
        Ottawa: Vuelo(destino='Ottawa', precio=50.0, num_plazas=110, num_pasajeros=90, codigo='VLG321', fecha=datetime.date(2007, 12, 3), duracion=datetime.timedelta(seconds=25200))       
        Paris: Vuelo(destino='Paris', precio=10.0, num_plazas=85, num_pasajeros=85, codigo='UA894', fecha=datetime.date(2007, 11, 23), duracion=datetime.timedelta(seconds=9000))
        Philadelphia: Vuelo(destino='Philadelphia', precio=30.0, num_plazas=130, num_pasajeros=100, codigo='EAS765', fecha=datetime.date(2007, 12, 3), duracion=datetime.timedelta(seconds=26100))
        Quebec: Vuelo(destino='Quebec', precio=20.0, num_plazas=80, num_pasajeros=60, codigo='EAS678', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=31500))        
        San Francisco: Vuelo(destino='San Francisco', precio=20.0, num_plazas=120, num_pasajeros=90, codigo='VLG987', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=34200))
        Toronto: Vuelo(destino='Toronto', precio=90.0, num_plazas=150, num_pasajeros=130, codigo='RYA321', fecha=datetime.date(2007, 12, 1), duracion=datetime.timedelta(seconds=28800))    
        Valencia: Vuelo(destino='Valencia', precio=2.1, num_plazas=150, num_pasajeros=150, codigo='RYA803', fecha=datetime.date(2007, 11, 22), duracion=datetime.timedelta(seconds=4200))   
        Vancouver: Vuelo(destino='Vancouver', precio=80.0, num_plazas=140, num_pasajeros=120, codigo='VLG765', fecha=datetime.date(2007, 12, 1), duracion=datetime.timedelta(seconds=26100))
        Washington DC: Vuelo(destino='Washington DC', precio=10.0, num_plazas=110, num_pasajeros=80, codigo='RYA456', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=31500))
        Winnipeg: Vuelo(destino='Winnipeg', precio=30.0, num_plazas=90, num_pasajeros=70, codigo='IB123', fecha=datetime.date(2007, 12, 4), duracion=datetime.timedelta(seconds=27000))     
```

__Ejercicio 29__. 
`codigo_vuelo_mas_barato_por_destino`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario que relaciona cada destino con el código del vuelo más barato a ese destino.

_Resultados esperados_
```python
TEST: codigo_vuelo_mas_barato_por_destino
        Barcelona: ('VLG256', 19.56)
        Bilbao: ('EAS286', 29.56)
        Boston: ('RYA123', 110.0)
        Calgary: ('EAS654', 60.0)
        Chicago: ('VLG456', 90.0)
        Dallas: ('IB678', 80.0)
        Edmonton: ('VLG098', 10.0)
        Halifax: ('UA456', 40.0)
        Houston: ('EAS321', 70.0)
        Londres: ('IB6511', 28.4)
        Los Angeles: ('VLG654', 60.0)
        Madrid: ('IB1123', 12.37)
        Miami: ('UA908', 50.0)
        Montreal: ('IB987', 70.0)
        New York: ('IB321', 40.0)
        Ottawa: ('VLG321', 50.0)
        Paris: ('UA894', 10.0)
        Philadelphia: ('EAS765', 30.0)
        Quebec: ('EAS678', 20.0)
        San Francisco: ('VLG987', 20.0)
        Toronto: ('RYA321', 90.0)
        Valencia: ('RYA803', 2.1)
        Vancouver: ('VLG765', 80.0)
        Washington DC: ('RYA456', 10.0)
        Winnipeg: ('IB123', 30.0)
```

__Ejercicio 30__. 
`destino_mas_pasajeros`: Dada una lista de tuplas de tipo `Vuelo` devuelve el destino con mayor número de pasajeros.
_Resultados esperados_
```python
TEST: destino_mas_pasajeros
        Madrid
```

__Ejercicio 31__. 
`destino_mas_vuelos`: Dada una lista de tuplas de tipo `Vuelo` devuelve el destino con mayor número de vuelos.

_Resultados esperados_
```python
TEST: destino_mas_vuelos
        Madrid
```

__Ejercicio 32__. 
`n_destinos_mas_vuelos`: Dados una lista de tuplas de tipo `Vuelo` y un valor entero n, devuelve una lista con los n destinos con más vuelos ordenada de mayor a menor número de vuelos. Tenga en cuenta que n puede tomar el valor None en cuyo caso devolverá la lista de todos los destinos ordenada por número de vuelos

_Resultados esperados_
```python
TEST: n_destinos_mas_vuelos  (n=3)
        ['Madrid', 'Paris', 'Barcelona']

TEST: n_destinos_mas_vuelos  (n=None)
        ['Madrid', 'Barcelona', 'Valencia', 'Paris', 'Bilbao', 'Londres', 'Boston', 'Chicago', 'Dallas', 'Houston', 'Los Angeles', 'Miami', 'New York', 'Philadelphia', 'San Francisco', 'Washington DC', 'Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa', 'Halifax', 'Winnipeg', 'Quebec', 'Edmonton']
```

__Ejercicio 33__. 
`mes_mas_vuelos_destinos_distintos`: Dada una lista de tuplas de tipo `Vuelo`  devuelve el mes en el que hay más vuelos a destinos distintos.

_Resultados esperados_
```python
TEST: mes_mas_vuelos_destinos_distintos
        Resultado:
        12
```

__Ejercicio 34__. 
`destino_mas_viajeros_por_mes`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario en el que las claves sean los meses y como valor el destino con más viajeros de cada mes.

_Resultados esperados_
```python
TEST: destino_mas_viajeros_por_mes
        11: Madrid
        12: Boston
```

__Ejercicio 35__. 
`destinos_mas_n_vuelos_por_mes`: Dados una lista de tuplas de tipo `Vuelo`y un número n, devuelve un diccionario que relaciona cada mes con una lista ordenada alfabéticamente de los distintos destinos en los que haya más de n vuelos ese mes.

_Resultados esperados_
```python
TEST: destinos_mas_n_vuelos_por_mes (n=2)
        11: ['Barcelona', 'Madrid', 'Paris', 'Valencia']
        12: []
```

## Parte 6: Otras combinaciones de tratamientos con diccionarios

Implementa los siguientes ejercicios en el módulo `vuelos06.py` y sus test en el módulo `vuelos06_test.py`.

__Ejercicio 36__. 
`destinos_mas_n_vuelos_por_mes`: Dados una lista de tuplas de tipo `Vuelo` y dos fechas, que pueden ser `None`, devuelve un diccionario que relaciona cada destino con el porcentaje medio de ocupación de los vuelos a ese destino entre esas dos
fechas. Si la primera fecha es `None`, se tendrán en cuenta los vuelos anteriores a la segunda. Si la segunda fecha es `None`, se tendrán en cuenta los vuelos posteriores a la primera y si las dos fechas son `None` no habrá restricción de fechas.
_Resultados esperados_
```python
EJERCICIO 36 ============================================================
TEST: porcentaje_ocupacion_medio_por_destino-->f1: None f2: None
         {'Madrid': 91.25448028673836, 'Barcelona': 83.75, 'Valencia': 94.16666666666666, 'Paris': 100.06944444444444, 'Bilbao': 82.5, 'Londres': 85.9090909090909, 'Boston': 89.47368421052632, 'Chicago': 92.85714285714286, 'Dallas': 83.33333333333333, 'Houston': 82.3529411764706, 'Los Angeles': 81.25, 'Miami': 80.0, 'New York': 78.57142857142857, 'Philadelphia': 76.92307692307692, 'San Francisco': 75.0, 'Washington DC': 72.72727272727273, 'Toronto': 86.66666666666667, 'Vancouver': 85.71428571428571, 'Montreal': 84.61538461538461, 'Calgary': 83.33333333333333, 'Ottawa': 81.81818181818181, 'Halifax': 80.0, 'Winnipeg': 77.77777777777777, 'Quebec': 75.0, 'Edmonton': 71.42857142857143}

TEST: porcentaje_ocupacion_medio_por_destino-->f1: 2020-01-01 f2: 2020-12-31
         {}

TEST: porcentaje_ocupacion_medio_por_destino-->f1: 2020-01-01 f2: None
         {}

TEST: porcentaje_ocupacion_medio_por_destino-->f1: None f2: 2020-12-31
         {'Madrid': 91.25448028673836, 'Barcelona': 83.75, 'Valencia': 94.16666666666666, 'Paris': 100.06944444444444, 'Bilbao': 82.5, 'Londres': 85.9090909090909, 'Boston': 89.47368421052632, 'Chicago': 92.85714285714286, 'Dallas': 83.33333333333333, 'Houston': 82.3529411764706, 'Los Angeles': 81.25, 'Miami': 80.0, 'New York': 78.57142857142857, 'Philadelphia': 76.92307692307692, 'San Francisco': 75.0, 'Washington DC': 72.72727272727273, 'Toronto': 86.66666666666667, 'Vancouver': 85.71428571428571, 'Montreal': 84.61538461538461, 'Calgary': 83.33333333333333, 'Ottawa': 81.81818181818181, 'Halifax': 80.0, 'Winnipeg': 77.77777777777777, 'Quebec': 75.0, 'Edmonton': 71.42857142857143}
```

__Ejercicio 37__. 
`precio_medio_pasajeros_por_mes_anyo`: Dada una lista de tuplas de tipo `Vuelo` devuelve un diccionario tal que a cada mes-año como clave
le haga corresponder el precio medio de los vuelos y el número de pasajeros total. Las claves serán cadenas de texto formadas por el mes, un guion y el año (por ejemplo, 10-2017). Los valores del diccionario serán tuplas formadas por dos elementos: media del precio de los vuelos y el número total de pasajeros.

_Resultados esperados_
```python
TEST: precio_medio_pasajeros_por_mes_anyo
          11-2007: (32.51583333333333, 3173)
          12-2007: (53.1578947368421, 2030)
```

__Ejercicio 38__. 
`n_codigos_menor_ocupacion_por_mes`: Dados una lista de tuplas de tipo `Vuelo` y un número entero n, devuelve un diccionario tal que a cada destino le
hace corresponder una lista con los n códigos de vuelo de menor ocupación.
_Resultados esperados_
```python

EJERCICIO 38 ============================================================
TEST: n_codigos_menor_ocupacion_por_destino--> n=3
          Barcelona: ['VLG256', 'UA7810', 'VLG256']
          Bilbao: ['EAS286', 'EAS286']
          Boston: ['RYA123']
          Calgary: ['EAS654']
          Chicago: ['VLG456']
          Dallas: ['IB678']
          Edmonton: ['VLG098']
          Halifax: ['UA456']
          Houston: ['EAS321']
          Londres: ['IB6511', 'IB6511']
          Los Angeles: ['VLG654']
          Madrid: ['IB1123', 'IB1123', 'IB2365']
          Miami: ['UA908']
          Montreal: ['IB987']
          New York: ['IB321']
          Ottawa: ['VLG321']
          Paris: ['EAS348', 'RYA212', 'UA894']
          Philadelphia: ['EAS765']
          Quebec: ['EAS678']
          San Francisco: ['VLG987']
          Toronto: ['RYA321']
          Valencia: ['VLG127', 'RYA803', 'RYA803']
          Vancouver: ['VLG765']
          Washington DC: ['RYA456']
          Winnipeg: ['IB123']

TEST: n_codigos_menor_ocupacion_por_destino--> n=5
          Barcelona: ['VLG256', 'UA7810', 'VLG256', 'UA7810']
          Bilbao: ['EAS286', 'EAS286']
          Boston: ['RYA123']
          Calgary: ['EAS654']
          Chicago: ['VLG456']
          Dallas: ['IB678']
          Edmonton: ['VLG098']
          Halifax: ['UA456']
          Houston: ['EAS321']
          Londres: ['IB6511', 'IB6511']
          Los Angeles: ['VLG654']
          Madrid: ['IB1123', 'IB1123', 'IB2365', 'IB2365', 'AIF389']
          Miami: ['UA908']
          Montreal: ['IB987']
          New York: ['IB321']
          Ottawa: ['VLG321']
          Paris: ['EAS348', 'RYA212', 'UA894', 'RYA212', 'UA894']
          Philadelphia: ['EAS765']
          Quebec: ['EAS678']
          San Francisco: ['VLG987']
          Toronto: ['RYA321']
          Valencia: ['VLG127', 'RYA803', 'RYA803', 'VLG127']
          Vancouver: ['VLG765']
          Washington DC: ['RYA456']
          Winnipeg: ['IB123']
```

__Ejercicio 39__. 
`fecha_mayor_incremento_pasajeros`: Dada una lista de tuplas de tipo `Vuelo` devuelve cuál es la fecha con mayor incremento del número de pasajeros respecto del día anterior. El concepto del día anterior se refiere al anterior que hubo vuelos.

_Resultados esperados_
```python

TEST: fecha_mayor_incremento_pasajeros
        2007-12-01
```
