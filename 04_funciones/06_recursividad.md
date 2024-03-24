---
layout: default
title: 📙 Recursividad
parent: 🕹 04. Funciones
description: Podemos hacer uso de las funciones recursivas cuando es posible expresar un problema en subproblemas cuya naturaleza es la misma que la de el problema inicial. Dicho de otra manera, una función recursiva es aquella que se define en función de si misma.
order: 45
nav_order: f
permalink: /recursividad
---

# Recursividad

> ¿En qué trabajas? Estoy intentando arreglar los problemas que creé cuando intentaba arreglar los problemas que creé cuando intentaba arreglar los problemas que creé. Y así nació la recursividad.

La **recursividad** o recursión es un concepto que proviene de las matemáticas, y que aplicado al mundo de la programación nos permite resolver problemas o tareas donde las mismas pueden ser divididas en subtareas cuya funcionalidad es la misma. Dado que los subproblemas a resolver son de la misma naturaleza, se puede usar la misma función para resolverlos. Dicho de otra manera, una función recursiva es aquella que está definida en función de sí misma, por lo que se llama repetidamente a sí misma hasta llegar a un punto de salida.

Cualquier función recursiva tiene dos secciones de código claramente divididas:
* Por un lado tenemos la sección en la que la función se llama a sí misma.
* Por otro lado, tiene que existir siempre una condición en la que la función retorna sin volver a llamarse. Es muy importante porque de lo contrario, la función se llamaría de manera indefinida.

Veamos unos ejemplos con el **factorial** y la **serie de fibonacci**.

## Calcular factorial

Uno de los ejemplos mas usados para entender la recursividad, es el cálculo del factorial de un número `n!`. El factorial de un número `n` se define como la multiplicación de todos sus números predecesores hasta llegar a uno. Por lo tanto `5!`, leído como cinco factorial, sería `5*4*3*2*1`.

Utilizando un enfoque tradicional no recursivo, podríamos calcular el factorial de la siguiente manera.


```python
def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r

factorial_normal(5) # 120
```



Dado que el factorial es una tarea que puede ser dividida en subtareas del mismo tipo (multiplicaciones), podemos darle un enfoque recursivo y escribir la función de otra manera.


```python
def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

factorial_recursivo(5) # 120
```



Lo que realmente hacemos con el código anterior es llamar a la función `factorial_recursivo()` múltiples veces. Es decir, `5!` es igual a `5 * 4!`  y `4!` es igual a `4 * 3!` y así sucesivamente hasta llegar a 1.

Algo muy importante a tener en cuenta es que si realizamos demasiadas llamadas a la función, podríamos llegar a tener un error del tipo `RecursionError`. Esto se debe a que todas las llamadas van apilándose y creando un contexto de ejecución, algo que podría llegar a causar un `stack overflow`. Es por eso por lo que Python lanza ese error, para protegernos de llegar a ese punto.

## Serie de Fibonacci

Otro ejemplo muy usado para ilustrar las posibilidades de la recursividad, es calcular la serie de fibonacci. Dicha serie calcula el elemento `n` sumando los dos anteriores `n-1` + `n-2`. Se asume que los dos primeros elementos son 0 y 1.


```python
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
```

Podemos ver que siempre que la `n` sea distinta de cero o uno, se llamará recursivamente a la función, buscando los dos elementos anteriores. Cuando la `n` valga cero o uno se dejará de llamar a la función y se devolverá un valor concreto. Podemos calcular el elemento 7, que será 0,1,1,2,3,5,8,13, es decir, 13.


```python
fibonacci_recursivo(7)
# 13
```