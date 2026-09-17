# Ejercicios del tema 2: Expresiones, tipos predefinidos y entrada salida
---

Cree una carpeta ``src``, y dentro de la misma un archivo ``ejercicioX.py`` para cada ejercicio que vaya a resolver, sustituyendo la X por el número del ejercicio. Implemente en cada archivo la función solicitada por el ejercicio correspondiente, asegurándose de que las pruebas de la función se realicen como programa principal.

### Ejercicio 1

Defina una función `es_bisiesto` que reciba un año y devuelva un valor lógico `True` si el año es bisiesto, y `False` en caso contrario. Un año es bisiesto si es divisible por 400, o bien si es divisible por 4 pero no por 100.

Pruebe la función anterior pasándole los años 2000, 2024, 1900 y 2025 (los dos primeros son bisiestos, los dos últimos no).

### Ejercicio 2

Defina una función `extrae_numeros` que reciba un texto y devuelva todas aquellas cantidades que aparezcan dentro del texto. Por ejemplo, si el texto es "Este año la empresa ganó 12432 euros de 8 contratos", la función devuelve `[12432, 8]`. Observe que los elementos de la lista devuelta son de tipo `int`. 

Pruebe la función pasándole la frase de ejemplo anterior.

### Ejercicio 3

Defina una función `calcula_edad` que reciba la fecha de nacimiento de una persona y devuelva:

- La edad que tiene actualmente la persona.
- Cuántos días quedan para su cumpleaños.

Pruebe la función pasándole su fecha de nacimiento. Con el valor obtenido muestre un mensaje de este estilo:

```
Tienes 18 años. Quedan 121 días para tu cumpleaños.
```

Haga uso de las cadenas de formato para construir el mensaje anterior.


### Ejercicio 4

Disponemos de un fichero de datos en el que se recogen las variaciones de la temperatura media del planeta registrada mensualmente. Para un periodo determinado del que disponemos de datos (desde 1880 hasta 2016), cada valor nos indica en cuántos grados es mayor o menor la temperatura media registrada en un mes/año determinado, con respecto a la temperatura media de todo el periodo para el que hay datos. Por ejemplo, si para diciembre de 2016 tenemos el valor 0,7895, significa que la temperatura media registrada para diciembre de 2016 fue 0,7895 grados mayor que la media de temperaturas registradas entre 1880 y 2016.

Defina una función ``lee_variaciones_temperatura`` que reciba la ruta de un archivo de datos en formato CSV y devuelva una lista de tuplas con los datos leídos. El archivo CSV constará de dos columnas, la primera de las cuales indica una fecha y la segunda la diferencia entre la temperatura media registrada ese mes y la temperatura media de todo el periodo para el que hay datos. 

Pruebe la función anterior leyendo el fichero ubicado en ``data/monthly_csv.csv`` y mostrando en la consola las 5 primeras tuplas de la lista obtenida.

### Ejercicio 5
Defina una función ``muestra_variaciones_temperatura`` que reciba la ruta de un archivo de datos en formato CSV como el del ejercicio anterior y genere una gráfica que muestre la evolución en el tiempo de las variaciones de temperatura.

Use el módulo `pyplot` de `matplotlib`, como en el siguiente ejemplo:

```python
from matplotlib import pyplot
pyplot.title("Ejemplo de uso de pyplot")
valores_x = [0, 1, 2] # Coordenada x de los puntos a mostrar
valores_t = [5, 5, 1] # Coordenada y de los puntos a mostrar
pyplot.plot(valores_x, valores_y) # Dibuja la gráfica
pyplot.show() # Se muestra la gráfica en una ventana
```

Pruebe la función pasándole la ruta ``data/monthly_csv.csv``.

### Ejercicio 6
Cree una nueva versión de la función ``muestra_variaciones_temperatura``, que reciba, además de la ruta del archivo de datos, dos parámetros ``fecha_inicial`` y ``fecha_final``. La función generará la misma gráfica del ejercicio anterior, pero usando sólo los datos contenidos en el intervalo de fechas que va de ``fecha_inicial`` a ``fecha_final``, ambas inclusive. 

Los parámetros ``fecha_inicial`` y ``fecha_final`` pueden contener un valor ``None``, en cuyo caso no se aplicará ninguna restricción al comienzo o el final del intervalo de fechas a mostrar en la gráfica. 

Prueba la función pasándole la ruta ``data/monthly_csv.csv``.

### Ejercicio 7

Añada el siguiente código al módulo ejercicio4.py, y a continuación trate de completar los huecos marcados con #TODO 
 
```python
from collections import namedtuple

# Definición del tipo Persona:
# nombre: Nombre de la persona.
# edad: Edad de la persona en años.
# tiene_licencia: Booleano que indica si la persona tiene licencia de conducir.
# hobbies: Conjunto de hobbies o actividades que le gustan a la persona.
# paises_visitados: Conjunto de países que la persona ha visitado.
# libros_leidos: Lista de libros que la persona ha leído en orden de lectura.
Persona = namedtuple('Persona', ['nombre', 'edad', 'tiene_licencia', 'hobbies', 'paises_visitados', 'libros_leidos'])

juan = Persona('Juan', 20, True, {'fútbol', 'cine'}, {'España', 'Chile'}, ['Don Quijote', 'El Principito'])
maria = Persona('Maria', 15, False, {'lectura', 'música', 'cine'}, {'Francia', 'Chile'}, ['El Principito', '1984'])
pedro = Persona('Pedro', 17, True, {'fútbol', 'natación'}, {'México'}, ['Cien Años de Soledad', 'Moby Dick', '1984'])


print("Juan tiene más de 18 años:",
    #TODO
)

print("Maria tiene licencia de conducir:",
    #TODO
)

print("Juan ha visitado Chile:",
    #TODO
)

print("A María le gustan el cine y la música:",
    #TODO
)

print("'El Principito' es el último libro que ha leído Maria:",
    #TODO
)

print("Ni Juan ni Pedro tienen licencia de conducir:",
    #TODO
)

print("Maria ha leído al menos 2 libros:",
    #TODO
)

print("María no ha visitado México, pero Pedro sí:",
    #TODO
)

print("Juan ha leído más libros que María pero menos que Pedro:",
    #TODO
)

print("Pedro no ha visitado Chile y tampoco le gusta el cine:",
    #TODO
)

print("El último libro que María ha leído es '1984' y Juan no lo ha leído aún:",
    #TODO
)

print("Pedro ha visitado más países que Juan o ha leído más libros que María:",
    #TODO
)

print("María tiene licencia de conducir o ha leído 'Moby Dick', pero no ambas cosas",
    #TODO
)

print("Juan ha visitado España o Francia, pero no ambos",
    #TODO
)
```

Para las siguientes expresiones, se precisan dos operadores que aún no hemos estudiado:

* Operador de intersección de conjuntos ``&``: devuelve un conjunto con los elementos comunes a los dos conjuntos sobre los que se opera.
* Método ``index`` del tipo ``list``: recibe un valor y devuelve la posición de la lista en la que aparece por primera vez dicho valor. **¡CUIDADO!** Si no se encuentra el valor en la lista, se produce un error de tipo ``ValueError``.

```python
print("Pedro y Juan comparten al menos un hobby:",
    #TODO
)

print("Juan y María han visitado al menos un país en común o ambos tienen el hobby de ir al cine:",
    #TODO
)

print("Juan ha leído 'Don Quijote' antes que 'El Principito':",
    #TODO
)
```
