---
layout: default
title: 📗 Operadores Lógicos
parent: ➗ 05. Operadores
description: Los operadores lógicos permiten trabajar con valores booleanos o binarios (0 o 1), realizando tres operaciones conocidas como and, or y not.
order: 55
nav_order: d
permalink: /operadores-logicos
---

# Operadores lógicos

Los operadores lógicos o *logical operators* nos **permiten trabajar con valores de tipo booleano**. Un valor booleano o `bool` es un tipo que solo puede tomar valores `True` o `False`. Por lo tanto, estos operadores nos permiten realizar diferentes operaciones con estos tipos, y su resultado será otro booleano. Por ejemplo, `True and True` usa el operador `and`, y su resultado será `True`. A continuación lo explicaremos mas en detalle.

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
<td>and</td>
<td>Devuelve True si ambos elementos son True</td>
<td>True and True = True</td>
</tr>
<tr>
<td>or</td>
<td>Devuelve True si al menos un elemento es True</td>
<td>True or False = True</td>
</tr>
<tr>
<td>not</td>
<td>Devuelve el contrario, True si es Falso y viceversa</td>
<td>not True = False</td>
</tr>
</tbody>
</table>

## Operador `and`

El operador `and` evalúa si el valor a la izquierda **y** el de la derecha son `True`, y en el caso de ser cierto, devuelve `True`. Si uno de los dos valores es `False`, el resultado será `False`. Es realmente un operador muy lógico e intuitivo que incluso usamos en la vida real. Si hace sol `y` es fin de semana, iré a la playa. Si ambas condiciones se cumplen, es decir que la variable `haceSol=True` y la variable `finDeSemana=True`, iré a la playa, o visto de otra forma `irALaPlaya=(haceSol and finDeSemana)`.


```python
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False
```



## Operador `or`

El operador `or` devuelve `True` cuando al menos uno de los elementos es igual a `True`. Es decir, evalúa si el valor a la izquierda **o** el de la derecha son `True`.


```python
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False
```




Es importante notar que varios operadores pueden ser usados conjuntamente, y salvo que existan paréntesis que indiquen una cierta prioridad, el primer operador que se evaluará será el `and`. En el ejemplo que se muestra a continuación, podemos ver que tenemos dos operadores `and`. Para calcular el resultado final, tenemos que empezar por el `and` calculando el resultado en grupos de dos y arrastrando el resultado hacia el siguiente grupo. El resultado del primer grupo sería `True` ya que estamos evaluando `True and True`. Después, nos guardamos ese `True` y vamos a por el siguiente y último elemento, que es `False`. Por lo tanto hacemos `True and False` por lo que el resultado final es `False`


```python
print(True and True and False)
#     |-----------|
#           True  and  False
#         |------------------|
#                False
```



También podemos mezclar los operadores. En el siguiente ejemplo empezamos por `False and True` que es `False`, después `False or True` que es `True` y por último `True or False` que es `True`. Es decir, el resultado final de toda esa expresión es `True`.


```python
print(False and True or True or False)
#     False and True = False
#               Fase or True = True
#                       True or False = True
# True
```



## Operador `not`

Y por último tenemos el operador `not`, que simplemente invierte `True` por `False` y `False` por `True`. También puedes usar varios `not` juntos y simplemente se irán aplicando uno tras otro. La verdad que es algo difícil de ver en la realidad, pero simplemente puedes contar el número de `not` y si es par el valor se quedará igual. Si por lo contrario es impar, el valor se invertirá.


```python
print(not True)  # False
print(not False) # True
print(not not not not True) # True
```



Dado que estamos tratando con booleanos, hemos considerado que usar `True` y `False` es lo mejor y más claro, pero es totalmente válido emplear `1` y `0` respectivamente para representar ambos estados. Y por supuesto los resultados no varían


```python
print(not 0) # True
print(not 1) # False
```



## Ejemplos

Antes de entrar con los ejemplos, es importante notar que el orden de aplicación de los operadores puede influir en el resultado, por lo que es importante tener muy claro su prioridad de aplicación. De mayor a menor prioridad, el primer sería `not`, seguido de `and` y `or`.

<p class="alert alert-info">
<b>Para saber más:</b> Puedes leer la especificación oficial si quieres saber el orden de aplicación de todos los operadores <a href="https://docs.python.org/3/reference/expressions.html#operator-precedence"> en este enlace</a>
</p>


Pero, imaginemos que no sabemos el orden de aplicación de los operadores. Vamos a intentar con ingeniería inversa descubrirlo con unos cuantos ejemplos. En el ejemplo que se muestra a continuación, habría dos posibilidades. La primera sería `(False and False) or True` cuyo resultado sería `True` y la segunda `False and (False or True)` cuyo resultado sería `False`. Dado que el resultado que `Python` da es `True`, podemos concluir que el equivalente es la primera opción, es decir que `and` tiene prioridad sobre el `or`


```python
print(False and False or True)
# True
```



Lo mismo con el siguiente ejemplo. Como ya sabemos de antes que `and` es evaluado primero, la siguiente expresión sería en realidad equivalente a `True or (False and False)` por lo que su resultado es `True`


```python
print(True or False and False)
# True
```



Como ya hemos indicado anteriormente, se puede usar `0` y `1` para representar `False` y `True` respectivamente. Veamos a usar esa representación para abreviar. Podemos simplificar la siguiente expresión, ya que el `not` es el operador que primer se aplica. Por lo tanto nos quedaría `0 and 0 or 1 and 1 or 1 and 0`. Y como ya sabemos, después se aplica el `and`, por lo que nos quedaría `(0 and 0) or (1 and 1) or (1 and 0)`. Y ya nos quedaría sólo aplicar el `or` de la expresión resultante `0 or 1 or 1`, por lo que el resultando final es `1` o `True`. Date cuenta que la expresión se podría simplificar, y una vez en un `or` nos encontramos que un lado es `True`, podríamos dejar de calcular el resto de la expresión ya que el resultado ya sería `True`


```python
print(0 and not 1 or 1 and not 0 or 1 and 0)
# True
```
