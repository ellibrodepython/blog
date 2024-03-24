---
layout: default
title: 📗 Números aleatorios
parent: 🔬 13. Ejemplos y ejercicios
description: Generar números aleatorios en Python es por suerte una tarea muy fácil usando la librería random. Existen diferentes funciones que nos permiten generar números enteros o decimales aleatorios como la función random(), la uniform() o randint().
order: 93
nav_order: a
permalink: /numeros-aleatorios-python
---

# Números aleatorios Python
Generar números aleatorios en Python es por suerte una tarea muy fácil usando la librería `random`.

Vamos a ver diferentes funciones:
* randint
* uniform
* random
* choice

## Función randint

La función `randint` genera un número aleatorio **entero** entre 0 y n, siendo el segundo valor 30 en este caso.
```python
from random import *
print(randint(0, 30))
# 10
```

## Función uniform

Si queremos generar valores aleatorios que sean **decimales** podemos hacer uso de `uniform`.
```python
from random import *
print(uniform(0,10))
# 6.68079620859125
```

## Función random

Por otro lado tenemos la función `random` que no acepta parámetros y genera números aleatorios **decimales** de entre 0 y 1.

```python
from random import *
print(random())
# 0.00402817235037356
```


## Función choice

Por último, la función `choice` nos permite elegir un elemento aleatorio de una lista.

```python
from random import *
print(choice(["A", "B", "C"]))
# C
```
