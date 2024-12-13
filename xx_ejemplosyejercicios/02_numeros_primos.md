---
layout: default
title: 📙 Números primos
description: Los números primos son aquellos que sólo son divisibles por uno y por sí mismos. Por lo tanto los números 2, 3, 5, 7, 11 son primos. Puede implementarse de varias formas en Python, con bucles o de forma recursiva.
order: 94
nav_order: b
permalink: /numeros-primos-python
nav_exclude: true
---

# Números primos Python

Los números primos son aquellos que sólo son divisibles por uno y por sí mismos. Se entiende por divisible a que el resultado sea un número entero, es decir, no decimal.

Por lo tanto los números 2, 3, 5, 7, 11 **son primos**, ya que no hay ningún número que los pueda dividir de manera entera (excluyendo al 1 y al propio número)

Sin embargo, el número 10 **no es primo**, ya que se puede dividir por 2 y por 5.

Los números primos son un concepto un tanto enigmático y muy estudiado. Algunas teorías como la [Conjetura de Goldbach](https://es.wikipedia.org/wiki/Conjetura_de_Goldbach "Conjetura de Goldbach") son de lo más interesantes.

> Todo número entero mayor que 5 se puede escribir como suma de tres números primos.

Sabida ya la teoría, veamos como se puede implementar en Python una [función](/funciones-en-python) que calcule si un número es primo o no. Veremos dos formas, una usando bucles [for](/for-python) y otra empleando [recursividad](/recursividad).

## Números primos en Python (bucles)

Para implementar una calculadora de números primos en Python, lo primero es saber si dos números son divisibles. Usamos el operador módulo `%`.

```python
if D%d != 0:
    print("No es divisor")
```

El operador [módulo](/operadores-aritmeticos) nos devuelve el resto de la división entre dos números. Por lo tanto `5%3` es `2`. Es decir, si el resto es distinto de cero, decimos que `d` no es divisor de `D`.

Para determinar si un número es primo, iteramos todos los números desde `2` hasta nuestro número, comprobando si ese número `n` puede dividir al nuestro. En el momento en el que encontramos a un divisor, ya sabemos que no es primo y devolvemos `False`.

Si por lo contrario ningún número consigue dividir al nuestro, devolvemos `True` indicando que el número es primo.

```python
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
```

Veamos un ejemplo de cómo usar nuestra función.

```python
es_primo(13)   # Es primo
es_primo(14)   # No es primo 2 es divisor
es_primo(887)  # Es primo
es_primo(1001) # No es primo 7 es divisor
```


## Número primos en Python (recursividad)

Ciertos algoritmos que usan bucles, pueden ser implementados con [recursividad](/recursividad), es decir, haciendo uso de una función que se llama repetidas veces a sí misma.

La siguiente función se llama a sí misma comprueba si un número es divisible por otro, empezando por `n=2` hasta llegar al número en cuestión.

* Si `n` es mayor que  nuestro número, significa que ya hemos probado a dividir nuestro número con todos los anteriores, por lo que podemos considerar que **es primo**.
* Si el número no es divisible entre `n`, continuamos llamando a `es_primo` incrementando `n`.
* Si detectamos que el número es divisible por `n`, salimos de la función indicando que no es primo.

```python
def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False
```

Fíjate en lo siguiente:
* **Resulta fácil comprobar que un número no es primo**, ya que basta con encontrar un número que lo divida. Se puede ver a simple vista que `10029438` no es primo, ya que al ser par es divisible por 2.
* **Pero es difícil demostrar que un número es primo**, ya que es necesario comprobar que no es divisible por ninguno, y esto requiere de más esfuerzo.

Veamos como usar la función.

```python
es_primo(33) # No es primo 3 es divisor
es_primo(10000000175489) # No es primo 599 es divisor
```

Por último, es importante tener en cuenta que Python pone un cierto límite a las veces que una función puede ser llamada recursivamente. En algunos casos podrías encontrarte con un `RecursionError`, indicando que has superado el límite.

```python
es_primo(1009)
# RecursionError: maximum recursion depth exceeded in comparison
```