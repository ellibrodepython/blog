---
layout: default
title: 📙 Continue en Python
title_nav: 📙 Continue
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: La sentencia continue en Python nos permite modificar el comportamiento de los bucles, saltando el código restante de la iteración actual y pasando a la siguiente en el caso de que haya.
order: 20
nav_order: h
permalink: /continue-python
---

# Sentencia continue

## Introducción al continue

El uso de `continue` al igual que el ya visto [break](/break-python), nos permite modificar el comportamiento de de los bucles [while](/while-python) y [for](/for-python).

Concretamente, `continue` se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.

La diferencia entre el `break` y `continue` es que el `continue` no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.

En el siguiente ejemplo vemos como al encontrar la letra `P` se llama al continue, lo que hace que se salte el `print()`. Es por ello por lo que no vemos la letra `P` impresa en pantalla.


```python
cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)
# Salida:
# y
# t
# h
# o
# n
```
 
A diferencia del `break`, el `continue` no rompe el bucle sino que finaliza la iteración actual, haciendo que todo el código que va después se salte, y se vuelva al principio a evaluar la condición.

En el siguiente ejemplo podemos ver como cuando la `x` vale 3, se llama al `continue`, lo que hace que se salte el resto de código de la iteración (el `print()`). Por ello, vemos como el número 3 no se imprime en pantalla.


```python
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

#Salida: 4, 2, 1, 0
```
