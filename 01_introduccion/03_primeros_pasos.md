---
layout: default
title: 📗 Hola Mundo en Python
title_nav: 📗 Hola Mundo en Python
parent: 🕺🏻 01. Introducción
description: Te explicamos de forma fácil y sencilla como escribir tu primer programa en Python, el famoso Hola Mundo. Para ello basta con usar la función print() y pasarle como argumento de entrada la cadena Hola Mundo entre comillas.
order: 4
nav_order: c
permalink: /hola-mundo-python
---

# Primeros pasos en Python

A continuación te ayudamos a dar tus primeros pasos en Python. ¡Allá vamos!

## Hola mundo en Python

En cualquier introducción a un nuevo lenguaje de programación, no puede faltar el famoso *Hola Mundo*. Se trata del primer programa por el que se empieza, que consiste en programar una aplicación que muestra por pantalla ese texto. Si ejecutas el siguiente código, habrás cumplido el primer hito de la programación en Python.

```python
print("Hola Mundo")
```

Por lo tanto ya te puedes imaginar que la función `print()` sirve para imprimir valores por pantalla. Imprimirá todo lo que haya dentro de los paréntesis. Fácil ¿verdad? A diferencia de otros lenguajes de programación, en Python se puede hacer en 1 línea.


## Definiendo variables en Python

Vamos a complicar un poco más las cosas. Creemos una variable que almacene un número. A diferencia de otros lenguajes de programación, no es necesario decirle a Python el tipo de dato que queremos almacenar en `x`. En otros lenguajes es necesario especificar que `x` almacenará un valor entero, pero no es el caso. Python es muy listo y al ver el número `5`, sabrá de que tipo tiene que ser la `x`.

```python
x = 5
```

Ahora podemos juntar el `print()` que hemos visto con la `x` que hemos definido, para en vez de imprimir el *Hola Mundo*, imprimir el valor de la `x`.

```python
print(x)
# Salida: 5
```

En el anterior fragmento habrás visto el uso `#`. Se trata de la forma que tiene Python de crear los denominados comentarios. Un comentario es un texto que acompaña al código, pero que no es código propiamente dicho. Se usa para realizar anotaciones sobre el código, que puedan resultar útiles a otras personas. En nuestro caso, simplemente lo hemos usado para decirte que la salida de ese comando será `5`, ya que `x` valía 5.


## Sumando variables en Python

Vamos a sumar dos variables e imprimir su valor. Lo primero vamos a declararlas, con nombres `a` y `b`. Declarar una variable significa "crearla".

```python
# Declaramos las variables a, b
# y asignamos dos valores
a = 3
b = 7
```

Ahora Python ya conoce `a` y `b` y sus respectivos valores. Podemos hacer uso de `+` para sumarlos, y una vez más de `print()` para mostrar su valor por pantalla.

```python
print(a+b)
```

Es importante que sólo usemos variables que hayan sido definidas, porque de lo contrario tendremos un error. Si hacemos:

```python
print(z)
# NameError: name 'z' is not defined
```
Tendremos un error porque Python no sabe que es `z`, ya que no ha sido declarada con anterioridad.


## Ejemplo condicional

Podemos empezar a complicar un poco más las cosas con el uso de una sentencia condicional. Te lo explicamos más adelante en [este post sobre el if](/if-python/ "este post sobre el if").

El siguiente código hace uso del **if** para comprobar si la `a` es igual `==` a 10. Si lo es, se imprimirá "Es 10" y si no lo es "No es 10". Es importante el uso de `==`, que es el [operador relacional que veremos en otros posts](/operadores-relacionales/ "operador relacional que veremos en otros posts").

```python
a = 10
if a == 10:
    print("Es 10")
else:
    print("No es 10")
```

## Decimales y cadenas

De la misma forma que hemos visto que una variable puede almacenar un valor entero como `10`, es posible también almacenar otros tipos como [decimales](/tipos-numericos-float/ "decimales") o incluso [cadenas de texto](/cadenas-python/ "cadenas de texto").

Si queremos almacenar un valor decimal, basta con indicarlo usando la separación con `.`

```python
valor_decimal = 10.3234
```

Y si queremos almacenar una cadena, es necesario indicar su contenido entre comillas simples `'`o dobles `"`.

```python
mi_cadena = "Hola Mundo"
```

Esperamos que te haya resultado útil esta introducción, y con ella ya estas list@ para continuar al siguiente tutorial, donde veremos más acerca de la sintaxis de Python.
