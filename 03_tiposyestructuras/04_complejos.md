---
layout: default
title: 📗 Números Complejos Python
title_nav: 📗 Números complejos
parent: 📦 03. Tipos y estructuras
description: Los números complejos son aquellos que se representan como una tupla de valores, uno real y otro imaginario. En Python se define un tipo para su representación.
order: 29
nav_order: d
permalink: /numeros-complejos
---

# ¿Qué son los números complejos?

En pocas palabras, los números complejos son aquellos que tienen dos partes:
* Una parte **real**, como por ejemplo `3` o `7.5`.
* Y otra **imaginaria**, como `5j` o `-7j`.

Como puedes ver, la parte imaginaria viene acompañada de `j`, aunque es también común usar la `i` (de imaginario). Un número complejo tiene la siguiente forma:

```python
parte_real + parte_imaginaria*j
```

Veamos unos ejemplos:

```python
a = 5 + 5j
b = 1.3 - 7j
```

También podemos tener un número complejo con parte real igual a cero.

```python
c = 10.3j
```

Una vez vistos cómo son, vamos a ponerlos en contexto con el resto de conjuntos numéricos:
* Los números **enteros** hacen referencia a los números naturales, es decir, todos aquellos números que no contienen parte decimal: 3, -1, 10.
* Los números **racionales** son el cociente de dos números naturales: 3/10, 7/9.
* Los números **irracionales** son aquellos que no pueden ser expresados como una fracción m/n. Por ejemplo, el número `pi` es irracional.
* Los números **reales** son el conjunto de todos los anteriores, es decir, cualquier número que se te ocurra sería un número real.
* Los números **imaginarios** son números reales acompañados de la constante `i` (a veces la `j` es usada indistintamente), como `4i` o `3.7i`.
* Y por último los números **complejos** son la suma de un número real y otro imaginario, dando lugar a los ya vistos `5+5j`.

Llegados a este punto, tal vez te preguntes ¿y qué es `i`? Pues bien, `i` es simplemente un nombre que se le da a la raíz cuadrada de `-1`, ya que si recuerdas, los números negativos no tienen raíces cuadradas. Esta notación se la debemos al famoso [Leonhard Euler](https://es.wikipedia.org/wiki/Leonhard_Euler).

Por lo tanto, la raíz cuadrada de `-5`, podría expresarse como `5i`, y aunque pueda parecer algo poco relevante, se trata de una herramienta muy potente en el mundo de las matemáticas, física e ingeniería.


# ¿Para qué sirven los números complejos?

Los números complejos son muy utilizados en las **telecomunicaciones** y **electrónica**, ya que son muy útiles para describir las ondas electromagnéticas y la corriente eléctrica.

También son usados en diferentes dominios de las matemáticas y en física, donde destaca su uso en la mecánica cuántica.

Un número complejo puede representarse en un plano, donde el eje `x` representa la parte real y el eje `y` la imaginaria. Es decir, se puede ver a un número complejo `5+5i` como un punto de coordenadas.

<center><img src="https://github.com/ellibrodepython/blog/blob/main/img/complejo1.png" style="width:50%"></center>

Una vez representado en esta gráfica, cualquier número complejo formará un ángulo con el eje `x`. Todo número complejo tiene también un módulo, que es la distancia que une el punto del origen de coordenadas `0+0i`.

Ahora sólo tienes que imaginarte a este punto dando vueltas a una determinada frecuencia alrededor del plano, y ya estarías describiendo a una onda sin haberte dado cuenta.


# Números complejos en Python

Los números complejos en Python pueden ser creados sin tener que importar ninguna librería. Basta con hacer lo siguiente:

```python
c = 3 + 5j
print(c)       #(3+5j)
print(type(c)) #<class 'complex'>
```

Podemos ver como la [clase](/programacion-orientada-a-objetos-python) que representa a los complejos en Python se llama `complex`. Una vez creado, es posible acceder a la parte real con `real` y a la imaginaria con `imag`.


```python
c = 3 + 5j
print(c.real) #3.0
print(c.imag) #5.0
```

También se puede crear un número complejo haciendo uso de `complex`, pero sin usar la `j`.

```python
c = complex(3,5)
print(c) #(3+5j)
```

# Operaciones con números complejos

Usando variables del tipo `complex`, podemos realizar las operaciones más comunes típicas de los números complejos.

## Suma de complejos

Para sumar números complejos, se suman las partes reales por un lado, y las imaginarias por otro.

```python
a = 1 + 3j
b = 4 + 1j
print(a+b) #(5+4j)
```

## Resta de complejos

Para restar, se restan las partes reales por un lado y las imaginarias por otro.

```python
a = 1 + 3j
b = 4 + 1j
print(a-b) #(-3+2j)
```

## Multiplicación de complejos

La multiplicación es algo más compleja. Si multiplicamos `a+bj` por `c+dj`, se puede demostrar fácilmente que el resultado es `(ac-bd)` para la parte real y `(ad+bc)` para la imaginaria.

```python
a = 1 + 3j
b = 4 + 1j
print(a*b) #(1+13j)
```

## División de complejos

También podemos hacer la división. Si quieres saber cómo se dividen dos números complejos y su demostración matemática, te dejamos [este enlace](https://www.superprof.es/diccionario/matematicas/aritmetica/division-complejos.html).

```python
a = 1 + 3j
b = 4 + 1j
print(a/b) #(0.41+0.64j)
```

## Conjugado de complejos

Por último, podemos realizar el conjugado de un número complejo en Python con el método `conjugate()`. Calcular el conjugado consiste en negar la parte imaginaria, es decir, cambiar si signo de `+` a `-` y viceversa.

```python
a = 1 + 1j
print(a.conjugate()) #(1-1j)
```

# Librería cmath

Si quieres realizar más operaciones con número complejos, tal vez quieras echar un vistazo a la librería [cmath](https://docs.python.org/3/library/cmath.html), que es mucho más completa, y compleja.

Algunas de las cosas que puedes hacer son las siguientes:
* Calcular la **fase**, que es el ángulo que forma el vector con el eje `x`, en radianes.
* Calcular la forma **polar**, es decir módulo y ángulo.

```python
import cmath

print(cmath.phase(complex(5, 0))) # 0.0
print(cmath.polar(complex(5, 5))) # (7.0710678118654755, 0.7853981633974483)
```
