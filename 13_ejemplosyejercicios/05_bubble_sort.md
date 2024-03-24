---
layout: default
title: 📙 Bubble Sort en Python
parent: 🔬 13. Ejemplos y ejercicios
description: Bubble Sort en Python es un algoritmo de ordenación que permite ordenar listas de manera sencilla y sin requerir un extra de memoria. No es el algoritmo más eficiente pero si de los más sencillos, con una complejidad O(n^2) y O(n) en el mejor de los casos.
order: 96
nav_order: d
permalink: /bubble-sort
---

# Bubble Sort en Python


Imaginemos que tenemos una lista `x` con un determinado número de elementos y la **queremos ordenar de menor a mayor**. Para ello existen diferentes algoritmos de ordenación o *sorting*, cada uno con sus ventajas e inconvenientes en por ejemplo complejidad en *time* y *space*. Es decir, el tiempo que tardan en ejecutarse y la memoria que consumen.

Vamos a explicar el **bubble sort** en Python, y cómo implementarlo. No se trata del algoritmo más eficiente, pero si del más sencillo y podemos expresarlo en tan sólo 8 líneas de código Python como se muestra a continuación:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break

# Dada una lista desordenada                
x = [9, 8, 7, 5, 4, 3, 0]

# La ordenamos utilizando bubble sort
bubble_sort(x)
print(x)
# [0, 3, 4, 5, 7, 8, 9]
```

Como podemos ver, el algoritmo es de lo más simple. Itera la lista entera múltiples veces, tomando valores de dos en dos. En cada iteración compara cada par adyacente, y pone el más alto a la derecha. Hace esto a lo largo de toda la lista, por lo que acaba moviendo al número más alto al final de la misma. Repitiendo el mismo proceso varias pasadas, acabamos teniendo la lista ordenada.

Veamos lo que el algoritmo hace en cada iteración. Fíjate en la `↓` y como en cada iteración, ese número se va moviendo hacia el final, quedando ordenado. Podemos ver que en cada iteración, recorremos un elemento menos, ya que al quedar ordenado por la derecha, nos podemos ahorrar volver a comprar hasta el final. Por ejemplo, una vez hemos pasado el `9` desde el principio hasta el final, no es necesario volver a compararlo, ya que sabemos que es el más alto y ya está al final.

```
# Empezamos
# [9, 8, 7, 5, 4, 3, 0]

#     ↓
# [8, 9, 7, 5, 4, 3, 0]
# [8, 7, 9, 5, 4, 3, 0]
# [8, 7, 5, 9, 4, 3, 0]
# [8, 7, 5, 4, 9, 3, 0]
# [8, 7, 5, 4, 3, 9, 0]
# [8, 7, 5, 4, 3, 0, 9]

#     ↓
# [7, 8, 5, 4, 3, 0, 9]
# [7, 5, 8, 4, 3, 0, 9]
# [7, 5, 4, 8, 3, 0, 9]
# [7, 5, 4, 3, 8, 0, 9]
# [7, 5, 4, 3, 0, 8, 9]

#     ↓
# [5, 7, 4, 3, 0, 8, 9]
# [5, 4, 7, 3, 0, 8, 9]
# [5, 4, 3, 7, 0, 8, 9]
# [5, 4, 3, 0, 7, 8, 9]

#     ↓
# [4, 5, 3, 0, 7, 8, 9]
# [4, 3, 5, 0, 7, 8, 9]
# [4, 3, 0, 5, 7, 8, 9]

#     ↓
# [3, 4, 0, 5, 7, 8, 9]
# [3, 0, 4, 5, 7, 8, 9]

# [0, 3, 4, 5, 7, 8, 9]
```

Ahora vamos a desgranar el código. Para intercambiar o hacer un *swap* de dos elementos de la lista hacemos uso del [tuple unpacking](https://ellibrodepython.com/unpacking-python). Es decir, imaginemos que queremos mover el elemento `[0]` a la posición `[1]` y el `[1]` a la posición `[0]`. Se podría hacer de muchas formas pero Python nos ofrece el  que permite realizar el cambio en una sola línea:

```python
x = [1, 2]
x[1], x[0] = x[0], x[1]

print(x)
# [2, 1]
```

Por otro lado, el uso de `for j in range(0, n-i-1):` hace que en cada iteración recorramos un elemento menos, en vez de hasta el final. Dado que los últimos elementos ya están ordenados, esto nos ahorra comparaciones innecesarias. Es importante también el `-1` ya que al tomar elementos de dos en dos, sin él nos iríamos fuera de la lista.

Por último el uso de la variable `swapped` no ofrece una optimización muy interesante que en ciertas ocasiones puede mejorar la eficiencia de nuestro *bubble sort*. Cuando tenemos listas ya (o casi) ordenadas, esto reduce la cantidad de iteraciones necesarias. Es decir, imaginemos que tenemos la lista ya ordenada. Si hacemos una pasada y `swapped` es `False`, significa que no se ha realizado ningún intercambio, y por lo tanto podremos considerar nuestro trabajo completado, ya que la lista ya está ordenada. Con esta optimización reduciríamos de complejidad `O(N^2)` a `O(n)`.

Algunas características del *bubble sort*:
* Sencillo de implementar.
* No requiere de memoria extra.
* Complejidad de `O(n^2)`.
* Complejidad en el mejor de los casos de `O(n)`.
* Requiere `n*(n-1)/2` comparaciones.

