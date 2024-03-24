---
layout: default
title: 📗 Range en Python
title_nav: 📗 Range
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: El uso de range en Python nos permite generar secuencias de números, dados un inicio, un final y un salto.
order: 16
nav_order: c
permalink: /range-python
---

# Range en Python

## Uso del range

Uno de las iteraciones mas comunes que se realizan, es la de iterar un número entre por ejemplo 0 y `n`. Si ya programas, estoy seguro de que estas cansado de escribir esto, aunque sea en otro lenguaje. Pongamos que queremos iterar una variable `i` de 0 a 5. Haciendo uso de lo que hemos visto anteriormente, podríamos hacer lo siguiente.


```python
for i in (0, 1, 2, 3, 4, 5):
    print(i) #0, 1, 2, 3, 4, 5
```

Se trata de una solución que cumple con nuestro requisito. El contenido después del `in` se trata de una clase que como ya hemos visto antes, es iterable, y es de hecho una tupla. Sin embargo, hay otras formas de hacer esto en Python, haciendo uso del `range()`.


```python
for i in range(6):
    print(i) #0, 1, 2, 3, 4, 5
```


El `range()` genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro menos 1. En realidad, se pueden pasar hasta tres parámetros separados por coma, donde el primer es el inicio de la secuencia, el segundo el final y el tercero el salto que se desea entre números. Por defecto se empieza en 0 y el salto es de 1.


```python
#range(inicio, fin, salto)
```

Por lo tanto, si llamamos a `range()` con `(5,20,2)`, se generarán números de 5 a 20 de dos en dos. Un truco es que el `range()` se puede convertir en `list`.


```python
print(list(range(5, 20, 2)))
```


Y mezclándolo con el `for`, podemos hacer lo siguiente.


```python
for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19
```

Se pueden generar también secuencias inversas, empezando por un número mayor y terminando en uno menor, pero para ello el salto deberá ser negativo.


```python
for i in range (5, 0, -1):
    print(i) #5,4,3,2,1
```
