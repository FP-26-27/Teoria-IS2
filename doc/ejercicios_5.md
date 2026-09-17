# T01.5-For

Proyecto para trabajar con ejercicios sencillos de for

1. Función `sumar_pares` que, dados dos números enteros inicio y fin, devuelva la suma de los números pares que están en el intervalo [inicio, fin).
    ```python 
    >>> sumar_pares(1, 10)
    20
    >>> sumar_pares(0, 5)
    6
    >>> sumar_pares(5, 5)
    0
    >>> sumar_pares(10, 15)
    36
    ``` 
2. Función `mostrar_tabla_multiplicar` que, dado un número n, muestre por pantalla la tabla de multiplicar de n (desde 1 hasta 10). Por ejemplo, si n es 5, debería mostrar:
```
5 x  1 = 5
5 x  2 = 10
…
5 x 10 = 50
```
3. Función `factorial` que, dado un número n, devuelva el factorial de ese número. El factorial de un número n es el valor resultado de multiplicar n x (n-1) x (n-2) x … x 1. Por ejemplo, el factorial de 5 es 5x4x3x2x1=120.
   ```python
   >>> factorial(0)
   1
   >>> factorial(1)
   1
   >>> factorial(5)
   120
   >>> factorial(7)
   5040
   ```
4. Función `suma_digitos` que, dado un número entero positivo n, devuelva la suma de los dígitos del número. Por ejemplo, si el número es el 12345, el resultado debería ser 15.

   ```python
   >>> suma_digitos(0)
   0
   >>> suma_digitos(12345)
   15
   >>> suma_digitos(9876)
   30
   >>> suma_digitos(1001)
   2
   ```

5. Función `contar_vocales` que, dada una cadena de texto, devuelva el número de vocales que contiene esa cadena. 

```python
  >>> contar_vocales("Hola Mundo")
  4
  >>> contar_vocales("Python")
  1
  >>> contar_vocales("AEIOUaeiou")
  10
  >>>contar_vocales("bcdfg")
  0
  ```
