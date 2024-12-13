---
layout: default
title: 📙 Zip en Python
title_nav: 📙 Iterar con zip
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: El uso de la función zip en Python nos permite iterar clases iterables en paralelo. Para ello, acepta varios iterables como entrada y nos devuelve un iterador.
order: 21
nav_order: i
permalink: /zip-python
---

# Iterar con zip en Python

La función `zip()` de Python viene incluida por defecto en el *namespace*, lo que significa que puede ser usada sin tener que importarse.

De acuerdo con la documentación [oficial](https://docs.python.org/3/library/functions.html#zip):

> Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted.

Dicho de otra manera, si pasamos dos listas a `zip` como entrada, el resultado será una tupla donde cada elemento tendrá todos y cada uno de los elementos i-ésimos de las pasadas como entrada.

Veamos un ejemplo. Como podemos ver, el resultado tras aplicar `zip` es una lista con `a[0]b[0]` en el primer elemento y `a[1]b[1]` como segundo.

```python
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))
# [(1, 'Uno'), (2, 'Dos')]
```

*A priori* puede parecer una función no muy relevante, pero es realmente útil combinada con un [for](/for-python) para iterar dos [listas](/listas-en-python) en paralelo.

```python
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)
    
# Número 1 Letra Uno
# Número 2 Letra Dos
```

## zip() con n argumentos

Ya hemos visto el uso de `zip` con dos listas, pero dado que está definida como `zip(*iterables)`, es posible pasar un número arbitrario de [iterables](/iterator-python) como entrada.

Veamos un ejemplo con varias [listas](/listas-en-python). Es importante notar que todas tienen la misma longitud, dos.

```python
numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)

for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)
    
# 1 Uno One Un
# 2 Dos Two Deux
```

## zip() con diferentes longitudes

También podemos usar `zip` usando iterables de diferentes longitudes. En este caso lo que pasará es que el iterador para cuando la lista más pequeña se acaba.

```python
numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]

for n, e in zip(numeros, espanol):
    print(n, e)

# 1 Uno
# 2 Dos
```

Resulta lógico que este sea el comportamiento, porque de no ser así y se continuara, no tendríamos valores para usar.

## zip() con un argumento

Como cabría esperar, dado que `zip` está definido para un número arbitrario de parámetros de entrada, es posible también posible usar un único valor. El resultado son [tuplas](/tuplas-python) de un elemento.

```python
numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))

# [(1,), (2,), (3,), (4,), (5,)]
```

## zip() con diccionarios

Hasta ahora nos hemos limitado a usar `zip` con listas, pero la función está definida para cualquier clase [iterable](/iterator-python). Por lo tanto podemos usarla también con [diccionarios](/diccionarios-en-python).

Si realizamos lo siguiente, `a,b` toman los valores de las key del [diccionario](/diccionarios-en-python). Tal vez algo no demasiado interesante.

```python
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for a, b in zip(esp, eng):
    print(a, b)

# 1 1
# 2 2
# 3 3
```

Sin embargo, si hacemos uso de la función [items](https://ellibrodepython.com/diccionarios-en-python#items), podemos acceder al *key* y *value* de cada elemento.

```python
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)

# 1 Uno One
# 2 Dos Two
# 3 Tres Three
```

Nótese que en este caso ambas *key* `k1` y `k2` son iguales.

## Deshacer el zip()

Con un pequeño truco, es posible deshacer el `zip` en una sola línea de código. Supongamos que hemos usado `zip` para obtener `c`.

```python
a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print(list(c))
# [(1, 'One'), (2, 'Two'), (3, 'Three')]
```

¿Es posible obtener `a` y `b` desde `c`? Sí, tan sencillo como:

```python
c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')
```

Nótese el uso de `*c`, lo que es conocido como [unpacking](/unpacking-python) en Python.
