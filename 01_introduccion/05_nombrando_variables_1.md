---
layout: default
title: 📗 Nombrando variables I
parent: 🕺🏻 01. Introducción
description: Las variables en Python pueden ser creadas con el nombre de la variable igual al valor. A diferencia de en otros lenguajes de programación, no es necesario declararla anteriormente.
order: 6
nav_order: e
permalink: /variables-python
---

# Nombrando variables


## Crear variables
Las variables en Python se pueden crear asignando un valor a un nombre sin necesidad de declararla antes.

```python
x = 10
y = "Nombre"
z = 3.9
```


## Nombres de variables
Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o números al principio.

```python
# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10
```

Los siguientes ejemplos no son permitidos.
```python
# No válido
2variable = 10
var-iable = 10
var iable = 10
```

## Asignar múltiples valores
Se pueden asignar múltiples variables en la misma línea.
```python
x, y, z = 10, 20, 30
```

## Imprimir variables
Una variable puede ser impresa por pantalla usando `print()`

```python
x = 10
y = "Nombre"

print(x)
print(y)
```