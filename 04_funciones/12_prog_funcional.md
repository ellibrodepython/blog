---
layout: default
title: 📕 Programación Funcional
parent: 🕹 04. Funciones
description: La programación funcional es un paradigma distinto al orientado a objetos u estructurado. Se caracteriza por la ausencia de bucles, siendo las funciones la herramienta más importante. A pesar de que Python no es puramente funcional, ofrece funciones propias de lenguajes funcionales como map, filter y reduce.
order: 50
nav_order: k
permalink: /programacion-funcional-python
---

# Programación Funcional en Python

En pocas palabras, la programación funcional es un paradigma de programación distinto al tradicional estructurado u [orientado a objetos](https://ellibrodepython.com/programacion-orientada-a-objetos-python) al que solemos estar acostumbrados. Se basa principalmente en el uso de funciones, siendo las mismas practicamente la única herramienta que el lenguaje nos ofrece. Por ello, en lenguajes puramente funcionales como [Haskell](https://www.haskell.org/) no existen bucles [for](https://ellibrodepython.com/for-python) o [while](https://ellibrodepython.com/while-python).

¿Un lenguaje de programación sin bucles? Aunque pueda parecer una locura, también tiene sus ventajas, y ofrece ciertas características muy importantes que veremos a continuación.

A pesar de que Python no es un lenguaje puramente funcional, nos ofrece algunas primitivas propias de lenguajes funcionales, como `map`, `filter` y `reduce`. Todas ellas ofrecen una alternativa al uso de bucles para resolver ciertos problemas. Veamos unos ejemplos.

## map en Python

La función `map` toma dos entradas:
* Una [lista](https://ellibrodepython.com/listas-en-python) o [iterable](https://ellibrodepython.com/iterator-python) que será modificado en una nueva.
* Una [función](/funciones-en-python), que será aplicada a cada uno de los elementos de la lista o iterable anterior.

Nos devuelve una nueva lista donde todos y cada uno de los elementos de la lista original han sido pasados por la función.

```python
map(funcion_a_aplicar, entrada_iterable)
```

Imaginemos que queremos multiplicar por dos todos los elementos de una lista. La primera forma que se nos podría ocurrir sería la siguiente. Nótese que también podría usarse [list comprehension](https://ellibrodepython.com/list-comprehension-python), pero eso lo dejamos para otro artículo.

```python
lista = [1, 2, 3, 4, 5]
lista_pordos = []
for l in lista:
    lista_pordos.append(l*2)

print(lista_pordos)
# [2, 4, 6, 8, 10]
```

Pero **veamos como darle un enfoque funcional**. Como hemos dicho, `map` toma una función y un iterable como entrada, aplicando la función a cada elemento. Entonces podemos definir una función `por_dos`, que pasaremos a `map` junto con nuestra lista inicial.

```python
lista = [1, 2, 3, 4, 5]

def por_dos(x):
    return x * 2

lista_pordos = map(por_dos, lista)

print(list(lista_pordos))
# [2, 4, 6, 8, 10]
```

Como podemos observar, ya no usamos bucles. Simplemente le pasamos a `map` la función y la lista y ya hace el trabajo por nosotros. Dado que `por_dos` se trata de una función muy sencilla, es posible usar funciones [lambda](https://ellibrodepython.com/lambda-python) para compactar un poco el código, quedando lo siguiente:

```python
lista = [1, 2, 3, 4, 5]
lista_pordos = map(lambda x: 2*x, lista)

print(list(lista_pordos))
# [2, 4, 6, 8, 10]
```


## filter en Python

La función `filter` también recibe una función y una lista pero **el resultado es la lista inicial filtrada**. Es decir, se pasa cada elemento de la lista por la función, y sólo si su resultado es `True`, se incluye en la nueva lista.

```python
filter(funcion_filtrar, entrada_iterable)
```

Al igual que hacíamos antes, usamos las funciones [lambda](https://ellibrodepython.com/lambda-python) que nos permiten declarar y asignar una [función](https://ellibrodepython.com/funciones-en-python) en la misma línea de código. En el siguiente ejemplo filtramos los números pares.

```python
lista = [7, 4, 16, 3, 8]
pares = filter(lambda x: x % 2 == 0, lista)

print(list(pares))
# [4, 16, 8] 
```

Nótese que el siguiente código sería equivalente:

```python
lista = [7, 4, 16, 3, 8]

def es_par(x):
    return x % 2 == 0

pares = filter(es_par, lista)

print(list(pares))
# [4, 16, 8]
```

Una vez más, resaltar que no estamos usando bucles. Simplemente damos la entrada y la función a aplicar a cada elemento, y `filter` se encarga del resto. Esta es una de las características clave de la programación funcional. Se centra más en el qué hacer que en el cómo hacerlo. Para ello se usan funciones predefinidas como las que estamos viendo, a las que sólo tenemos que pasar las entradas y hacer el trabajo por nosotros.


## reduce en Python

Por último, podemos usar `reduce` para **reducir todos los elementos de la entrada a un único valor** aplicando un determinado criterio. Por ejemplo, podemos **sumar** todos los elementos de una lista de la siguiente manera.

```python
from functools import reduce
lista = [1, 2, 3, 4, 5]
suma = reduce(lambda acc, val: acc + val, lista)
print(suma) # 15
```

Lo que podría reescribirse usando la función `add`:

```python
from operator import add
from functools import reduce
lista = [1, 2, 3, 4, 5]
suma = reduce(add, lista)
print(suma) # 15
```

O también los podemos **multiplicar**, modificando la función lambda.

```python
from functools import reduce
lista = [1, 2, 3, 4, 5]
multiplicacion = reduce(lambda acc, val: acc * val, lista)
print(multiplicacion) # 120
```

Es importante notar que la función recibe dos argumentos: el acumulador y cada uno de los valores de la lista.
* El **acumulador** es el valor devuelto en la iteración anterior, que va acumulando un resultado hasta que llegamos al final.
* El **valor** es cada uno de los elementos de nuestra lista, que en nuestro caso vamos añadiendo al acumulador.

El uso de `reduce` es especialmente útil cuando tenemos por ejemplo una [lista](https://ellibrodepython.com/listas-en-python) de [diccionarios](https://ellibrodepython.com/diccionarios-en-python) y queremos sumar todos los valores de un campo en concreto. Veamos un ejemplo donde calculamos la edad media de varias personas.


```python
from functools import reduce
personas = [
    {'Nombre': 'Alicia', 'Edad': 22},
    {'Nombre': 'Bob', 'Edad': 29},
    {'Nombre': 'Charlie', 'Edad': 33}
]
suma_edad = reduce(lambda total, p: total + p['Edad'], personas, 0)
print(suma_edad/len(personas)) # 28.0
```

Nótese que llamamos a `reduce` con un valor adicional `0`, que es el valor inicial del acumulador. Una vez más, hemos resuelto un problema en el que tradicionalmente usaríamos bucles con las primitivas de la programación funcional.

## Características de la Programación Funcional

Una vez entendido el funcionamiento de `map`, `filter` y `reduce`, ya tenemos unas nociones básicas de la programación funcional. Sus características más importantes son las siguientes:
* Los lenguajes de programación puramente funcionales **carecen de bucles for y while**.
* Se dice que en la programación funcional, las funciones son "ciudadanas de primera clase", lo que nos viene a decir que **prácticamente todo se hace con funciones**, y no con bucles.
* La programación funcional prefiere también las **funciones puras**, es decir, funciones sin [side effects](https://es.wikipedia.org/wiki/Efecto_secundario_(inform%C3%A1tica)). **Las funciones puras no dependen de variables externas o globales**. Esto significa que para las mismas entradas, siempre se producen las mismas salidas.
* Por otro lado, en la programación funcional se prefiere **variables inmutables**, lo que significa que una vez creadas no pueden ser modificadas. Esto es algo que verdaderamente ahorra problemas, aunque la eficiencia puede ser discutible.
* En general, se considera que los lenguajes de programación funcionales son **más seguros**, y ofrecen [formal verification](https://es.wikipedia.org/wiki/Verificaci%C3%B3n_formal).

Por último, resaltar una vez más que aunque Python no es un lenguaje puramente funcional, ofrece algunas funciones propias de lenguajes funcionales como `map`, `filter` y `reduce`. Si estás interesado en más, puedes echar un vistazo a el paquete [itertools](https://docs.python.org/3/library/itertools.html).

## Ejemplos Programación Funcional

Dada una lista de personas almacenadas en diccionarios:
* Filtrar de acuerdo al sexo
* Y calcular la media

```python
from functools import reduce
personas = [
    {'Nombre': 'Alicia', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'},
]

hombres = list(filter(lambda x: x['Sexo'] == 'M', personas))
suma_edades = reduce(lambda suma, p: suma + p['Edad'], hombres, 0)
media_edad = suma_edades/(len(hombres))
print(media_edad) # 33.0
```

Tal vez no muy legible, pero todo lo anterior se podrá expresar en una única línea de código.

```python
media_edades = reduce(lambda suma, p: suma + p['Edad'], filter(lambda x: x['Sexo'] == 'M', personas), 0) / len(list(filter(lambda x: x['Sexo'] == 'M', personas)))
print(media_edades) # 33.0
```