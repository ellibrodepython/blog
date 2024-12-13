---
layout: default
title: 📙 Break en Python
title_nav: 📙 Break
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: El uso del break() en Python nos permite terminar prematuramente la ejecución de un bucle for o while.
order: 19
nav_order: g
permalink: /break-python
---

# Sentencia break Python

## Introducción al break

La sentencia `break` nos permite alterar el comportamiento de los bucles [while](/while-python) y [for](/for-python). Concretamente, permite terminar con la ejecución del bucle.

Esto significa que una vez se encuentra la palabra `break`, el bucle se habrá terminado.

## Break con bucles for

Veamos como podemos usar el `break` con bucles [for](/for-python). El `range(5)` generaría 5 iteraciones, donde la `i` valdría de 0 a 4. Sin embargo, en la primera iteración, terminamos el bucle prematuramente.

El `break` hace que nada más empezar el bucle, se rompa y se salga sin haber hecho nada.


```python
for i in range(5):
    print(i)
    break
    # No llega

# Salida: 0
```

Un ejemplo un poco más útil, sería el de buscar una letra en una palabra. Se itera toda la palabra y en el momento en el que se encuentra la letra que buscábamos, se rompe el bucle y se sale.

Esto es algo muy útil porque si ya encontramos lo que estábamos buscando, no tendría mucho sentido seguir iterando la lista, ya que desperdiciaríamos recursos.


```python
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

# Salida:
# P
# y
# t
# Se encontró la h
```


## Break con bucles while

El `break` también nos permite alterar el comportamiento del [while](/while-python). Veamos un ejemplo.

La condición `while True` haría que la sección de código se ejecutara indefinidamente, pero al hacer uso del `break`, el bucle se romperá cuando `x` valga cero.


```python
x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
    print("Fin del bucle")

#4, 3, 2, 1, 0
```

Por norma general, y salvo casos muy concretos, si ves un `while True`, es probable que haya un `break` dentro del bucle.

## Break y bucles anidados

Como hemos dicho, el uso de `break` rompe el bucle, pero sólo aquel en el que está dentro.

Es decir, si tenemos dos bucles anidados, el `break` romperá el bucle anidado, pero no el exterior.

```python
for i in range(0, 4):
    for j in range(0, 4):
        break
        #Nunca se realiza más de una iteración
    # El break no afecta a este for
    print(i, j)

# 0 0
# 1 0
# 2 0
# 3 0
```
