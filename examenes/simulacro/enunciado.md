# Fundamentos de Programación · Tercera convocatoria · Examen de Python (Modelo B)

Se dispone de datos sobre las actuaciones de varias giras de conciertos en recintos españoles. Los datos están almacenados en el archivo *actuaciones.csv* del que se muestra un extracto de sus dos primeras líneas:

```csv
id_actuacion,recinto,artista,promotora,fecha_actuacion,asistentes_totales,asistentes_por_zona,teloneros,tasa_ocupacion
1,Gran Canaria Arena,Hielo y Ceniza,Riff Producciones,29/03/2026,9614,"{'pista': 5402, 'grada': 3867, 'vip': 345}","['Delta Sur', 'Eco Joven']",87.4
```

Cada línea del archivo CSV incluye la siguiente información sobre una actuación: el **identificador de la actuación**, el **recinto**, el **artista**, la **promotora**, la **fecha de la actuación**, los **asistentes totales**, los **asistentes en cada zona** del recinto (“pista”, “grada” y “vip”), los **teloneros** que abrieron la actuación y la **tasa de ocupación**.

Por ejemplo, en el CSV se puede observar:

- La primera línea es una línea de cabecera.
- En la segunda línea, se indica que el **29/03/2026** actúa en el **Gran Canaria Arena** el artista **Hielo y Ceniza**, contratado por la promotora **Riff Producciones**, ante **9614** asistentes, repartidos entre **5402** en la zona *“pista”*, **3867** en *“grada”* y **345** en *“vip”*, con los teloneros **Delta Sur** y **Eco Joven**, siendo la tasa de ocupación del **87.4%**.

## Proyecto que se le requiere implementar

El proyecto debe tener la siguiente estructura de carpetas:

- ***data:*** carpeta en la que se ubica el fichero *actuaciones.csv*
- ***doc:*** carpeta en la que se ubica el fichero *identificacion.md* que debe rellenar con sus datos
- ***src:*** carpeta en la que se ubican los módulos Python ***actuaciones.py*** ***actuaciones_test.py***

Para implementar los ejercicios que se solicitan **utilice obligatoriamente** la definición del *NamedTuple* que se indica a continuación:

```python
from datetime import datetime, date
from typing import NamedTuple

Actuacion = NamedTuple("Actuacion", [
    ("id_actuacion", int),
    ("recinto", str),
    ("artista", str),
    ("promotora", str),
    ("fecha_actuacion", date),
    ("asistentes_totales", int),
    ("asistentes_por_zona", dict[str, int]),
    ("teloneros", list[str]),
    ("tasa_ocupacion", float)
])
```

Se pide implementar las funciones de los ejercicios que figuran a continuación en el módulo ***actuaciones.py*** y sus correspondientes **métodos de prueba con los parámetros adecuados** en el módulo ***actuaciones_test.py***. Tenga en cuenta que se pueden definir funciones auxiliares cuando se considere necesario. Las puntuaciones están indicadas para cada ejercicio y las pruebas solo puntuarán si las funciones *test* tienen los parámetros adecuados, se pueden ejecutar y el resultado coincide con el esperado.

## Ejercicio 1 (2,00 puntos)

**lee_actuaciones**: dada una cadena de texto con la ruta de un fichero *CSV*, devuelve una lista de tuplas de tipo Actuacion con la información contenida en el fichero.

```python
def lee_actuaciones(ruta_fichero: str) -> list[Actuacion]:
```

Para realizar la función anterior, se recomienda que se ayude de las siguientes funciones auxiliares:

- **parsea_fecha:** dada una cadena con fecha en formato "%d/%m/%Y", devolver la fecha correspondiente.

```python
def parsea_fecha(fecha:str) -> date:
```

- **parsea_zonas:** dada una cadena que incluye los asistentes por zona del recinto, devolver el diccionario correspondiente, donde su clave es la zona y el valor asociado es el número de asistentes en dicha zona. Por ejemplo, en el caso mostrado anteriormente, el diccionario resultante es: { 'pista': 5402, 'grada': 3867, 'vip': 345 }.

```python
def parsea_zonas(asistentes_por_zona: str) -> dict[str, int]:
```

- **parsea_teloneros:** dada una cadena que incluye los teloneros, devuelva la lista correspondiente.

```python
def parsea_teloneros(teloneros: str) -> list[str]:
```

Resultados esperados:

```text
TEST lee_actuaciones
Número de registros leídos: 69

Los dos primeros registros son:
Actuacion(id_actuacion=1, recinto='Gran Canaria Arena', artista='Hielo y Ceniza', promotora='Riff Producciones', fecha_actuacion=datetime.date(2026, 3, 29), asistentes_totales=9614, asistentes_por_zona=defaultdict(<class 'int'>, {'pista': 5402, 'grada': 3867, 'vip': 345}), teloneros=['Delta Sur', 'Eco Joven'], tasa_ocupacion=87.4)
Actuacion(id_actuacion=2, recinto='Gran Canaria Arena', artista='Hielo y Ceniza', promotora='Riff Producciones', fecha_actuacion=datetime.date(2026, 4, 10), asistentes_totales=8976, asistentes_por_zona=defaultdict(<class 'int'>, {'pista': 4566, 'grada': 3708, 'vip': 702}), teloneros=['Cristal Roto'], tasa_ocupacion=81.6)

Los dos últimos registros son:
Actuacion(id_actuacion=68, recinto='Gran Canaria Arena', artista='Cometa 84', promotora='Atlántico Shows', fecha_actuacion=datetime.date(2026, 10, 29), asistentes_totales=9042, asistentes_por_zona=defaultdict(<class 'int'>, {'pista': 4589, 'grada': 3960, 'vip': 493}), teloneros=['Ana Brisa', 'Las Hiedras', 'Los Satélites'], tasa_ocupacion=82.2)
Actuacion(id_actuacion=69, recinto='Roig Arena', artista='Cometa 84', promotora='Atlántico Shows', fecha_actuacion=datetime.date(2027, 1, 17), asistentes_totales=14960, asistentes_por_zona=defaultdict(<class 'int'>, {'pista': 5786, 'grada': 8091, 'vip': 1083}), teloneros=['Mirlo', 'Medusa', 'Eco Joven'], tasa_ocupacion=95.9)
```

## Ejercicio 2 (2,00 puntos)

**actuaciones_artista**: dada una lista de tuplas de tipo Actuacion, el nombre de un artista y dos fechas opcionales, una *fecha de inicio* y otra *fecha de fin*, con valor por defecto None, devuelve una lista de tuplas (recinto, fecha, asistentes totales) con las actuaciones de dicho artista en el periodo comprendido entre ambas fechas, **ordenada de la actuación más reciente a la más antigua**. Con relación al periodo debe tener en cuenta que si ambas fechas son None se incluyen todas las actuaciones; si solo la fecha de inicio es None se consideran las actuaciones hasta la fecha de fin (inclusive); si solo la fecha de fin es None se consideran desde la fecha de inicio (inclusive); y si ambas se especifican, se toman las actuaciones comprendidas entre ambas fechas, ambas inclusive.

```python
def actuaciones_artista(actuaciones:list[Actuacion],
                        artista: str,
                        fecha_inicio: date|None = None,
                        fecha_fin: date|None = None) -> list[tuple[str,date,int]]:
```

Resultados esperados:

```text
TEST actuaciones_artista
Las actuaciones de Marea Alta entre None y None son:
Roig Arena en fecha 2026-03-24 y 14929 asistentes.
WiZink Center en fecha 2026-01-30 y 16269 asistentes.
Gran Canaria Arena en fecha 2025-11-10 y 10505 asistentes.
Gran Canaria Arena en fecha 2025-10-23 y 9372 asistentes.

TEST actuaciones_artista
Las actuaciones de Luna Carmesí entre 2026-01-01 y 2026-12-31 son:
Bizkaia Arena en fecha 2026-11-07 y 15438 asistentes.
Roig Arena en fecha 2026-08-20 y 13104 asistentes.
WiZink Center en fecha 2026-04-30 y 15827 asistentes.
Palau Sant Jordi en fecha 2026-03-21 y 15408 asistentes.
Roig Arena en fecha 2026-03-14 y 14368 asistentes.
WiZink Center en fecha 2026-01-11 y 15963 asistentes.

TEST actuaciones_artista
Las actuaciones de Hielo y Ceniza entre None y 2026-08-31 son:
Bizkaia Arena en fecha 2026-08-27 y 18340 asistentes.
Bizkaia Arena en fecha 2026-07-01 y 17279 asistentes.
Gran Canaria Arena en fecha 2026-04-10 y 8976 asistentes.
Gran Canaria Arena en fecha 2026-03-29 y 9614 asistentes.

TEST actuaciones_artista
Las actuaciones de Los Faros del Sur entre 2026-10-01 y None son:
Palau Sant Jordi en fecha 2027-04-21 y 14454 asistentes.
Palau Sant Jordi en fecha 2027-01-11 y 16002 asistentes.
Coliseum A Coruña en fecha 2026-11-22 y 9845 asistentes.
Roig Arena en fecha 2026-10-16 y 14134 asistentes.
```

## Ejercicio 3 (1,50 puntos)

**hay_conflicto_agenda_artista:** dada una lista de tuplas de tipo Actuacion y el nombre de un artista, devuelve True si dicho artista tiene dos o más actuaciones programadas en la *misma* fecha exacta (en cualquier recinto), False en caso contrario.

```python
def hay_conflicto_agenda_artista(actuaciones: list[Actuacion], artista: str) -> bool:
```

Resultados esperados:

```text
TEST hay_conflicto_agenda_artista
Hay conflicto de agenda para Kora Vance: True

TEST hay_conflicto_agenda_artista
Hay conflicto de agenda para Luna Carmesí: False
```

## Ejercicio 4 (2,00 puntos)

**telonero_mas_frecuente**: dada una lista de tuplas de tipo Actuacion y una tasa de ocupación mínima, con valor por defecto 0.0, devuelve un diccionario cuya clave es el nombre de un recinto y el valor asociado es el telonero más frecuente en dicho recinto, es decir, aquél que ha abierto más actuaciones en dicho recinto, considerando **únicamente las actuaciones cuya tasa de ocupación sea mayor o igual que la mínima indicada**. Los recintos sin ninguna actuación que cumpla la condición no aparecen en el diccionario.

```python
def telonero_mas_frecuente(actuaciones:list[Actuacion],
                           ocupacion_minima: float = 0.0) -> dict[str,str]:
```

Resultados esperados:

```text
TEST telonero_mas_frecuente
Con una ocupación mínima del 0.0%:
En Gran Canaria Arena el telonero más frecuente es Cristal Roto.
En Bizkaia Arena el telonero más frecuente es Las Hiedras.
En Coliseum A Coruña el telonero más frecuente es Plan B.
En WiZink Center el telonero más frecuente es Ana Brisa.
En Palau Sant Jordi el telonero más frecuente es Los Satélites.
En Auditorio Rocío Jurado el telonero más frecuente es Pulso.
En Roig Arena el telonero más frecuente es Eco Joven.

TEST telonero_mas_frecuente
Con una ocupación mínima del 90.0%:
En Bizkaia Arena el telonero más frecuente es Las Hiedras.
En Coliseum A Coruña el telonero más frecuente es Cristal Roto.
En WiZink Center el telonero más frecuente es Rayo Verde.
En Roig Arena el telonero más frecuente es Eco Joven.
En Palau Sant Jordi el telonero más frecuente es Medusa.
En Gran Canaria Arena el telonero más frecuente es Cristal Roto.
En Auditorio Rocío Jurado el telonero más frecuente es Mirlo.
```

## Ejercicio 5 (2,50 puntos)

**artista_mayor_tiempo_retorno:** Dada una lista de tuplas de tipo Actuacion y el nombre de un recinto, devuelve una tupla *(artista, dias)* con el nombre del artista y el **mayor número de días transcurridos entre dos actuaciones consecutivas** de dicho artista en ese mismo recinto.

- **Nota:** Solo se consideran artistas con **al menos 2 actuaciones** en el recinto dado. Si ningún artista ha actuado más de una vez en dicho recinto, la función debe devolver None.

```python
def artista_mayor_tiempo_retorno(actuaciones:list[Actuacion],
                                 recinto: str) -> tuple[str,int] | None:
```

Para calcular los días transcurridos, la propiedad days devuelve los días de diferencia entre dos fechas *f1* y *f2*: `(f2-f1).days`

Resultados esperados:

```text
TEST artista_mayor_tiempo_retorno
El artista con mayor tiempo de retorno a Roig Arena es: Cometa 84 con 214 días.

TEST artista_mayor_tiempo_retorno
No constan retornos del mismo artista a Auditorio Rocío Jurado.
```
