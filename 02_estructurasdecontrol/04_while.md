---
layout: default
title: 📗 Bucle while en Python
title_nav: 📗 Bucle while
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: Los bucles while en Python permiten ejecutar un bloque de código mientras se cumpla una determinada condición. Una vez la condición se deje de cumplir, se saldrá del bucle continuando con la ejecución normal.
order: 17
nav_order: d
permalink: /while-python
---

# Bucles while

Anteriormente hemos visto el uso del [if](/if-python) y el [for](/for-python) para modificar el flujo de ejecución del código. A continuación vemos otra forma de hacerlo con el `while`.

## While

El uso del `while` nos permite **ejecutar una sección de código repetidas veces**, de ahí su nombre. El código se ejecutará **mientras** una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Llamaremos **iteración** a una ejecución completa del bloque de código.

Cabe destacar que existe dos tipos de bucles, los que tienen un número de iteraciones **no definidas**, y los que tienen un número de iteraciones **definidas**. El `while` estaría dentro del primer tipo. Mas adelante veremos los `for`, que se engloban en el segundo.


```python
x = 5
while x > 0:
    x -=1
    print(x)

# Salida: 4,3,2,1,0
```


En el ejemplo anterior tenemos un caso sencillo de `while`. Tenemos una condición `x>0` y un bloque de código a ejecutar mientras dure esa condición `x-=1` y `print(x)`. Por lo tanto mientras que `x` sea mayor que 0, se ejecutará el código. Una vez se llega al final, se vuelve a empezar y si la condición se cumple, se ejecuta otra vez. En este caso se entra al bloque de código 5 veces, hasta que en la sexta, `x` vale cero y por lo tanto la condición ya no se cumple. Por lo tanto el `while` tiene dos partes:
* La **condición** que se tiene que cumplir para que se ejecute el código.
* El **bloque de código** que se ejecutará mientras la condición se cumpla.

Ten cuidado ya que un mal uso del `while` puede dar lugar a bucles infinitos y problemas. Cierto es que en algún caso tal vez nos interese tener un bucle infinito, pero salvo que estemos seguros de lo que estamos haciendo, hay que tener cuidado. Imaginemos que tenemos un bucle cuya condición siempre se cumple. Por ejemplo, si ponemos `True` en la condición del `while`, siempre que se evalúe esa expresión, el resultado será `True` y se ejecutará el bloque de código. Una vez llegado al final del bloque, se volverá a evaluar la condición, se cumplirá, y vuelta a empezar. No te recomiendo que ejecutes el siguiente código, pero puedes intentarlo.


```python
# No ejecutes esto, en serio
while True:
    print("Bucle infinito")
```

Es posible tener un `while` en una sola línea, algo muy útil si el bloque que queremos ejecutar es corto. En el caso de tener mas de una sentencia, las debemos separar con `;`.


```python
x = 5
while x > 0: x-=1; print(x)
```


También podemos usar otro tipo de operación dentro del `while`, como la que se muestra a continuación. En este caso tenemos una lista que mientras no este vacía, vamos eliminando su primer elemento.


```python
x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)
#['Dos', 'Tres']
#['Tres']
#[]
```

## Else y while

Algo no muy corriente en otros lenguajes de programación pero si en Python, es el uso de la cláusula `else` al final del `while`. Podemos ver el ejemplo anterior mezclado con el `else`. La sección de código que se encuentra dentro del `else`, se ejecutará cuando el bucle termine, pero solo si lo hace "por razones naturales". Es decir, si el bucle termina porque la condición se deja de cumplir, y no porque se ha hecho uso del `break`.


```python
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")
```



Podemos ver como si el bucle termina por el `break`, el `print()` no se ejecutará. Por lo tanto, se podría decir que si no hay realmente ninguna sentencia `break` dentro del bucle, tal vez no tenga mucho sentido el uso del `else`, ya que un bloque de código fuera del bucle cumplirá con la misma funcionalidad.


```python
x = 5
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")
```


## Bucles anidados

Ya hemos visto que los bucles `while` tienen una condición a evaluar y un bloque de código a ejecutar. Hemos visto ejemplos donde el bloque de código son operaciones sencillas como la resta `-`, pero podemos complicar un poco mas las cosas y meter otro bucle `while` dentro del primero. Es algo que resulta especialmente útil si por ejemplo queremos generar permutaciones de números, es decir, si queremos generar todas las combinaciones posibles. Imaginemos que queremos generar todas las combinaciones de de dos números hasta 2. Es decir, 0-0, 0-1, 0-2,... hasta 2-2.


```python
# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0
```


Vamos a analizara el ejemplo paso por paso. El primer bucle genera números del 0 al 2, lo que corresponde a la variable `i`. Por otro lado el segundo bucle genera también número del 0 al 2, almacenados en la variable `j`. Al tener un bucle dentro de otro, lo que pasa es que por cada `i` se generan 3 `j`. Muy importante no olvidar que al finalizar el bucle de la `j`, debemos resetear `j=0` para que en la siguiente iteración la condición de entrada se cumpla.

Podemos complicar las cosas aún más y tener tres bucles anidados, generando combinaciones de 3 elementos con número 0, 1, 2. En este caso tendremos desde 0,0,0 hasta 2,2,2.


```python
i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0
```


## Ejemplos while

Árbol de navidad en Python. Imprime un árbol de navidad formado con `*` haciendo uso del `while` y de la multiplicación de un entero por una cadena, cuyo resultado en Python es replicar la cadena.


```python
z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1
#      *     
#     ***    
#    *****   
#   *******  
#  *********
# ***********
```



Aunque esta no sea tal vez la mejor forma de iterar una cadena es un buen ejemplo para el uso del `while` e introducir el indexado de listas con `[]`, que veremos en otros capítulos.


```python
text = "Python"
i = 0
while i < len(text):
    print(text[:i + 1])
    i += 1
# P
# Py
# Pyt
# Pyth
# Pytho
# Python
```


Sucesión de **Fibonacci** en Python. En matemáticas, la sucesión de *fibonacci* es una sucesión infinita de números naturales, donde el siguiente es calculado sumando los dos anteriores.


```python
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b
#1, 1, 2, 3, 5, 8, 13, 21
```

