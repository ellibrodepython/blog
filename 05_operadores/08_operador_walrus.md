---
layout: default
title: Walrus Python
title_nav: 📙 Operador walrus
parent: ➗ 05. Operadores
description: El operador walrus fue introducido en Python 3.8 y se representa por dos puntos seguidos de un igual (:=). Su uso permite asignar y devolver una variable en la misma sentencia, y su nombre se debe a que el operador se parece a una morsa con sus colmillos (walrus significa morsa en Inglés).
order: 59
nav_order: h
permalink: /operador-walrus
---

# Operador Walrus

## Introducción

El operador walrus o *walrus operator* se introdujo con la [PEP572](https://www.python.org/dev/peps/pep-0572) en Python 3.8, y se trata de un operador de [asignación](/operadores-asignacion) con una funcionalidad extra que veremos a continuación. El operador se representa con dos puntos seguidos de un igual `:=`, lo que tiene cierto parecido a una morsa, siendo `:` los ojos y `=` los colmillos, por lo que de ahí viene su nombre (*walrus* significa morsa en Inglés).

El problema que dicho operador intenta resolver es el siguiente. Podemos simplificar las siguientes tres líneas de código.

```python
x = "Python"
print(x)
print(type(x))

# Salida:
# Python
# <class 'str'>
```

En sólo dos líneas. Como podemos ver, el uso de `:=` **asigna y devuelve** el contenido de la variable.
```python
print(x := "Python")
print(type(x))
# Python
# <class 'str'>
```

Para gente que venga de otros lenguajes de programación como `C`, tal vez le resulte raro este operador, ya que C permite realizar lo siguiente. Podemos ver como `(x = 5)` puede ser comparado con `== 5`. Sin embargo **esta sintaxis no es válida en Python**, y el operador wallrus es precisamente lo que intenta resolver.

```c
#include <stdio.h>
int main(){
    int x;
    if ((x = 5) == 5) {
        printf("Hola");
    }
    return 0;
}
```

## Ejemplos Operador Walrus

En el siguiente programa pedimos al usuario que introduzca un texto y lo vamos añadiendo a una lista hasta que el texto introducido sea "terminar". Sin el operador walrus se podría escribir de la siguiente forma.
```python
lista = []
entrada = input("Escribe algo: ")
while entrada != "terminar":
    lista.append(entrada)
    entrada = input("Escribe algo: ")
    
print(lista)
```

Sin embargo aprovechando que el operador walrus `:=` devuelve el contenido que es asignado, podemos usar `entrada` para comparar con `!= "terminar"`. Es decir, podemos unir la asignación `=` y la comparación en la misma línea. Esto nos permite ahorrar alguna línea de código.

```python
lista = []
while (entrada := input("Escribe algo: ")) != "terminar":
    lista.append(entrada)

print(lista)
```

También nos podemos ahorrar una línea de código si queremos primero asignar a una variable y luego emplear dicha variable en, por ejemplo, un [if](/if-python).
```python
a = 20*[1]
if (n := len(a)) > 10:
    print(f"La lista tiene {n} elementos (>10)")
```

Por otro lado puede ser útil cuando usemos [list comprehensions](/list-comprehension-python) donde el valor que usamos para filtrar es modificado y se necesita también en el cuerpo del bucle.
```python
resultado = [(x, y, x/y) for x in datos if (y := f(x)) > 0]
```

De manera similar, podemos reutilizar el resultado de una expresión evitando tener que volver a computarla.

```python
lista = [[y := f(x), x/y] for x in range(5)]
```

Puedes encontrar otros ejemplos en los siguientes enlaces:
* En la [documentación oficial](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions) de Python
* En la propia sección de ejemplos de la [PEP572](https://www.python.org/dev/peps/pep-0572/#examples).
* Y en este [pull request](https://github.com/python/cpython/pull/8122/files).


## Críticas Al Operador Walrus

El operador walrus ha recibido muchas críticas entre los desarrolladores de Python, principalmente porque aunque sea cierto que su uso puede ahorrarnos alguna línea de código, a veces empeora la legibilidad. No siempre menos código implica una mejora, sobre todo si se hace más complicado de leer.

Por otro lado, aunque el operador walrus sea muy similar al operador de asignación `=`, su uso no es consistente. Por ejemplo, el siguiente código no es correcto usando `:=`.

```python
# Incorrecto
class Example:
    [(j := i) for i in range(5)]
# SyntaxError: assignment expression within a comprehension cannot be used in a class body
```

De hecho, el propio creador *Christoph Groth* sugirió en el siguiente [hilo](https://mail.python.org/pipermail/python-ideas/2018-March/049409.html) que tal vez sería conveniente implementar el uso de `=` como en C/C++ (recuerda el ejemplo que hemos visto anteriormente). Si esto se llega a producir, no sabemos que podría pasar con el operador walrus, pero tal vez ya no sería necesario.