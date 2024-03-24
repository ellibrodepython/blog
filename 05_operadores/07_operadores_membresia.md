---
layout: default
title: 📙 Operadores Membresía
parent: ➗ 05. Operadores
description: Los operadores de membresía en Python permiten saber si un elemento esta contenido en una secuencia, y son el in y not in.
order: 58
nav_order: g
permalink: /operadores-membresia
---

# Operadores de membresía

Los operadores de membresía o *membership operators* son operadores que nos **permiten saber si un elemento esta contenido en una secuencia**. Por ejemplo si un número está contenido en una lista de números.

<table class="table table-sm">
<thead>
<tr>
<th scope="col">Operador</th>
<th scope="col">Nombre</th>
<th scope="col">Ejemplo</th>
</tr>
</thead>
<tbody>
<tr>
<td>in</td>
<td>True si el elemento esta contenido</td>
<td>xxx</td>
</tr>
<tr>
<td>not in</td>
<td>False si el elemento no esta contenido</td>
<td>xxx</td>
</tr>
</tbody>
</table>

## Operador `in`

El operador `in` nos permite ver si un elemento esta contenido dentro de una secuencia, como podría ser una lista. En el siguiente ejemplo se ve un caso sencillo donde se verifica si `3` esta contenido en la lista `[1, 2, 3]`. Como efectivamente lo está, el resultado es `True`.


```python
print(3 in [1, 2, 3])
# True
```



Vamos a complicar las cosas un poco y explorar los límites del operador. Que pasaría si intentásemos hacer algo como lo que se ve en el siguiente ejemplo. Podría ser lógico pensar que `3 in 3` sería `True`, porque realmente si que parece que el 3 esta contenido en el segundo 3. Pues no, el siguiente código daría un error, diciendo que la clase `int` no es iterable. En otros capítulos exploraremos más acerca de esto. Por ahora nos basta con decir que el elemento a la derecha del `in` debe ser un objeto tipo lista


```python
#print(3 in 3) # Error! TypeError
```

Vamos a darle una última vuelta de tuerca. Podríamos también ver si una lista está contenida en otra lista. En este caso, la lista de la derecha del `in` es una lista embebida dentro de otra lista. Como `[1, 2]` está dentro de la segunda lista, el resultado es `True`


```python
print([1, 2] in [4, [1, 2], 7])
# True
```


## Operador `not in`

Por último, el operador `not in` realiza lo contrario al operador `in`. Verifica que un elemento no está contenido en otra secuencia. En el siguiente ejemplo se puede ver como `3` no es parte de la secuencia, por lo que el resultado es `False`


```python
print(3 not in [1, 2, 4, 5])
# True
```



La verdad que ambos operadores `in` y `not in` son muy útiles y nos ahorran mucho trabajo. Es importante tenerlo en cuenta, porque no otros lenguajes de programación no existen tales operadores, y debemos escribir código extra para obtener tal funcionalidad. Una forma de implementar nuestro operador `in` y `is not` con una función sería la siguiente. Simplemente iteramos la lista y si encontramos el elemento que estábamos buscando devolvemos `True`, de lo contrario `False`.


```python
a=3
lista=[1, 2, 3, 4, 5]

# Función que implementa "is" y "is not"
def estaContenido(a, lista):
for l in lista:
if a==l:
return True
return False

print(estaContenido(a, lista))
```



<p class="alert alert-info">
<b>Para saber más:</b> Te dejamos <a href="https://docs.python.org/3/reference/expressions.html#membership-test-operations">un enlace</a> a la documentación oficial acerca de los operadores de membresía.
</p>

