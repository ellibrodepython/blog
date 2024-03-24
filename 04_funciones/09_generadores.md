---
layout: default
title: 📕 Generadores
parent: 🕹 04. Funciones
description: Te explicamos el uso de yield en Python y su uso para crear generadores o generators. Los generadores son una especie de función que puede ser creada en Python, y tienen la particularidad de que almacenan el estado entre llamadas. Uno de sus principales ventajas es que permite la generación de valores al vuelo, sin que todos estén almacenados en memoria.
order: 47
nav_order: h
permalink: /yield-python
---

# Generators en Python

Si alguna vez te has encontrado con una función en Python que no sólo tiene una sentencia `return`, sino que además devuelve un valor haciendo uso de `yield`, ya has visto lo que es un generador o *generator*. A continuación te explicamos cómo se crean, para qué sirven y sus ventajas. Es muy importante también no confundir los generadores con las corrutinas, que también usan `yield` pero de otra manera, sin embargo estas las dejamos para otro post.

Empecemos por lo básico. Seguramente ya sepas lo que es una función y cómo puede devolver un valor con `return`.


```python
def funcion():
    return 5
```

Como hemos explicado, los generadores usan `yield` en vez de `return`. Vamos a ver que pasaría si cambiamos el return por el yield.


```python
def generador():
    yield 5
```

Y ahora vamos a intentar llamar a las dos "funciones".


```python
print(funcion())
print(generador())
# Salida: 5
# Salida: <generator object generador at 0x103e7f0a0>
```

Podemos ver ya la primera diferencia al usar el `yield`. En el primer caso, se devuelve un 5, pero en el segundo lo que se devuelve es en realidad un objeto de la clase `generator`. En realidad el número 5 también puede ser accedido en el caso del generador, pero esto lo veremos más adelante.

Entonces, si una función contiene al menos una sentencia `yield`, se convertirá en una función generadora. Una función generadora se diferencia de una función normal en que tras ejecutar el `yield`, la función devuelve el control a quién la llamó, pero la función es pausada y el estado (valor de las variables) es guardado. Esto permite que su ejecución pueda ser reanudada más adelante.

## Iterando los Generadores

A continuación vamos a ver cómo acceder a los valores del generador. Para entenderlo mejor, te recomendamos que leas antes más acerca de [iterables e iteradores](/for-python/).

Otra de las características que hacen a los *generators* diferentes, es que pueden ser iterados, ya que codifican los métodos `__iter__()` y `__next__()`, por lo que podemos usar `next()` sobre ellos. Dado que son iterables, lanzan también un `StopIteration` cuando se ha llegado al final.

Volviendo al ejemplo anterior, vamos a ver como podemos usar el `next()`.


```python
a = generador()
print(next(a))
# Salida: 5
```

Como te prometimos antes, el 5 también se podía acceder ¿has visto?. Pero vamos a ver que pasa ahora si intentamos llamar otra vez a `next()`. Si recuerdas, sólo tenemos una llamada a `yield`.


```python
a = generador()
print(next(a))
print(next(a))
# Salida: 5
# Salida: Error! StopIteration:
```

Como era de esperar, tenemos una excepción del tipo `StopIteration`, ya que el generador no devuelve más valores. Esto se debe a que cada vez que usamos `next()` sobre el generador, se llama y se continúa su ejecución después del último `yield`. Y en este caso cómo no hay más código, no se generan más valores.

## Creando Generadores

Vamos a ver otro ejemplo más completo donde tengamos un generador que genere varios valores. En la siguiente función podemos ver como tenemos una variable `n` que incrementada en 1, y después retorna con `yield`. Lo que pasará aquí, es que el generador generará un total de tres valores.


```python
def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n
```

Y haciendo uso de `next()` al igual que hacíamos antes, podemos ver los valores que han sido generados. Lo que pasa por debajo, sería lo siguiente:
* Se entra en la función generadora, `n=1` y se devuelve ese valor. Como ya hemos visto, el estado de la función se guarda (el valor de `n` es guardado para la siguiente llamada)
* La segunda vez que usamos `next()` se entra otra vez en la función, pero se continúa su ejecución donde se dejó anteriormente. Se suma 1 a la `n` y se devuelve el nuevo valor.
* La tercera llamada, realiza lo mismo.
* Una cuarta llamada daría un error, ya que no hay más código que ejecutar.


```python
g = generador()
print(next(g))
print(next(g))
print(next(g))
# Salida: 1, 2, 3
```

Otra forma más cómoda de realizar lo mismo, sería usando un simple bucle for, ya que el generador es iterable.


```python
for i in generador():
    print(i)
# Salida: 1, 2, 3
```


## Forma alternativa

Los generadores también pueden ser creados de una forma mucho más sencilla y en una sola línea de código. Su sintaxis es similar a las *list comprehension*, pero cambiando el corchete `[]` por paréntesis `()`.

El ejemplo con *list comprehensions* sería el siguiente. Simplemente se generan los valores de una lista elevados al cuadrado.


```python
lista = [2, 4, 6, 8, 10]
al_cuadrado = [x**2 for x in lista]
print(al_cuadrado)
# [4, 16, 36, 64, 100]
```


Y su equivalente con generadores sería lo siguiente.


```python
al_cuadrado_generador = (x**2 for x in lista)
print(al_cuadrado_generador)
# Salida: <generator object <genexpr> at 0x103e803b8>
```

Y como hemos visto los valores pueden ser generados de la siguiente forma.


```python
for i in al_cuadrado_generador:
    print(i)
# Salda: 4, 16, 36, 64, 100
```

La diferencia entre el ejemplo usando *list compregensions* y *generators* es que en el caso de los generadores, los valores no están almacenados en memoria, sino que se van generando al vuelo. Esta es una de las principales ventajas de los generadores, ya que los elementos sólo son generados cuando se piden, lo que hace que sean mucho más eficientes en lo relativo a la memoria.

## Ventajas y ejemplos

Llegados a este punto tal vez te preguntes para qué sirven los generadores. Lo cierto es que aunque no existieran, podría realizarse lo mismo creando una clase que implemente los métodos `__iter__()` y `__next__()`. Veamos un ejemplo de una clase que genera los primeros 10 números (0,9) al cuadrado.


```python
class AlCuadrado:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 9:
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result
```

Y de la misma forma que usábamos los generadores, podemos usar nuestra clase `AlCuadrado`. Creamos un objeto de ella, y la iteramos. En cada iteración generará un nuevo valor nuevo hasta que se llegue al final.


```python
eleva_al_cuadrado = AlCuadrado()
for i in eleva_al_cuadrado:
    print(i)
#0,1,4,9,16,25,36,49,64,81
```

Sin embargo esta forma es un tanto larga y tal vez confusa. Como hemos visto antes, podemos llegar a hacer lo mismo en una sola línea de código. ¿Para que complicarse la vida?

Por otro lado, ya hemos mencionado que el uso de los generadores hace que no todos los valores estén almacenados en memoria sino que sean generados al vuelo. Vamos a ver un ejemplo donde se puede ver mejor. Supongamos que queremos sumar los primeros 100 números naturales ([referencia](https://wiki.python.org/moin/Generators)). Una opción podría ser crear una lista de todos ellos y después sumarla. En este caso, todos los valores son almacenados en memoria, algo que podría ser un problema si por ejemplo intentamos sumar los primeros 1e10 números.


```python
def primerosn(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums
    
print(sum(firstn(100)))
# Salida: 4950
```


Sin embargo, podemos realizar lo mismo con un generador. En este caso los valores serán generados uno por uno según se vayan necesitando.


```python
def primerosn(n):
    num = 0
    for i in range(n):
        yield num
        num += 1
print(sum(primerosn(100)))
# Salida 4950
```


Nótese que es un ejemplo con fines didácticos, por lo que si quieres hacer esto, la mejor manera sería usando un simple `range()` asumiendo que usas Python 3.


```python
print(sum(range(100)))
# Salida: 4950
```



