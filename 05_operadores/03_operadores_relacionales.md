---
layout: default
title: 📗 Operadores Relacionales
parent: ➗ 05. Operadores
description: Los operadores relacionales permiten saber la relación existente entre dos variables, devolviendo True o False en función de si la relación indicada se cumple o no.
order: 54
nav_order: c
permalink: /operadores-relacionales
---

# Operadores relacionales
Los operadores relacionales, o también llamados *comparison operators* nos permiten saber la **relación existente entre dos variables**. Se usan para saber si por ejemplo un número es mayor o menor que otro. Dado que estos operadores indican si se cumple o no una operación, el valor que devuelven es `True` o `False`. Veamos un ejemplo con `x=2` e `y=3`

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
<td>==</td>
<td>Igual</td>
<td>x == y = False</td>
</tr>
<tr>
<td>!=</td>
<td>Distinto</td>
<td>x != y = True</td>
</tr>
<tr>
<td>></td>
<td>Mayor</td>
<td>x > y = False</td>
</tr>
<tr>
<td>&lt</td>
<td>Menor</td>
<td>x &lt y = True</td>
</tr>
<tr>
<td>>=</td>
<td>Mayor o igual</td>
<td>x >= y = False</td>
</tr>
<tr>
<td>&lt=</td>
<td>Menor o igual</td>
<td>x &lt y = True</td>
</tr>
</tbody>
</table>


```python
x=2; y=3
print("Operadores Relacionales")
print("x==y =", x==y) # False
print("x!=y =", x!=y) # True
print("x>y  =", x>y)  # False
print("x<y  =", x<y)  # True
print("x>=y =", x>=y) # False
print("x<=y =", x<=y) # True
```


## Operador ==

El operador `==` permite comparar si las variables introducidas a su izquierda y derecha son iguales. Muy importante no confundir con `=`, que es el operador de asignación.


```python
print(4==4)          # True
print(4==5)          # False
print(4==4.0)        # True
print(0==False)      # True
print("asd"=="asd")  # True
print("asd"=="asdf") # False
print(2=="2")        # False
print([1, 2, 3] == [1, 2, 3]) # True
```



## Operador !=
El operador `!=` devuelve `True` si los elementos a comparar son iguales y `False` si estos son distintos. De hecho, una vez definido el operador `==`, no sería necesario ni explicar `!=` ya que hace exactamente lo contrario. Definido primero, definido el segundo. Es decir, si probamos con los mismos ejemplo que el apartado anterior, veremos como el resultado es el contrario, es decir `False` donde era `True` y viceversa.


```python
print(4!=4)          # False
print(4!=5)          # True
print(4!=4.0)        # False
print(0!=False)      # False
print("asd"!="asd")  # False
print("asd"!="asdf") # True
print(2!="2")        # True
print([1, 2, 3] != [1, 2, 3]) # False
```



## Operador >
El operador `>` devuelve `True` si el primer valor es mayor que el segundo y `False` de lo contrario.


```python
print(5>3) # True
print(5>5) # False
```



Algo bastante curioso, es como Python trata al tipo booleano. Por ejemplo, podemos ver como `True` es igual a `1`, por lo que podemos comprar el tipo `True` como si de un número se tratase.


```python
print(True==1)     # True
print(True>0.999)  # True
```



<p class="alert alert-info">
<b>Para saber más:</b> De hecho, el tipo bool en Python hereda de la clase int. Si quieres saber más acerca del tipo bool en Python puedes leer la <a href="https://www.python.org/dev/peps/pep-0285/"> PEP285</a>
</p>

También se pueden comparar listas. Si los elementos de la lista son numéricos, se comparará elemento a elemento.


```python
print([1, 2] > [10, 10]) # False
```



## Operador <
El operador `<` devuelve `True` si el primer elemento es mayor que el segundo. Es totalmente válido aplicar operadores relacionales como `<` sobre cadenas de texto, pero el comportamiento es un tanto difícil de ver a simple vista. Por ejemplo `abc` es menor que `abd` y `A` es menor que `a`


```python
print("abc" < "abd") # True
print("A"<"a")       # True
```



Para el caso de `A` y `a` la explicación es muy sencilla, ya que `Python` lo que en realidad está comparando es el valor entero `Unicode` que representa tal caracter. La función `ord()` nos da ese valor. Por lo tanto cuando hacemos `"A"<"a"` lo que en realidad hacemos es comprar dos números.


```python
print(ord('A')) # 65
print(ord('a')) # 97
```



<p class="alert alert-info">
<b>Para saber más:</b> En el <a href="http://docs.python.org/tutorial/datastructures.html#comparing-sequences-and-other-types"> siguiente enlace</a>  tienes más información de como Python compara variables que no son números.
</p>


## Operador >=

Similar a los anteriores, `>=` permite comparar si el primer elemento es mayor o igual que es segundo, devolviendo `True` en el caso de ser cierto.


```python
print(3>=3)           # True
print([3,4] >= [3,5]) # False
```



## Operdor <=

De la misma manera, `<=` devuelve `True` si el primer elemento es menor o igual que el segundo. Nos podemos encontrar con cosas interesantes debido a la precisión numérica existente al representar valores, como el siguiente ejemplo.


```python
print(3<=2.99999999999999999)
```
