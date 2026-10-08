# TEO-Ambito de variables y Paso de parámetros

**Autora**: Toñi Reina


## Ejercicio 1: La Nave Espacial y sus Controles

La nave Estrella Veloz tiene dos recursos globales:
- Combustible (inicialmente 1000 unidades).
- Tripulantes (inicialmente 5).

Cada sistema de la nave trabaja con variables locales que pueden tener el mismo nombre que las globales:
- El sistema motor tiene su propio tanque de combustible y una variable de temperatura.
- El sistema oxígeno tiene su propio tanque de combustible y una variable de presión.

👉 **Tu tarea es**:

En una carpeta `src` crea el módulo `nave_espacial.py`, añade al módulo el siguiente código y ejecútalo. Observa qué ocurre en cada impresión.

💻 **Código**

```python
# Variables globales
combustible = 1000
tripulantes = 5

def sistema_motor():
    combustible = 300  # Variable local con el mismo nombre
    temperatura = 85   # Variable local
    print("🔧 Sistema Motor")
    print("Combustible (local en motor):", combustible)
    print("Temperatura del motor:", temperatura)
    print("Tripulantes (global):", tripulantes)
    print("-" * 30)

def sistema_oxigeno():
    combustible = 150  # Variable local con el mismo nombre
    presion = 2.5      # Variable local
    print("💨 Sistema Oxígeno")
    print("Combustible (local en oxígeno):", combustible)
    print("Presión del oxígeno:", presion)
    print("Tripulantes (global):", tripulantes)
    print("-" * 30)

# Ejecución de los sistemas
sistema_motor()
sistema_oxigeno()

print("🌍 Centro de control")
print("Combustible (global):", combustible)
print("Tripulantes (global):", tripulantes)
print("-" * 30)

# Intenta descomentar estas líneas para ver qué ocurre
# print(temperatura)  # ❌ Error: no definida en este ámbito
# print(presion)      # ❌ Error: no definida en este ámbito
```

🎯 **Preguntas de reflexión**
1. ¿Por qué el valor de combustible es diferente en cada sistema?
2. ¿Qué ocurre si intentas imprimir temperatura o presion fuera de las funciones?
3. ¿Qué variable se mantiene igual en todos los sistemas y en el centro de control?

_____________________________
## Ejercicio 2 : El Mago y la Poción
Un mago quiere preparar una poción usando un ingrediente y un caldero:

- El ingrediente se pasa como parámetro, pero también hay una variable global con el mismo nombre.
- El caldero se pasa como parámetro (lista), y también existe otra variable global con el mismo nombre.

👉 **Tu tarea es**:
Crea un módulo `mago.py` en la carpeta `src`. Copia el siguiente código, ejecútalo y observa qué ocurre con las variables después de llamar a la función.

```python
# Variables globales
ingrediente = "Raíz de mandrágora"
caldero = ["Hojas de luna"]

def preparar_pocion(ingrediente, caldero):
    print("✨ Preparando poción...")
    print("Ingrediente recibido (parámetro):", ingrediente)
    print("Caldero recibido (parámetro):", caldero)

    # Modificaciones dentro de la función
    ingrediente = "Polvo de estrellas"  # Cambia solo el parámetro, no la global
    caldero.append("Agua mágica")       # Sí afecta a la lista global

    print("Ingrediente dentro de la función:", ingrediente)
    print("Caldero dentro de la función:", caldero)
    print("-" * 30)

# Llamada a la función
preparar_pocion(ingrediente, caldero)

# Imprimir variables globales después
print("🌍 Variables globales tras la función:")
print("Ingrediente global:", ingrediente)
print("Caldero global:", caldero)
```

🎯 **Preguntas de reflexión**
1. ¿Por qué el valor de ingrediente global no cambia aunque se modifique dentro de la función?
2. ¿Por qué el caldero global sí cambia después de llamar a la función?
3. ¿Qué enseña este comportamiento sobre el paso de parámetros con tipos inmutables (str, int, float) y tipos mutables (listas, diccionarios)?