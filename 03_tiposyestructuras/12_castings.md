---
layout: default
title: 📙 Casting Python
title_nav: 📙 Castings
parent: 📦 03. Tipos y estructuras
description: Hacer un cast significa convertir un tipo de dato a otro. En Python es posible convertir a string con str() o a integer o entero con int(). También se puede convertir a float con float().
order: 36
nav_order: k
permalink: /casting-python
---

# Cast en Python

Hacer un *cast* o *casting* significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los [int](/entero-en-python), [string](/cadenas-python) o [float](/float-python). Pues bien, es posible convertir de un tipo a otro.

Pero antes de nada, veamos los diferentes tipos de *cast* o conversión de tipos que se pueden hacer. Existen dos:

* Conversión **implícita**: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.

* Conversión **explícita**: Es realizada expresamente por nosotros, como por ejemplo convertir de `str` a `int` con `str()`.

## Conversión implícita

Esta conversión de tipos es realizada automáticamente por Python, prácticamente sin que nos demos cuenta. Aún así, es importante saber lo que pasa por debajo para evitar problemas futuros.

El ejemplo más sencillo donde podemos ver este comportamiento es el siguiente:

```python
a = 1   # <class 'int'>
b = 2.3 # <class 'float'>

a = a + b
print(a)       # 3.3
print(type(a)) # <class 'float'>
```

* `a` es un [int](/entero-en-python)
* `b` es un [float](/float-python)

Pero si sumamos `a` y `b` y almacenamos el resultado en `a`, podemos ver como internamente Python ha convertido el [int](/entero-en-python) en [float](/float-python) para poder realizar la operación, y la variable resultante es [float](/float-python)

Sin embargo hay otros casos donde Python no es tan listo y no es capaz de realizar la conversión. Si intentamos sumar un [int](/entero-en-python) a un [string](/cadenas-python), tendremos un error `TypeError`.

```python
a = 1
b = "2.3"

c = a + b

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Si te das cuenta, es lógico que esto sea así, ya que en este caso `b` era `"2.3"`, pero ¿y si fuera `"Hola"`? ¿Cómo se podría sumar eso? No tiene sentido.

## Conversión explicita

Por otro lado, podemos hacer conversiones entre tipos o *cast* de manera explícita haciendo uso de diferentes funciones que nos proporciona Python. Las más usadas son las siguientes:

* float(), str(), int(), list(), set()
* Y algunas otras como hex(), oct() y bin()

### Convertir float a int

Para convertir de [float](/float-python) a [int](/entero-en-python) debemos usar `float()`. Pero mucho cuidado, ya que el tipo entero no puede almacena decimales, por lo que perderemos lo que haya después de la coma.

```python
a = 3.5
a = int(a)
print(a)
# Salida: 3
```

### Convertir float a string

Podemos convertir un [float](/float-python) a [string](/cadenas-python) con `str()`. Podemos ver en el siguiente código como cambia el tipo de `a` después de hacer el *cast*.

```python
a = 3.5
print(type(a)) # <class 'float'>
a = str(a)
print(type(a)) # <class 'str'>
```

### Convertir string a float

Podemos convertir un [string](/cadenas-python) a [float](/float-python) usando `float()`. Es importante notar que se usa el `.` como separador.

```python
a = "35.5"
print(float(a))
# Salida: 35.5
```

El siguiente código daría un error, dado que `,` no se reconoce por defecto como separador decimal.

```python
a = "35,5"
print(float(a))
# Salida: ValueError: could not convert string to float: '35,5'
```

Y por último, resulta obvio pensar que el siguiente código dará un error también.

```python
a = "Python"
print(float(a))
# Salida: ValueError: could not convert string to float: 'Python'
```

### Convertir string a int

Al igual que la conversión a [float](/float-python) del caso anterior, podemos convertir de [string](/cadenas-python) a [int](/entero-en-python) usando `int()`.
```python
a = "3"
print(type(a)) # <class 'str'>
a = int(a)
print(type(a)) # <class 'int'>
```

Cuidado ya que no es posible convertir a [int](/entero-en-python) cualquier valor.

```python
a = "Python"
a = int(a)
# ValueError: invalid literal for int() with base 10: 'Python'
```

### Convertir int a string

La conversión de [int](/entero-en-python) a [string](/cadenas-python) se puede realizar con `str()`.

A diferencia de otras conversiones, esta puede hacerse siempre, ya que cualquier valor entero que se nos ocurra poner en `a`, podrá ser convertido a [string](/cadenas-python).

```python
a = 10
print(type(a)) # <class 'int'>
a = str(a)
print(type(a)) # <class 'str'>
```


### Convertir a list

Es también posible hacer un *cast* a [lista](/listas-en-python), desde por ejemplo un [set](/sets-python). Para ello podemos usar `list()`.

```python
a = {1, 2, 3}
b = list(a)

print(type(a)) # <class 'set'>
print(type(b)) # <class 'list'>
```

### Convertir a set

Y de manera completamente análoga, podemos convertir de [lista](/listas-en-python) a [set](/sets-python) haciendo uso de `set()`.

```python
a = ["Python", "Mola"]
b = set(a)

print(type(a)) # <class 'list'>
print(type(b)) # <class 'set'>
```

Esperamos que esto haya servido para aclarar el concepto de *casts* o conversiones de tipos en Python. Es muy importante tener bien claro el tipo de datos con el que estamos trabajando en cada momento, ya que Python es un lenguaje con tipado dinámico, algo que puede ser una gran ventaja, pero también causa de muchos quebraderos de cabeza.

Y recuerda, la función `type()` es tu amiga.

Si quieres saber más, tal vez te interese el concepto de *duck typing*.
