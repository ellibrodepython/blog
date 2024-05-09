---
layout: default
title: 📙 Unpacking en Python
parent: 🕺🏻 01. Introducción
description: A través del uso de args y kwargs en Python, podemos hacer lo que es denominado como unpacking, y consiste en asignar un iterable o diccionario a varias variables.
order: 12
nav_order: k
permalink: /unpacking-python
---

# Unpacking en Python

El *unpacking* en Python nos permite asignar una [lista](https://ellibrodepython.com/listas-en-python) a múltiples variables en una única línea de código.

```python
a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
print(c) # 3
```

También es posible hacerlo con otros iterables como las [tuplas](https://ellibrodepython.com/tuplas-python).

```python
a, b, c = (1, 2, 3)
print(a) # 1
print(b) # 2
print(c) # 3
```

Y como es de esperar, el número de variables debe coincidir con la longitud. Obtenemos `not enough values to unpack` si proporcionamos menos.

```python
a, b, c = (1, 2)
# ValueError: not enough values to unpack (expected 3, got 2)
```

Y `too many values to unpack` si proporcionamos de más.

```python
a, b = (1, 2, 3, 4)
# ValueError: too many values to unpack (expected 2)
```

Se pueden dar casos curiosos como el siguiente, ya que en realidad funciona con cualquier [iterable](https://ellibrodepython.com/iterator-python).

```python
a, b, c = "123"
print(a) # 1
print(b) # 2
print(c) # 3
```

De hecho funciona también con [diccionarios](https://ellibrodepython.com/diccionarios-en-python), siendo la *key* lo usado por defecto.

```python
a, b, c = {'uno': 1, 'dos':2, 'tres': 3}
print(a) # uno
print(b) # dos
print(c) # tres
```

Aunque también podemos usar los *values*.

```python
a, b, c = {'uno': 1, 'dos':2, 'tres': 3}.values()
print(a) # 1
print(b) # 2
print(c) # 3
```

Dado que `range` devuelve un iterador, también lo podemos usar.

```python
a, b, c = range(3)
print(a) # 0
print(b) # 1
print(c) # 2
```


## Operador de Unpacking

Relacionado con el *unpacking* existe el operador `*`, que nos permite realizar asignaciones cuando el número de elementos es distinto. Tanto de esta manera.

```python
*a, b = (1, 2, 3)
print(a) # [1, 2]
print(b) # 3
```

Como de esta otra.

```python
a, *b = (1, 2, 3)
print(a) # 1
print(b) # [2, 3]
```

Podemos usarlo para unir listas. Aunque es importante notar que esto se puede hacer de otras formas como usando `+` o `.extend()`.

```python
a = [1, 2]
b = [3, 4]
c = [*a, *b]

print(c)
# [1, 2, 3, 4]
```

También tenemos el operador definido para diccionarios, usando `**`.

```python
a = {"uno": 1, "dos": 2}
b = {"tres": 3, "cuatro": 4}

c = {**a, **b}

print(c)
# {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
```

Ten cuidado si tienes *keys* duplicados, ya que el segundo sobrescribirá al primero.

```python
a = {"uno": 1, "dos": 2}
b = {"uno": 0, "dos": 0}

c = {**a, **b}

print(c)
# {'uno': 0, 'dos': 0}
```

Y por último también podemos hacer cosas interesantes con bucles [for](https://ellibrodepython.com/for-python).

```python
for primero, *resto in [(1, 2, 3), (4, 5, 6, 7)]:
    print("Primero:", primero)
    print("Resto:", resto)
    
# Primero: 1
# Resto: [2, 3]
# Primero: 4
# Resto: [5, 6, 7]
```

## Unpacking para Swapping

La principal aplicación práctica del *unpacking* es para intercambiar o hacer *swap* de variables en una única línea de código. Aunque pueda parecer algo sencillo, no todos los lenguajes permiten esto.

```python
a, b = (1, 2)
print(a, b)
# 1 2

a, b = b, a
print(a, b)
# 2 1
```

## Unpacking en Funciones

Por último, aunque lo vemos más en detalle en [args y kwargs](https://ellibrodepython.com/args-kwargs-python), el *unpacking* nos permite pasar un número de argumentos variables a una función.

```python
def funcion(a, *args, **kwargs):
    print(f"args={a} args={args} kwargs={kwargs}")

funcion(1)
# args=1 args=() kwargs={}

funcion(1, 2)
# args=1 args=(2,) kwargs={}

funcion(1, 2, 3, cuatro=4, cinco=5)
# args=1 args=(2, 3) kwargs={'cuatro': 4, 'cinco': 5}
```
