---
layout: default
title: Mutabilidad en Python
title_nav: 📙 Mutabilidad
parent: 📦 03. Tipos y estructuras
description: Python diferencia dos tipos de objetos de acuerdo a si pueden ser o no modificados una veces creados. En el caso de poder serlo, son mutables, y en el caso de que no, inmutables.
order: 38
nav_order: m
permalink: /mutabilidad-python
---

# Identidad, tipo y valor
Python es un lenguaje de programación orientado a objetos, y como tal, trata a todos los tipos de datos como objetos. Un simple [entero](/entero-en-python) es un objeto.

```python
# x es un objeto
x = 5
```

Y una [función](/funciones-en-python) es también un objeto.
```python
# x es un objeto
def x():
    pass
```

Sabido esto, tal vez te preguntes ¿y entonces cuál es la diferencia? ¿en qué se diferencian los objetos? Pues bien, cada objeto viene identificado por su **identidad**, **tipo** y **valor**:

* Identidad: Nunca cambia e identifica de manera unívoca al objeto. El operador [`is`](/operadores-identidad) nos permite saber si dos objetos son en realidad el mismo. Es decir, si dos variables hacen referencia al mismo.
* Tipo: Nos indica el tipo al que pertenece, como un [float](/float-python) o una [lista](/listas-en-python). La función `type()` nos indica el tipo de un determinado objeto. Es la clase a la que pertenece.
* Valor: Todo objeto tiene unas características particulares. Si estas características pueden ser modificadas, diremos que es un tipo mutable. De lo contrario, que es inmutable.

Veamos un ejemplo con un **entero**:
* Podemos ver con `id()`, que se trata de un identificador único. Es importante notar que si ejecutamos el código diferentes veces, su valor no tiene porqué se el mismo.
* Por otro lado el tipo entero, `<class 'int'>`.
* Por último tenemos su valor, `10`.

```python
x = 10
print("Identidad:", id(x))
print("Tipo:", type(x))
print("Value:", x)

# Identidad: 4474035136
# Tipo: <class 'int'>
# Value: 10
```

Los enteros en Python, son un tipo **inmutable** y a continuación explicaremos las implicaciones que tiene esto.

# Mutabilidad

Los diferentes tipos de Python u otros objetos en general, pueden ser clasificados atendiendo a su mutabilidad. Pueden ser:
* **Mutables**: Si permiten ser modificados una vez creados.
* **Inmutables**: Si no permiten ser modificados una vez creados.

Son **mutables** los siguientes tipos:
* [Listas](/listas-en-python)
* Bytearray
* Memoryview
* [Diccionarios](/diccionarios-en-python)
* [Sets](/sets-python)
* Y clases definidas por el usuario

Y son **inmutables**:
* [Booleanos](/booleano-python)
* [Complejos](/numeros-complejos)
* [Enteros](/entero-en-python)
* [Float](/float-python)
* [Frozenset](/frozenset-en-python)
* [Cadenas](/cadenas-python)
* [Tuplas](/tuplas-python)
* [Range](/range-python)
* Bytes

Sabida ya la clasificación, tal vez te preguntes porqué es esto relevante. Pues bien, Python trata de manera diferente a los tipos mutables e inmutables, y si no entiendes bien este concepto, puedes llegar a tener comportamientos inesperados en tus programas.

La forma más sencilla de ver la diferencia, es usando las listas en oposición a las tuplas. Las primeras son mutables, las segundas no.

Una lista `l` puede ser modificada una vez creada.

```python
# La asignación se puede realizar
l = [1, 2, 3]
l[0] = 0
```

Como hemos explicado antes, `id()` nos devuelve un identificador único del objeto. Como puedes observar, es el mismo antes y después de realizar la modificación.

```python
l = [1, 2, 3]
print(id(l)) #4383854144
l[0] = 0
print(id(l)) #4383854144
```

Sin embargo, una tupla es inmutable, por lo que la siguiente asignación dará un error.

```python
# La asignación no se puede realizar
t = (1, 2, 3)
t[0] = 0
```

Aunque la tupla es inmutable, si que habría una forma de modificar el valor de `t`, pero lo que en realidad hacemos es crear una nueva tupla y asignarle el mismo nombre.

Se podría hacer algo como lo siguiente, convertir la tupla en lista, modificar la lista y convertir a tupla otra vez.

```python
t = (1, 2, 3)
print(id(t)) #4483581184
t = list(t)

# Modificar elemento
t[0] = 0

t = tuple(t)
print(t)     #(0, 2, 3)
print(id(t)) #4483953088
```

Como puedes ver, hemos conseguido modificar el valor de `t`, pero `id(t)` ya no nos devuelve el mismo valor. El nombre de la variable es el mismo, pero el objeto al que "apunta" ha cambiado.

Lo mismo pasa con los [sets](/sets-python) (mutables) y los [frozenset](/frozenset-en-python) (no mutables).

Esto no resulta tan evidente si usamos un entero. Veamos un ejemplo.

Tenemos una variable `x` con su `id` y le añadimos una unidad. El resultado es que el identificador cambia, ya que Python no puede cambiar el 5 al ser el entero un tipo inmutable.

```python
x = 5
print(id(x)) # 4525173536
x = x + 1
print(id(x)) # 4525173568 (Ha cambiado)
```

Sin embargo, si usamos una lista, que es un tipo **mutable**, al intentar modificar la `x`, dicha modificación puede ser realizada en la misma variable, por lo que el `id()` es el mismo 
```python
x = [1, 2]
print(id(x)) # 4382432768
x.append(3)
print(id(x)) # 4382432768 (No cambia)
```

Las principales diferencias entre tipos mutables e inmutables son las siguientes:

* Los tipos inmutables son generalmente más rápidos de acceder. Por lo que si no piensas modificar una lista, es mejor que uses una tupla.
* Los tipos mutables son perfectos cuando quieres cambiar su contenido repetidas veces.
* Los tipos inmutables son caros de cambiar, ya que lo que se hace en realidad es hacer una copia de su contenido en un nuevo objeto con las modificaciones.

# Excepciones de mutabilidad
Aunque tampoco se trata de una excepción propiamente dicha ya que no rompe con lo explicado anteriormente, hay casos en los que si podría parecer que se modifica un tipo inmutable.

Imaginemos que tenemos una tupla (inmutable) compuesta por varios elementos, donde hay una lista (mutable).

```python
l = [4, 5, 6]

# La lista es parte de la tupla
t = (1, 2, 3, l)
print(t)  # (1, 2, 3, [4, 5, 6])

# Podemos modificar la lista
l[0] = 0

# Que también modifica la tupla
print(t)  # (1, 2, 3, [0, 5, 6])
```

Aunque parece que hayamos modificado la tupla `t`, lo que en realidad hemos modificado es la lista `l`, y como la tupla referencia a ella, también se ve modificada.


# Mutabilidad y paso por valor/referencia
La mutabilidad de los objetos es una característica muy importante cuando tratamos con [funciones](/funciones-en-python), ya que Python los tratará de manera distinta.

Si conoces lenguajes de programación como C, los conceptos de paso por valor o referencia te resultarán familiares:

* Los tipos **inmutables** son pasados por **valor**, por lo tanto dentro de la función se accede a una copia y no al valor original.
* Los tipos **mutables** son pasados por **referencia**, como es el caso de las [listas](/listas-en-python) y los [diccionarios](/diccionarios-en-python). Algo similar a como C pasa las array como punteros.


En otros posts te explicamos con más detalle el [paso por valor y referencia](/paso-por-valor-y-referencia), pero veamos un ejemplo.

Tenemos una función que modifica dos variables.
```python
def funcion(a, b):
    a = 10
    b[0] = 10

# x es un entero
x = 5

# y es una lista
y = [5]
```

Si llamamos a la función con ambas variables, vemos como el valor de `x` no ha cambiado, pero el de `y` sí.
```python
funcion(x, y)

print(x) # 5
print(y) # 10
```

Esto se debe a que `a=10` trabaja con un valor de `a` local a la función, al ser el entero un tipo inmutable. Sin embargo `b[0]=10` actúa sobre la variable original.


# Ejercicios y ejemplos

## Modificar una tupla con slicing

Como hemos visto anteriormente, realizar la siguiente asignación no es posible.
```python
T = (1, 2, 3, 4, 5)
T[2] = 0
# TypeError: 'tuple' object does not support item assignment
```

Si por ejemplo queremos modificar el índice `T[2]`, podemos hacer uso del *slicing*.
```python
T = (1, 2, 3, 4, 5)
T = T[:2] + (0,) + T[3:]
print(T) #(1, 2, 0, 4, 5)
```
