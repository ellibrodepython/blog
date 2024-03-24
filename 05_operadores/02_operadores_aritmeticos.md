---
layout: default
title: 📗 Operadores Aritméticos
parent: ➗ 05. Operadores
description: Los operadores aritméticos permiten realizar operaciones como la suma o la resta con valores numéricos, aunque en Python tienen la particularidad que algunos también están definidos sobre otros tipos.
order: 53
nav_order: b
permalink: /operadores-aritmeticos
---

# Operadores aritméticos
Los operadores aritméticos o *arithmetic operators* son los más comunes que nos podemos encontrar, y nos **permiten realizar operaciones aritméticas** sencillas, como pueden ser la suma, resta o exponente. A continuación, condensamos en la siguiente tabla todos ellos con un ejemplo, donde `x=10` y `y=3`.

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
<td>+</td>
<td>Suma</td>
<td>x + y = 13</td>
</tr>
<tr>
<td>-</td>
<td>Resta</td>
<td>x - y = 7</td>
</tr>
<tr>
<td>*</td>
<td>Multiplicación</td>
<td>x * y = 30</td>
</tr>
<tr>
<td>/</td>
<td>División</td>
<td>x/y = 3.333</td>
</tr>
<tr>
<td>%</td>
<td>Módulo</td>
<td>x%y = 1</td>
</tr>
<tr>
<td>**</td>
<td>Exponente</td>
<td>x ** y = 1000</td>
</tr>
<tr>
<td>//</td>
<td>Cociente</td>
<td>3</td>
</tr>
</tbody>
</table>


```python
x = 10; y = 3
print("Operadores aritméticos")
print("x+y =", x+y)   #13
print("x-y =", x-y)   #7
print("x*y =", x*y)   #30
print("x/y =", x/y)   #3.3333333333333335
print("x%y =", x%y)   #1
print("x**y =", x**y) #1000
print("x//y =", x//y) #3
```


## Operador +
El operador `+` suma los números presentes a la izquierda y derecha del operador. Recalcamos lo de números porque no tendría sentido sumar dos cadenas de texto, o dos listas, pero en Python es posible hacer este tipo de cosas.


```python
print(10 + 3) # 13
```



Es posible sumar también dos cadenas de texto, pero la suma no será aritmética, sino que se unirán ambas cadenas en una. También se pueden sumar dos listas, cuyo resultado es la unión de ambas.


```python
print("2" + "2")       # 22
print([1, 3] + [6, 7]) # [1, 3, 6, 7]
```



## Operador -
El operador `-` resta los números presentes a la izquierda y derecha del operador. A diferencia el operador `+` en este caso no podemos restar cadenas o listas.


```python
print(10 - 3) #7
```


## Operador *
El operador `*` multiplica los números presentes a la izquierda y derecha del operador.


```python
print(10 * 3) #30
```



Como también pasaba con el operador `+` podemos hacer cosas "raras" con `*`. Explicar porque pasan estas cosas es un poquito más complejo, por lo que lo dejamos para otro capítulo, donde explicaremos como definir el comportamiento de determinados operadores para nuestras clases.


```python
print("Hola" * 3) #HolaHolaHola
```



## Operador /
El operador `/` divide los números presentes a la izquierda y derecha del operador. Un aspecto importante a tener en cuenta es que si realizamos una división cuyo resultado no es entero (es decimal) podríamos tener problemas. En Python 3 esto no supone un problema porque el mismo se encarga de convertir los números y el resultado que se muestra si es decimal.


```python
print(10/3) #3.3333333333333335
print(1/2)  #0.5
```



Sin embargo, en Python 2, esto hubiera tenido un resultado diferente. El primer ejemplo `10/3=3` y el segundo `1/2=0`. El comportamiento realmente sería el de calcular el cociente y no la división.

<p class="alert alert-info">
<b>Para saber más:</b> Si quieres saber más acerca de este cambio del operador de división, puedes leer la <a href="https://www.python.org/dev/peps/pep-0238/"> la PEP238</a>
</p>


## Operador %
El operador `%` realiza la operación módulo entre los números presentes a la izquierda y la derecha. Se trata de calcular el resto de la división entera entre ambos números. Es decir, si dividimos 10 entre 3, el cociente sería 3 y el resto 1. Ese resto es lo que calcula el módulo.


```python
print(10%3) # 1
print(10%2) # 0
```



## Operador **
El operador `**` realiza el exponente del número a la izquierda elevado al número de la derecha.


```python
print(10**3) #1000
print(2**2)  #4
```



Si ya has usado alguna vez Python, tal vez hayas oido hablar de la librería `math`. En esta librería también tenemos una función llamada `pow()` que es equivalente al operador `**`.


```python
import math
print(math.pow(10, 3)) #1000.0
```



<p class="alert alert-info">
<b>Para saber más:</b> Puedes consultar más información de la librería math <a href="https://docs.python.org/3/library/math.html">en la documentación oficial de Python</a>
</p>


## Operador //
Por último, el operador `//` calcula el cociente de la división entre los números que están a su izquierda y derecha.


```python
print(10//3)  #3
print(10//10) #1
```



Tal vez te hayas dado cuenta que el operador cociente `//` está muy relacionado con el operador módulo `%`. Volviendo a las lecciones del colegio sobre la división, recordaremos que el Dividendo `D` es igual al divisor `d` multiplicado por el cociente `c` y sumado al resto `r`, es decir `D=d*c+r`. Se puede ver como en el siguiente ejemplo, `10//3` es el cociente y `10%3` es el resto. Al aplicar la fórmula, verificamos que efectivamente `10` era el dividendo.


```python
D = 10 # Número que queremos dividir
d = 3  # Número entre el que queremos dividir
print(3 * (10//3) + 10%3) # 10
```



## Orden de aplicación
En los ejemplos anteriores simplemente hemos aplicado un operador a dos números sin mezclarlos entre ellos. También es posible tener varios operadores en la misma línea de código, y en este caso es muy importante tener en cuenta las prioridades de cada operador y cual se aplica primero. Ante la duda siempre podemos usar paréntesis, ya que todo lo que está dentro de un paréntesis se evaluará conjuntamente, pero es importante saber las prioridades.

El orden de prioridad sería el siguiente para los operadores aritméticos, siendo el primero el de mayor prioridad:
* `()` Paréntesis
* `**` Exponente
* `-x` Negación
* `*` `/` `//` Multiplicación, División, Cociente, Módulo
* `+` `-` Suma, Resta


```python
print(10*(5+3)) # Con paréntesis se realiza primero la suma
# 80
print(10*5+3)   # Sin paréntesis se realiza primero la multiplicación
# 53
```




```python
print(3*3+2/5+5%4) # Primero se multiplica y divide, después se suma
#10.4
print(-2**4)       # Primero se hace la potencia, después se aplica el signo
#-16
```



<p class="alert alert-info">
<b>Para saber más:</b> Si quieres saber más sobre el orden de prioridad de diferentes operadores, <a href="https://docs.python.org/3/reference/expressions.html">aquí tienes la documentación oficial de Python </a>
</p>

