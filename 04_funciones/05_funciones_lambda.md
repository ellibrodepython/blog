---
layout: default
title: 📙 Funciones Lambda
parent: 🕹 04. Funciones
description: Las funciones lambda en Python o expresiones lambda, son un tipo de función anónima que puede ser definida en una sola línea de código. También pueden ser asignadas a una variable para ser usadas después.
order: 44
nav_order: e
permalink: /lambda-python
---

# Funciones lambda

Las funciones `lambda` o anónimas son un tipo de funciones en Python que típicamente se definen en una línea y cuyo código a ejecutar suele ser pequeño. Resulta complicado explicar las diferencias, y para que te hagas una idea de ello te dejamos con la siguiente cita sacada de  [la documentación oficial](https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements).


> "Python lambdas are only a shorthand notation if you’re too lazy to define a function."

Lo que significa algo así como, "las funciones lambda son simplemente una versión acortada, que puedes usar si te da pereza escribir una función"

Lo que sería una función que suma dos números como la siguiente.


```python
def suma(a, b):
    return a+b
```

Se podría expresar en forma de una función `lambda` de la siguiente manera.


```python
lambda a, b : a + b
```



La primera diferencia es que una función `lambda` no tiene un nombre, y por lo tanto salvo que sea asignada a una variable, es totalmente inútil. Para ello debemos.


```python
suma = lambda a, b: a + b
```

Una vez tenemos la función, es posible llamarla como si de una función normal se tratase.


```python
suma(2, 4)
```




Si es una función que solo queremos usar una vez, tal vez no tenga sentido almacenarla en una variable. Es posible declarar la función y llamarla en la misma línea.


```python
(lambda a, b: a + b)(2, 4)
```


## Ejemplos

Una función `lambda` puede ser la entrada a una función normal.


```python
def mi_funcion(lambda_func):
    return lambda_func(2,4)

mi_funcion(lambda a, b: a + b)
```



Y una función normal también puede ser la entrada de una función `lambda`. Nótese que son ejemplo didácticos y sin demasiada utilidad práctica per se.


```python
def mi_otra_funcion(a, b):
    return a + b

(lambda a, b: mi_otra_funcion(a, b))(2, 4)
```



A pesar de que las funciones `lambda` tienen muchas limitaciones frente a las funciones normales, comparten gran cantidad de funcionalidades. Es posible tener argumentos con valor asignado por defecto.


```python
(lambda a, b, c=3: a + b + c)(1, 2) # 6
```



También se pueden pasar los parámetros indicando su nombre.


```python
(lambda a, b, c: a + b + c)(a=1, b=2, c=3) # 6
```



Al igual que en las funciones se puede tener un número variable de argumentos haciendo uso de `*`, lo conocido como **tuple unpacking**.


```python
(lambda *args: sum(args))(1, 2, 3) # 6
```


Y si tenemos los parámetros de entrada almacenados en forma de `key` y `value` como si fuera un diccionario, también es posible llamar a la función.


```python
(lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3) # 6
```

Por último, es posible devolver más de un valor.

```python
x = lambda a, b: (b, a)
print(x(3, 9))
# Salida (9,3)
```