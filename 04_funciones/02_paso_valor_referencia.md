---
layout: default
title: 📙 Paso por valor y referencia
parent: 🕹 04. Funciones
description: Cuando una función es llamada, sus parámetros de entrada pueden ser pasados por valor o por referencia. En el primer caso se actuará sobre una copia de la variable y en el segundo sobre la misma variable. En Python, existen ciertas particularidades.
order: 41
nav_order: b
permalink: /paso-por-valor-y-referencia
---

## Paso por valor y referencia

En muchos lenguajes de programación existen los conceptos de paso por **valor** y por **referencia** que aplican a la hora de como trata una función a los parámetros que se le pasan como entrada. Su comportamiento es el siguiente:
* Si usamos un parámetro pasado por **valor**, se creará una copia local de la variable, lo que implica que cualquier modificación sobre la misma no tendrá efecto sobre la original.
* Con una variable pasada como **referencia**, se actuará directamente sobre la variable pasada, por lo que las modificaciones afectarán a la variable original.

En Python las cosas son un poco distintas, y el comportamiento estará definido por el tipo de variable con la que estamos tratando. Veamos un ejemplo de paso por **valor**.


```python
x = 10
def funcion(entrada):
    entrada = 0
funcion(x)

print(x) # 10
```


Iniciamos la `x` a 10 y se la pasamos a `funcion()`. Dentro de la función hacemos que la variable valga 0. Dado que Python trata a los `int` como pasados por **valor**, dentro de la función se crea una copia local de `x`, por lo que la variable original no es modificada.

No pasa lo mismo si por ejemplo `x` es una lista como en el siguiente ejemplo. En este caso Python lo trata como si estuviese pasada por **referencia**, lo que hace que se modifique la variable original. La variable original `x` ha sido modificada.


```python
x = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)

funcion(x)
print(x) # [10, 20, 30, 40]
```


El ejemplo anterior nos podría llevar a pensar que si en vez de añadir un elemento a `x`, hacemos `x=[]`, estaríamos destruyendo la lista original. Sin embargo esto no es cierto.


```python
x = [10, 20, 30]
def funcion(entrada):
    entrada = []

funcion(x)
print(x)
# [10, 20, 30]
```


Una forma muy útil de saber lo que pasa por debajo de Python, es haciendo uso de la función `id()`. Esta función nos devuelve un identificador único para cada objeto. Volviendo al primer ejemplo podemos ver como los objetos a los que "apuntan" `x` y `entrada` son distintos.


```python
x = 10
print(id(x)) # 4349704528
def funcion(entrada):
    entrada = 0
    print(id(entrada)) # 4349704208

funcion(x)
```


Sin embargo si hacemos lo mismo cuando la variable de entrada es una lista, podemos ver que en este caso el objeto con el que se trabaja dentro de la función es el mismo que tenemos fuera.


```python
x = [10, 20, 30]
print(id(x)) # 4422423560
def funcion(entrada):
    entrada.append(40)
    print(id(entrada)) # 4422423560

funcion(x)
```