---
layout: default
title: 📙 Operadores Identidad
parent: ➗ 05. Operadores
description: El operador de identidad o identity operator "is" nos indica si dos variables hacen referencia al mismo objeto, devolviendo True en el caso de ser cierto.
order: 57
nav_order: f
permalink: /operadores-identidad
---

# Operadores de Identidad

El operador de identidad o *identity operator* `is` nos indica si dos variables hacen referencia al mismo objeto. Esto implica que si dos variables distintas tienen el mismo `id()`, el resultado de aplicar el operador `is` sobre ellas será `True`.

<table class="table table-sm">
<thead>
<tr>
<th scope="col">Operador</th>
<th scope="col">Nombre</th>
</tr>
</thead>
<tbody>
<tr>
<td>is</td>
<td>Devuelve True si hacen referencia a el mismo objeto</td>
</tr>
<tr>
<td>is not</td>
<td>Devuelve False si no hacen referencia a el mismo objeto</td>
</tr>
</tbody>
</table>

## Operador `is`

El operador `is` comprueba si dos variables hacen referencia a el mismo objeto. En el siguiente ejemplo podemos ver como al aplicarse sobre `a` y `b` el resultado es `True`.


```python
a = 10
b = 10

print(a is b) # True
```

Esto es debido a que Python reutiliza el mismo objeto que almacena el valor 10 para ambas variables. De hecho, si usamos la función `id()`, podemos ver que el objeto es el mismo.

```python
print(id(a)) # 4397849536
print(id(b)) # 4397849536
```

Podemos ver como también, ambos valores son iguales con el [operador relacional](/operadores-relacionales) `==`, pero esto es una mera casualidad como veremos a continuación. Que dos variables tengan el mismo contenido, no implica necesariamente que hagan referencia a el mismo objeto.

```python
print(a == b) # True
```

En el siguiente ejemplo, podemos ver como `a` y `b` almacenan el mismo valor, por lo que `==` nos indica `True`.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True
print(a is b) # False
```

Sin embargo, por como Python funciona por debajo, almacena el contenido en dos objetos diferentes. Al tratarse de objetos diferentes, esto hace que el operador `is` devuelva `False`.

A diferencia de antes, podemos ver como la función `id()` en este caso nos devuelve un valor diferente.

```python
print(id(a)) # 4496626880
print(id(b)) # 4496626816
```

Esta diferencia puede resultar algo liosa, por lo que te recomendamos que leas más acerca de la [mutabilidad](/mutabilidad-python) en Python.


<p class="alert alert-info">
<b>Para saber más:</b> Si quieres saber más acerca del operador id() te dejamos <a href="https://docs.python.org/3/library/functions.html#id">este enlace</a> a la documentación oficial.
</p>


## Operador `is not`

Una vez definido `is`, es trivial definir `is not` porque es exactamente lo contrario. Devuelve `True` cuando ambas variables no hacen referencia al mismo objeto.

```python
# Python crea dos objetos diferentes, uno
# para cada lista. Las listas son mutables.
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b) # True
```

```python
# Python reutiliza el objeto que almacena 5
# por lo que ambas variables apuntan a el mismo
a = 5
b = 5

print(a is not b) # False
```

<p class="alert alert-info">
<b>Para saber más:</b> Te dejamos un <a href="https://docs.python.org/3/reference/expressions.html#is">enlace</a> muy interesante con más información sobre el is y is not.
</p>

