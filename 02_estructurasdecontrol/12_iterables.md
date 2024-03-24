---
layout: default
title: 📕 Iteradores en Python
title_nav: 📕 Iteradores e Iterables
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: Los iterator o iteradores en Python son una herramienta muy potente que se nos ofrece para "navegar" a través de objetos que sean de una clase iterable. Pueden ser usados sobre cadenas, listas o diccionarios, pero también es posible hacer que una clase sea iterable implementando el método dunder __iter__().
order: 24
nav_order: k
permalink: /iterator-python
---

# Iteradores e Iterables

Si ya entiendes el uso del [while](/while-python/) y el [for](/for-python/), entonces sin duda estás listo para continuar con los **iterables**. Sin duda son una herramienta muy potente de Python que nos permite como su nombre indica, *iterar* colecciones que sean *iterables*. A continuación veremos estos dos conceptos en detalle.

Antes de nada planteemos el problema que queremos resolver. Tenemos una determinada colección de datos, en este caso una lista con varios valores, y queremos mostrar sus valores uno a uno por pantalla. Si eres nuevo en Python o vienes de otros lenguajes de programación, tal vez lo resolverías de la siguiente manera con un *while*.


```python
# Mal uso
lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
# Salida: 5, 4, 9, 2
```


Aunque es una solución válida y que funciona perfectamente, tal vez sea mejor usar un bucle *for*, ya que nos podemos ahorrar alguna línea de código.


```python
# Mal uso
lista = [5, 4, 9, 2]
for i in range(len(lista)):
    elemento = lista[i]
    print(elemento)
# Salida: 5, 4, 9, 2
```

Aunque esta segunda forma es también válida, en Python existe una forma mucho más fácil de iterar una lista. Dicha forma es la siguiente.


```python
lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)
# Salida 5, 4, 9, 2
```

Si saberlo, ya has hecho uso de los iteradores, usando la clase lista que es una clase iterable. Como puedes ver, se trata de una solución mucho más sencilla. A continuación veremos lo que es un iterable y cómo puede ser usado.


## Iterables

Una clase **iterable** es una clase que puede ser iterada. Dentro de Python hay gran cantidad de clases iterables como las listas, *strings*, diccionarios o ficheros. Si tenemos una clase iterable, podemos usarla a la derecha del *for* de la siguiente manera.


```python
# for elemento in [clase_iterable]:
#   ...
```

Si usamos el for como acabamos de mostrar, la variable `elemento` irá tomando los valores de cada elemento presente en la clase iterable. De esta manera, ya no tenemos que ir accediendo manualmente con `[]` a cada elemento.

Anteriormente hemos visto un ejemplo iterando una lista, pero también podemos iterar una cadena, ya que es una clase iterable. Al iterar una cadena se nos devuelve cada letra presente en la misma. Como puedes ver, la sintaxis se asemeja bastante al lenguaje natural, sería algo así como decir "pon en `c` cada elemento presenta en la cadena".


```python
cadena = "Hola"
for c in cadena:
    print(c)
# Salida: H o l a
```


Llegados a este punto, tal vez te preguntes ¿y cómo se yo si una clase es iterable o no? Pues bien, tienes dos opciones. La primera sería consultar la documentación oficial de Python. La segunda es ver si la clase u objeto en cuestión hereda de Iterable ([aquí te explicamos la herencia](/herencia-en-python/) por si aún no la tienes clara). Con `isinstance()` podemos comprobar si una clase hereda de otra.


```python
from collections import Iterable

cadena = "Hola"
numero = 3
print("cadena", isinstance(cadena, Iterable))
print("numero", isinstance(numero, Iterable))

# Salida
# cadena True
# numero False
```


Podemos ver como efectivamente la cadena es iterable y el número no. Es por ello por lo que podemos iterar la cadena, pero el siguiente código daría un error.


```python
numero = 3
for x in numero:
    print(x)
# Error TypeError: 'int' object is not iterable
```

Python nos ofrece también diferentes métodos que pueden ser usados sobre clases iterables como los que se muestran a continuación:
* `list()` convierte a lista una clase iterable
* `sum()` para sumar
* `join()` permite unir cada elemento de una clase iterable con el primer argumento usado.


```python
print(list("Hola"))
print(sum([1, 2, 3]))
print("-".join("Hola"))

# Salida:
#['H', 'o', 'l', 'a']
#6
#H-o-l-a
```


De la misma forma que iteramos una cadena o una lista, también podemos iterar un [diccionario](/diccionarios-en-python/). El iterador del diccionario devuelve las claves o *keys* del mismo.


```python
mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(i)
# Salida: a, b, c
```

Una vez hemos entendido lo que es una clase iterable, veamos lo que es un iterador.

## Iteradores

Se podría explicar la diferencia entre **iteradores** e **iterables** usando un libro como analogía. El libro sería nuestra clase iterable, ya que tiene diferentes páginas a las que podemos acceder. El libro podría ser una lista, y cada página un elemento de la lista. Por otro lado, el iterador sería un marcapáginas, es decir, una referencia que nos indica en qué posición estamos del libro, y que puede ser usado para "navegar" por él.

Es posible obtener un iterador a partir de una clase iterable con la función `iter()`. En el siguiente ejemplo podemos ver como obtenemos el iterador del libro.


```python
libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
```

Llegados a este punto, nuestro `marcapaginas` almacena un iterador. Se trata de un objeto que podemos usar para navegar a través del libro. Usando la función `next()` sobre el iterador, podemos ir accediendo secuencialmente a cada elemento de nuestra lista (las páginas de libro).


```python
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))

# página1
# página2
# página3
# página4
```

Algo parecido a esto es lo que sucede por debajo cuando usamos el `for` sobre una clase iterable. Se va accediendo secuencialmente a los elementos hasta que la excepción `StopIteration` es lanzada. Dicha excepción se lanza cuando hemos llegado al final, y no existen más elementos que iterar.


```python
print(next(marcapaginas))
# Salida: StopIteration
```

Una nota muy importante es que cuando el iterador es obtenido con `iter()` como hemos visto, apunta por defecto fuera de la lista. Es decir, si queremos acceder al primer elemento de la lista, deberemos llamar una vez a `next()`.

Por otro lado, a diferencia de un marcapáginas de un libro, el iterador sólo puede ir hacia delante. No es posible retroceder.

## Creando tu clase iterable

Llegados a este punto ya entendemos perfectamente los iterables e iteradores y hemos visto como pueden ser usados con diferentes clases de Python como las cadenas o listas. Sin embargo, tal vez quieras dar un paso más y definir tu propia clase. En [este post](/programacion-orientada-a-objetos/) ya te explicamos cómo definir tus clases. A continuación te explicaremos cómo hacer que tu clase sea iterable.

Empecemos desde cero. Vamos a definir una clase `MiClase` y crear un objeto con ella. Si intentamos usar la función `iter()` para obtener su iterador, tendremos un error ya que nuestra clase por defecto no es iterable.


```python
class MiClase:
    pass

miobjeto = MiClase()
iterador = iter(miobjeto)

# Salida
# TypeError: 'MiClase' object is not iterable
```


Para poder llamar a la función `iter()` sobre la clase, debemos implementar el método **dunder** `__iter__()`. Dicho método debe devolver un iterable, que será usado cuando la clase intente ser iterada.


```python
class MiClase:
    def __init__(self, items):
        self.lista = items
    def __iter__(self):
        return iter(self.lista)
```


Podemos ver como tenemos el método `__init__()` que es llamado cuando se crea una nueva instancia de la clase. Simplemente pasamos una lista como parámetro de entrada y la almacenamos como atributo en `.lista`.

Por otro lado, el método `__iter__()` devuelve un iterador, que simplemente es el iterador de la propia lista. Ahora que **nuestra clase ya es iterable**, podemos hacer lo siguiente.


```python
miobjeto = MiClase([5, 4, 3])
for item in miobjeto:
    print(item)

# Salida: 5, 4, 3
```

Cabe destacar que el ejemplo mostrado tiene fines didácticos y poca aplicación práctica, ya que simplemente se está encapsulando una lista dentro de una clase. Sin embargo sirve para ejemplificar cómo una clase se puede convertir en iterable, y seguramente con esta base encuentres aplicaciones prácticas en tus proyectos.
