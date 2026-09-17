# T01.3-If

En un módulo funciones.py implementa las siguientes funciones para practicar con la sentencia de control selectiva if y expresiones. Prueba las funciones en el módulo `funciones_test`.

## Ejercicio 1
Implementa una función que, dados el peso y la estatura de una persona, devuelva su **estado nutricional**, según la clasificación de la **OMS** (ver  Fuente: https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal).

| IMC                                | Estado nutricional |
| ---------------------------------- | ------------------ |
| Inferiora 18.5                     | Bajo peso          |
| [18.5 , 25)                        | Normal             |
| [25 , 30)                          | Sobrepeso          |
| Superior o igual a 30              | Obesidad           |



---

## Ejercicio 2

Implementa una función que dada una nota numérica entre 0 y 10, devuelve una nota que representa su calificación en las actas. La calificación puede ser SUSPENSO, APROBADO, NOTABLE ó SOBRESALIENTE. Si la nota tiene el valor None, indicará que el estudiante no se ha presentado y en el acta debe aparecer NO PRESENTADO.

## Ejercicio 3

Implementa una función llamada `categoria_huracan`, que dada la velocidad del viento, indique la categoría del huracán. Trata la velocidad del viento como un entero.

| Categoría | Velocidad (km/h)          |
| --------- | --------------------------|
| 1         | 118 – 152                 |
| 2         | 153 – 176                 |
| 3         | 177 – 208                 |
| 4         | 209 – 248                 |
| 5         | Superior a 248            |

---
## Ejercicio 4

El gobierno ha lanzado un *programa de Bono Cultural para Jóvenes* con el objetivo de incentivar la participación en actividades artísticas y culturales. Las reglas del programa son las siguientes:

1. Solo pueden acceder jóvenes de entre *12 y 30 años*.
2. El bono base depende de la edad:
      - Entre 12 y 17 años → 20 €
      - Entre 18 y 25 años → 40 €
      - Entre 26 y 30 años → 30 €
3. Si el joven es *estudiante y su familia gana menos de 20,000 € al año*, recibe un extra de *10 €*.
4. Si los ingresos familiares son mayores a 50,000 €, el bono se reduce en *5 €*.
5. El bono nunca puede ser negativo.

El escriba una función en Python que, dada la edad, si es estudiante y los ingresos familiares, determine el monto del bono cultural, si la persona no es eligible (no es joven) el monto del bono debe ser *5 €*.


📌 **Descomposición en funciones**

Para resolver este problema de froma más clara y ordenada, es aconsejable dividir el programa en subproblemas, y crear funciones específicas para resolver cada uno de los subproblemas. Una descomposición en funciones puede ser la siguiente:

- Función `es_elegible` que, dada la edad de una persona, verifica si la edad está dentro del rango permitido (12 a 30 años). Devuelve, por tanto, un valor lógico (`True` o `False`).
- Función `bono_base` que, dada la edad de una persona, determina el monto inicial del bono según el rango de edad.
- Función `ajuste_bono` que, dados el bono base, si la persona es estudiante y los ingresos familiares, devuelve la cuantía del bono tras aplicarle modificaciones correspondientes, teniendo en cuenta si es estudiante y el nivel de ingresos familiares.
  Usa la función nativa `max` para garantizar que el bono no sea negativo.
- Función `bono_cultural` que, dados la edad, si la persona es estudiante y los ingresos familiares, devuelve la cuantía del bono. Esta función es la función principal para resolver este problema, y se va a encargar de coordinar el resto de funciones.
  Primero llama a `es_elegible` para verificar si puede acceder al bono, luego obtiene el monto base con `bono_base`. Finalmente ajusta el valor con `ajuste_bono`.

👉 Esta descomposición en funciones hace que el código sea más:

  - **Modular** → cada parte del problema está aislada en su propia función.
  - **Reutilizable** → se pueden usar las funciones de manera independiente.
  - **Legible** → el programa se entiende paso a paso.
