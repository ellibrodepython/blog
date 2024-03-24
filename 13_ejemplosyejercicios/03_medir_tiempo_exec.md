---
layout: default
title: 📙 Medir tiempo ejecución
parent: 🔬 13. Ejemplos y ejercicios
description: Puedes medir el tiempo de ejecución de tus programas en Python de diferentes maneras. Para fragmentos de código pequeños puedes usar timeit y para más largos time. Ambos paquetes vienen por defecto con Python.
order: 95
nav_order: c
permalink: /tiempo-ejecucion-python
---

# Medir tiempo de ejecución

Medir el tiempo de ejecución de un programa es una tarea muy importante, ya que programar no sólo consiste en crear código que funcione, sino código que pueda ser ejecutado en un tiempo razonable. ¿Te imaginas que consultar tu saldo en la web del banco tardase 5 horas?

Imagina que tienes un determinado algoritmo que tarda en ejecutarse 1 segundo. *A priori* no parece demasiado, pero ¿y si tuviéramos a 1000 usuarios ejecutando ese algoritmo periódicamente? En este caso, podría ser interesante optimizarlo, ya que una simple reducción de 0.1 segundos, podría aliviar la carga de nuestro sistema notablemente.

Por lo contrario, si tenemos un determinado algoritmo o proceso que tarda 1 segundo, pero es usado muy de vez en cuanto, tal vez no sea interesante invertir recursos en optimizarlo.

Afortunadamente, Python nos proporciona diferentes formas de medir el tiempo de ejecución de un programa.

## Tiempo de ejecución con time

La librería [time](https://docs.python.org/3/library/time.html) es bastante completa, pero lo único que nos interesa para medir el tiempo de ejecución es el método `time()`.

Este método nos devuelve el número de segundos, con precisión de microsegundos, que han pasado desde el 1 de Enero de 1970.

```python
import time
print(time.time()) # 1609954317.943479
```

Para medir el tiempo de ejecución de nuestros programas, **basta con saber el tiempo que ha pasado antes y después** de ejecutar nuestro programa, y la diferencia será el tiempo que ha tardado nuestro código.

```python
import time
inicio = time.time()

# Código a medir
time.sleep(1)
# -------------

fin = time.time()
print(fin-inicio) # 1.0005340576171875
```

En este caso podemos ver como el tiempo transcurrido es prácticamente `1`, ya que `time.sleep(1)` tarda 1 segundo en ejecutarse.

Podemos ver también el tiempo que tardamos en calcular los primeros `10000000` números pares.

```python
import time
inicio = time.time()

# Código a medir
lista = [i for i in range(10000000) if i%2==0]
# -------------

fin = time.time()
print(fin-inicio) # 1.5099220275878906
```

Por otro lado, también podemos crear un [decorador](/decoradores-python) que use `time`, lo que nos permitirá medir el tiempo de ejecución de nuestras funciones sin repetir tanto código. Creamos el decorador de la siguiente manera:

```python
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(time.time() - inicio)
        return c
    return funcion_medida
```

Ahora podemos usar el decorador `mide_tiempo` con `@` antes de nuestra función, y cada vez que la llamemos se imprimirá por pantalla el tiempo que tardó en ejecutarse.

```python
@mide_tiempo
def calcula_pares(n):
    return [i for i in range(n) if i%2 == 0]

calcula_pares(10000000)
# 1.4356
```

## Tiempo de ejecución con timeit

Python nos ofrece también otra librería denominada [timeit](https://docs.python.org/3/library/timeit.html), y está pensada para medir tiempos de ejecución de fragmentos pequeños de código. Puede ser usada por línea de comandos o como una función dentro de Python.

El siguiente fragmento de código nos permite medir el tiempo de ejecución de la sentencia `x=5`. El argumento `number` es el número de veces que se ejecuta el fragmento de código.

```python
import timeit
tiempo = timeit.timeit('x = 5', number=100000000)
print(tiempo) # 2.173444958
```

Es importante notar que el `tiempo` que se nos devuelve, es la suma de todas las ejecuciones. Es decir, el siguiente ejemplo tarda `2.17` segundos en ejecutar `x=5` un total de `100000000` veces.

En el siguiente ejemplo vemos como la siguiente [list comprehension](/list-comprehension-python) tarda en ejecutarse una media de `0.18` segundos.

```python
import timeit
tiempo = timeit.timeit('lista = [i for i in range(1000000) if i%2==0]', number=5)
# Calculamos el tiempo medio
print(tiempo/5) # 0.18671
```

# Consejos y conclusiones

* Para medir el tiempo de ejecución de tus programas, haz la media de varias ejecuciones. Debido a diferentes factores, nunca obtendrás el mismo resultado, por eso es importante realizar la media. Observa los diferentes valores que obtienes, y si son muy dispares, plantéate las cosas.
* Si mides fragmentos de código que tardan muy poco en ejecutarse, deberás promediar más valores.
* Ten en cuenta que dependiendo de tu sistema operativo, la precisión que obtendrás de las diferentes librerías puede variar.
* No pierdas tiempo en optimizar códigos que apenas son usados. Dedica tiempo a analizar el código que requiere de optimización y centra ahí tus esfuerzos.

