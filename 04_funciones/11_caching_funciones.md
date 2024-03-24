---
layout: default
title: 📕 Caching Funciones
parent: 🕹 04. Funciones
description: Python nos permite realizar caching de funciones, lo que permite ahorrar en tiempo de ejecución cuando el valor con el que se llama a la función ya ha sido calculado anteriormente. El caching puede ser implementado por nosotros mismos usando un diccionario, o también podemos usar el lru_cache del paquete functools.
order: 49
nav_order: j
permalink: /caching-python
---

# Caching de Funciones

El [caché](https://es.wikipedia.org/wiki/Cach%C3%A9_(inform%C3%A1tica)) es un término muy usado en informática, y hace referencia al almacenamiento de resultados previos para su posterior reutilización, lo que permite reducir el tiempo de respuesta. Por ejemplo, si llamamos a una función con un determinado parámetro y acto seguido realizamos la misma llamada, sería interesante **reutilizar el primer resultado** para no tener que calcularlo otra vez. Existen por lo tanto dos posibilidades:
* Si ejecutamos la función y el resultado no ha sido calculado con anterioridad, se calcula y se almacena por si fuera útil en el futuro. Esto se conoce como **cache miss**.
* Si ejecutamos la función y el caché tiene almacenado el resultado para esa operación, en vez de calcular otra vez la salida la podemos reutilizar, lo que se conoce como **cache hit**. Dado que estamos reutilizando un valor ya calculado, generalmente el tiempo de respuesta será menor.


Por suerte, Python nos permite añadir *caching* a nuestras [funciones](/funciones-en-python), pero antes de implementarlo es conveniente hacer un análisis sobre nuestro programa y determinar si merece la pena. Algunas cosas a tener en cuenta:
* El *caching* es especialmente útil cuando trabajamos con **funciones muy intensivas en cálculo**, lo que hace que reutilizar el valor del caché reduzca notablemente el tiempo de respuesta.
* Es necesario conocer (a nivel estadístico) **la distribución de los argumentos con los que se llama la función**. Si la función bajo estudio se llama con valores muy dispares y apenas repetidos, el *caching* poco ayudará, ya que apenas tendremos un *cache hit*.
* El uso de un caché puede mejorar el tiempo de respuesta, pero frecuentemente **se paga en un incremento del uso de memoria**. También es necesario decidir el número de valores a almacenar.

A continuación veremos como implementar *caching* en Python, pudiendo hacerlo con [diccionarios](/diccionarios-en-python) o utilizando la librería `functools`. Para ejemplificarlo, veremos como implementar un caché en nuestro código de [números primos](/numeros-primos-python) visto anteriormente, empleando ambas formas.

```python
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
```

# Caching con Diccionarios

La primera forma de realizarlo es usando un [diccionario](/diccionarios-en-python) como caché. Nótese que este es un ejemplo didáctico, y que obvia algunos factores. Como puedes ver tenemos claramente diferenciado el *cache hit* y el *cache miss*. Si el valor no está en el caché se calcula y se devuelve.

```python
def es_primo_concache(num, _cache={}):
    if num not in _cache:
        _cache[num] = True
        for n in range(2, num):
            if num % n == 0:
                _cache[num] = False
                break
    return _cache[num]
```

Dado que `es_primo` es bastante intensivo en cálculo, cuando usamos números grandes el ahorro puede ser muy significativo. En el siguiente código podemos ver como la primera vez que ejecutamos la función, se tardan 3.5 segundos, ya que el resultado tiene que ser calculado. Sin embargo la segunda vez que la llamamos con la misma entrada, tenemos un *cache hit*, por lo que el valor ya no es calculado sino recuperado del caché, tardando microsegundos.

```python

import time
tic = time.time()
es_primo_concache(25565479)
print(time.time() - tic)

tic = time.time()
es_primo_concache(25565479)
print(time.time() - tic)

# 3.5551438331604004
# 4.0531158447265625e-06
```

# Caching con functools y lru_cache

La segunda forma de realizarlo, y un poco más sofisticada es usando `lru_cache`, un [decorador](/decoradores-python) que viene con la librería estándar [functools](https://docs.python.org/3/library/functools.html). La mayor ventaja es que no necesitamos modificar la función. Nótese que `maxsize` nos permite indicar el número máximo de valores que queremos almacenar en el caché.

```python
from functools import lru_cache

@lru_cache(maxsize=32)
def es_primo_concache(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
```

Por lo tanto si ahora llamamos a nuestra función con los mismos valores, podemos ver como la primera vez tarda 3.9 segundos, pero la segunda apenas tarda unos microsegundos.

```python
import time
tic = time.time()
es_primo_concache(25565479)
print(time.time() - tic)

tic = time.time()
es_primo_concache(25565479)
print(time.time() - tic)

# 3.9316678047180176
# 3.0994415283203125e-06
```

En el caso de que queramos limpiar el caché de nuestra función, podemos realizar lo siguiente.

```python
es_primo_concache.cache_clear()
```