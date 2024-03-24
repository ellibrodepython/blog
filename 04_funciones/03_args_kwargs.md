---
layout: default
title: 📙 Args y Kwargs Python
title_nav: 📙 Uso de args y kwargs
parent: 🕹 04. Funciones
description: Si quieres definir una función en Python con un número variable de argumentos de entrada, esto es posible gracias al uso de args y kwargs. El uso de args nos permite manejar los argumentos como una tupla, y kwargs como un diccionario.
order: 42
nav_order: c
permalink: /args-kwargs-python
---

# Args y Kwargs en Python

Si alguna vez has tenido que definir una [función](/funciones-en-python/) con un número variable de argumentos y no has sabido como hacerlo, a continuación te explicamos cómo gracias a los args y kwargs en Python.

Vamos a suponer que queremos una función que sume un conjunto de números, pero no sabemos *a priori* la cantidad de números que se quieren sumar. Si por ejemplo tuviéramos tres, la función sería tan sencilla como la siguiente.


```python
def suma(a, b, c):
    return a+b+c

suma(2, 4, 6)
#Salida: 12
```



El problema surge si por ejemplo queremos sumar cuatro números. Como es evidente, la siguiente llamada a la función anterior daría un error ya que estamos usando cuatro argumentos mientras que la función sólo soporta tres.


```python
suma(2, 4, 6, 1)
#TypeError: suma() takes 3 positional arguments but 4 were given
```


Introducida ya la problemática, veamos como podemos resolver este problema con \*args y \*\*kwargs en Python.

## Uso de \*args

Gracias a los \*args en Python, podemos definir funciones cuyo número de argumentos es variable. Es decir, podemos definir funciones genéricas que no aceptan un número determinado de parámetros, sino que se "adaptan" al número de argumentos con los que son llamados.

De hecho, el *args* viene de *arguments* en Inglés, o argumentos. Haciendo uso de \*args en la declaración de la función podemos hacer que el número de parámetros que acepte sea variable.


```python
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

suma(1, 3, 4, 2)
#Salida 10

suma(1, 1)
#Salida 2
```


Antes de nada, el uso del nombre `args` es totalmente arbitrario, por lo que podrías haberlo llamado como quisieras. Es una mera convención entre los usuarios de Python y resulta frecuente darle ese nombre. Lo que si es un requisito, es usar `*` junto al nombre.

En el ejemplo anterior hemos visto como `*args` puede ser iterado, ya que en realidad es una [tupla](/tuplas-python/). Por lo tanto iterando la tupla podemos acceder a todos los argumentos de entrada, y en nuestro caso sumarlos y devolverlos.

Nótese que es un mero ejemplo didáctico. En realidad podríamos hacer algo como lo siguiente, lo que sería mucho más sencillo.


```python
def suma(*args):
    return sum(args)

suma(5, 5, 3)
#Salida 13
```



Con esto resolvemos nuestro problema inicial, en el que necesitábamos un número variable de argumentos. Sin embargo, hay otra forma que nos proporciona además un nombre asociado al argumento, con el uso de \*\*kwargs. La explicamos a continuación.

## Uso de \*\*kwargs

Al igual que en \*args, en \*\*kwargs el nombre es una mera convención entre los usuarios de Python. Puedes usar cualquier otro nombre siempre y cuando respetes el `**`.

En este caso, en vez de tener una tupla tenemos un [diccionario](/diccionarios-en-python/). Puedes verificarlo de la siguiente forma con `type()`.


```python
def suma(**kwargs):
    print(type(kwargs))
    
suma(x=3)
#<class 'dict'>
```

Pero veamos un ejemplo más completo. A diferencia de \*args, los \*\*kwargs nos permiten dar un nombre a cada argumento de entrada, pudiendo acceder a ellos dentro de la función a través de un diccionario.


```python
def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s
    
suma(a=3, b=10, c=3)
#Salida
#a = 3
#b = 10
#c = 3
#16
```

Como podemos ver, es posible iterar los argumentos de entrada con `items()`, y podemos acceder a la clave `key` (o nombre) y el valor o `value` de cada argumento.

El uso de los \*\*kwargs es muy útil si además de querer acceder al valor de las variables dentro de la función, quieres darles un nombre que de una información extra.

## Mezclando \*args y \*\*kwargs

Una vez entendemos el uso de \*args y \*\*kwargs, podemos complicar las cosas un poco más. Es posible mezclar argumentos normales con \*args y \*\*kwargs dentro de la misma función. Lo único que necesitas saber es que debes definir la función en el siguiente orden:
* Primero argumentos normales.
* Después los \*args.
* Y por último los \*\*kwargs.

Veamos un ejemplo.


```python
def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

funcion(10, 20, 1, 2, 3, 4, x="Hola", y="Que", z="Tal")
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal
```


Y por último un truco que no podemos dejar sin mencionar es lo que se conoce como *tuple unpacking*. Haciendo uso de `*`, podemos extraer los valores de una lista o tupla, y que sean pasados como argumentos a la función.


```python
def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

args = [1, 2, 3, 4]
kwargs = {'x':"Hola", 'y':"Que", 'z':"Tal"}

funcion(10, 20, *args, **kwargs)
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal
```
