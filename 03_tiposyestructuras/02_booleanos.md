---
layout: default
title: 📗 Boolean Python
title_nav: 📗 Booleano
parent: 📦 03. Tipos y estructuras
description: Los tipos booleanos en Python, o también conocidos como bool en Inglés, son un tipo de datos que se usa para representar un valor binario, verdadero o falso (True o False). Por lo tanto sólo pueden almacenar dos valores distintos. Son uno de los tipos más usados en Python.
order: 27
nav_order: b
permalink: /booleano-python
---

# Booleanos en Python
Al igual que en otros lenguajes de programación, en Python existe el tipo bool o booleano. Es un tipo de dato que permite almacenar dos valores `True` o `False`.

## Declarar variable bool
Se puede declarar una variable booleana de la siguiente manera.
```python
x = True
y = False
```

## Evaluar expresiones
Un valor booleano también puede ser el resultado de evaluar una expresión. Ciertos operadores como el mayor que, menor que o igual que devuelven un valor bool.

```python
print(1 > 0)  #True
print(1 <= 0) #False
print(9 == 9) #True
```

## Función bool
También es posible convertir un determinado valor a bool usando la función bool().

```python
print(bool(10))     # True
print(bool(-10))    # True
print(bool("Hola")) # True
print(bool(0.1))    # True
print(bool([]))     # False
```

## Uso con if
Los condicionales if evalúan una condición que es un valor bool.

```python
a = 1
b = 2
if b > a:
    print("b es mayor que a")
```

La expresión que va después del if es siempre evaluada hasta que se da con un booleano.
```python
if True:
    print("Es True")
```

## Bool como subclase de int
Es importante notar que aunque estemos listando el tipo `bool` como si fuese un tipo más, es en realidad una subclase del `int` visto anteriormente. De hecho lo puedes comprobar de la siguiente manera.

```python
isinstance(True, int)
#True
issubclass(bool, int)
#True
```