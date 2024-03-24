---
layout: default
title: 📙 Operadores Bitwise
parent: ➗ 05. Operadores
description: Los operadores bitwise o también conocidos como operadores de bit, permiten realizar operaciones con los números en representación binaria.
order: 56
nav_order: e
permalink: /operadores-bitwise
---

# Operadores bitwise

Los operadores a nivel de bit o *bitwise operators* son operadores que **actúan sobre números enteros pero usando su representación binaria**. Si aún no sabes como se representa un número en forma binaria, a continuación lo explicamos.

<table class="table table-sm">
<thead>
<tr>
<th scope="col">Operador</th>
<th scope="col">Nombre</th>
</tr>
</thead>
<tbody>
<tr>
<td>|</td>
<td>And bit a bit</td>
</tr>
<tr>
<td>&</td>
<td>Or bit a bit</td>
</tr>
<tr>
<td>~</td>
<td>Not bit a bit</td>
</tr>
<tr>
<td>^</td>
<td>Xor bit a bit</td>
</tr>
<tr>
<td>>></td>
<td>Desplazamiento a la derecha</td>
</tr>
<tr>
<td>&lt&lt</td>
<td>Desplazamiento a la izquierda</td>
</tr>
</tbody>
</table>

Para entender los operadores de bit, es importante antes entender como se representa un número de manera binaria. Todos estamos acostumbrados a lo que se denomina representación `decimal`. Se llama así porque se usan diez números, del `0` al `9` para representar todos los valores. Nuestro decimal, es también posicional, ya que no es lo mismo un `9` en `19` que en `98`. En el primer caso, el valor es de simplemente `9`, pero en el segundo, en realidad ese 9 vale `90`.

Lo mismo pasa con la representación binaria pero con algunas diferencias. La primera diferencia es que sólo existen dos posibles números, el `0` y el `1`. La segunda diferencia es que a pesar de ser un sistema que también es posicional, los valores no son como en el caso decimal, donde el valor se multiplica por `1` en la primera posición, `10` en la segunda, `100` en la tercera, y así sucesivamente. En el caso binario, los valores son potencias de 2, es decir `1, 2, 4, 8, 16` o lo que es lo mismo `$$2^0, 2^1, 2^2, 2^3, 2^4$$`


```python
# Sistema decimal
# 7264
# 7-> En realidad vale 7*1000 = 7000
#  2-> En relidad vale 2*100  = 200
#   6-> En reaidad vale 6*10  = 60
#     4 En realidad vale 4*1  = 4
#                           +---------
#           Sumando todo:       7264
```

Entonces por ejemplo el número en binario `11011` es en realidad el número `27` en decimal. Es posible convertir entre binario y decimal y viceversa. Para números pequeños se puede hacer mentalmente muy rápido, pero para números más grandes, os recomendamos hacer uso de alguna función en `Python`, como la función `bin()`


```python
# Sistema binario
# 11011
# 1->  En realidad vale 1*16    = 16
#  1->  En realidad vale 1*8    = 8
#    0->  En realidad vale 1*4  = 0
#     1->  En realidad vale 1*2 = 2
#      1->  En realidad vle 1*1 = 1
#                           +---------
#          Sumando todo          27
```

Usando la función `bin()` podemos convertir un número `decimal` en `binario`. Podemos comprobar como el número anterior `11011` es efectivamente `27` en decimal. Fíjate que al imprimirlo con `Python`, se añade el prefijo `0b` antes del número. Esto es muy importante, y nos permite identificar que estamos ante un número binario.


```python
print(bin(27))
# 0b11011
```



Ahora que ya sabemos como es la representación `binaria`, estamos ya en condiciones de continuar con los operadores a nivel de bit, que realizan operaciones sobre los bits de estos números binarios que acabamos de introducir.

## Operador `&`

El operador `&` realiza la operación que vimos en otros capítulos `and`, pero por cada bit existente en la representación binaria de los dos números que le introducimos. Es decir, recorre ambos números en su representación binaria elemento a elemento, y hace una operación `and` con cada uno de ellos. En el siguiente ejemplo se estaría haciendo lo siguiente. Primer elemento de `a` con primer elemento de `b`, sería `1 and 1` por lo que el resultado es `1`. Ese valor se almacena en la salida. Continuamos con el segundo `1 and 0` que es `0`, tercero `0 and 1` que es `0` y por último `1 and 1` que es `1`. Por lo tanto el número resultante es `0b1001`, lo que representa el `9` en decimal.


```python
a = 0b1101
b = 0b1011
print(bin(a & b))
#0b1001
```



## Operador `|`

El operador `|` realiza la operación `or` elemento a elemento con cada uno de los bits de los números que introducimos. En el siguiente ejemplo podemos ver como el resultado es `1111` ya que siempre uno de los dos elementos es `1`. Se harían las siguientes comparaciones `1 or 1`, `1 or 0`, `0 or 1` y `1 or 1`.


```python
a = 0b1101
b = 0b1011
print(bin(a | b))
# 0b1111
```



## Operador `~`

El operador `~` realiza la operación `not` sobre cada bit del número que le introducimos, es decir, invierte el valor de cada bit, poniendo los `0` a `1` y los `1` a `0`. El comportamiento en `Python` puede ser algo distinto del esperado. En el siguiente ejemplo, tenemos el número `40` que en binario es `101000`. Si hacemos `~101000` sería de esperar que como hemos dicho, se inviertan todos los bits y el resultado sea `010111`, pero en realidad el resultado es `101001`. Para entender porque pasa esto, te invitamos a leer más información sobre el complemento a uno y el complemento a dos.


```python
a = 40
print(bin(a))
print(bin(~a))
0b101000
-0b101001
```



<p class="alert alert-info">
<b>Para saber más:</b> Para entender este operador mejor, es necesario saber que es el complemento a uno y a dos. Te dejamos <a href="https://es.wikipedia.org/wiki/Complemento_a_uno">este enlace </a>con mas información.
</p>


Si vemos el resultado con números decimales, es equivalente a hacer `~a` sería `-a-1` como se puede ver en el siguiente ejemplo. En este caso, en vez de mostrar el valor binario mostramos el decimal, y se puede ver como efectivamente si `a=40`, tras aplicar el operador `~` el resultado es `-40-1`.


```python
a = 40
print(a)
print(~a)
```



## Operador `^`

El operador `^` realiza la función `xor` con cada bit de las dos variables que se le proporciona. Anteriormente en otros capítulos hemos hablado de la `and` o `or`, que son operadores bastante usados y comunes. Tal vez `xor` sea menos común, y lo que hace es devolver `True` o `1` cuando hay al menos un valor `True` pero no los dos. Es decir, solo devuelve `1` para las combinaciones `1,0` y `0,1` y `0` para las demás.


```python
x = 0b0110 ^ 0b1010
print(bin(x))
# 0 xor 1 = 1
# 1 xor 0 = 1
# 1 xor 1 = 0
# 0 xor 0 = 0
# 0b1100
```


<p class="alert alert-info">
<b>Para saber más:</b> Si quieres saber más sobre la puerta XOR, te dejamos <a href="https://es.wikipedia.org/wiki/Puerta_XOR">un enlace</a> donde se explica.
</p>


## Operador `>>`

El operador `>>` desplaza todos los bit `n` unidades a la derecha. Por lo tanto es necesario proporcionar dos parámetros, donde el primer es el número que se desplazará o *shift* y el segundo es el número de posiciones. En el siguiente ejemplo tenemos `1000` en binario, por lo que si aplicamos un `>>2`, deberemos mover cada bit `2` unidades a la derecha. Lo que queda por la izquierda se rellena con ceros, y lo que sale por la derecha se descarta. Por lo tanto `1000>>2` será `0010`. Es importante notar que `Python` por defecto elimina los ceros a la izquierda, ya que igual que en el sistema decimal, son irrelevantes.


```python
a=0b1000
print(bin(a>>2))
# 0b10
```



## Operador `<<`

El operador `<<` es análogo al `>>` con la diferencia que en este caso el desplazamiento es realizado a la izquierda. Por lo tanto si tenemos `0001` y desplazamos `<<3`, el resultado será `1000`.


```python
a=0b0001
print(bin(a<<3))
# 0b1000
```



Es importante que no nos dejemos engañar por el número de bits que ponemos a la entrada. Si por ejemplo desplazamos en `4` o en mas unidades nuestra variable `a` el número de bits que se nos mostrará también se incrementará. Con esto queremos destacar que aunque la entrada sean `4` bits, Python internamente rellena todo lo que está a la izquierda con ceros.


```python
a=0b0001
print(bin(a<<10))
# 0b10000000000
```

