from collections import namedtuple


Persona = namedtuple('Persona', 'nombre, apellidos, edad')

def suma_edades(personas: list[Persona]) -> int:
    result = 0
    for p in personas:
        result += p.edad
    return result

def mapea_edades(personas: list[Persona]) -> list[int]:
    result = []
    for p in personas:
        result.append(p.edad)
    return result

def reduce_suma(edades: list[int]) -> int:
    return sum(edades)

def suma_edades2(personas: list[Persona]) -> int:
    edades = mapea_edades(personas)    # map: cada persona -> su edad
    return reduce_suma(edades)                            # reduce: se suman todas

personas = [
    Persona('Ana', 'García López', 34),
    Persona('Luis', 'Pérez Ruiz', 27),
    Persona('Marta', 'Sánchez Gil', 45),
]
print(suma_edades(personas))
print(suma_edades2(personas))


def max_persona(personas: list[Persona]) -> Persona | None:
    result = None
    for p in personas:
        if result == None or result.edad<p.edad:
            result = p
    return result

def min_persona(personas: list[Persona]) -> Persona | None:
    result = None
    for p in personas:
        if result == None or result.edad>p.edad:
            result = p
    return result

def mapea_edad_persona(personas: list[Persona])-> list[tuple[int, Persona]]:
    result = []
    for p in personas:
        result.append((p.edad, p))
    return result

def max_persona_2(personas: list[Persona]) -> Persona | None:
    tuplas = mapea_edad_persona(personas)

    result = max(tuplas)
    if result is not None:
        result = result[1]

    return result

def min_persona_2(personas: list[Persona]) -> Persona | None:
    tuplas = mapea_edad_persona(personas)

    result = min(tuplas)
    if result is not None:
        result = result[1]
        
    return result

print(max_persona(personas))
print(min_persona(personas))
print(max_persona_2(personas))
print(min_persona_2(personas))



VOWELS = 'aeiou'
sentence = 'we are studying list comprehensions'

#Ejemplo 1
def contador(sentence: str) -> int:
    result = 0
    for x in sentence:
        if x in VOWELS:
            result += 1
    return result

def contador_filter(sentence: str) -> int:
    '''result = []
    for x in sentence:
        if x in VOWELS:
            result.append(x)'''
    result = filter(lambda x:x in VOWELS, sentence)
    return len(result)












#Ejemplo 2
def mapea(secuencia: str) -> list[int]:
    result = []
    for x in secuencia:
        result.append(1 if x in VOWELS else 0)
    return result

def contador_2(sentence: str) -> int:
    unos_y_ceros = mapea(sentence)    # map: cada carácter -> 1 o 0
    return reduce_suma(unos_y_ceros)        # reduce: se suman todos

print(contador(sentence))
print(contador_2(sentence))

def existe_naive(datos: list[bool])->bool:
    result = False
    for x in datos:
        result = result or x
        if result:
            break
    return result

#Ejemplo 1
def existe_vowel(sentence: str) -> bool:
    result = False
    for x in sentence:
        result = result or x in VOWELS
        if result:
            break
    return result

#Ejemplo 2
def mapea_vocal(secuencia: str) -> list[bool]:
    result = []
    for x in secuencia:
        result.append(x in VOWELS)
    return result

def reduce_existe(booleanos: list[bool]) -> bool:
    return any(booleanos)
    
def existe_vowel2(sentence: str) -> bool:
    booleanos = mapea_vocal(sentence)    # map: cada carácter -> True o False
    return reduce_existe(booleanos)       # reduce: basta con que uno sea True

print(existe_naive([False, True]))
print(any([False, True]))
print(existe_vowel(sentence))
print(existe_vowel2(sentence))

def para_todo_naive(datos: list[bool])->bool:
    result = True
    for x in datos:
        result = result and x
        if not result:
            break
    return result

print(para_todo_naive([False, True]))
print(all([False, True]))

#Ejemplo 1
def para_todo_vowel(sentence: str) -> bool:
    result = True
    for x in sentence:
        result = result and x in VOWELS
        if not result:
            break
    return result

#Ejemplo 2
def reduce_para_todo(booleanos: list[bool]) -> bool:
    return all(booleanos)

def para_todo_vowel2(sentence: str) -> bool:
    booleanos = mapea_vocal(sentence)    # map: cada carácter -> True o False
    return reduce_para_todo(booleanos)       # reduce: basta con que uno sea True

lista = [600, 1, 2, -1]

def max_(datos: list[int]) -> int | None:
    result = None
    for x in datos:
        if result == None or result<x:
            result = x
    return result

def min_(datos: list[int]) -> int | None:
    result = None
    for x in datos:
        if result == None or result>x:
            result = x
    return result

print(max(lista), max_(lista), min(lista), min_(lista))


