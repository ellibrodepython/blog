---
layout: default
title: 📗 Sintaxis en Python
title_nav: 📗 Sintaxis Básica
parent: 🕺🏻 01. Introducción
description: En esta introducción a Python te explicamos la sintaxis básica de este lenguaje de programación. Te ayudamos a dar tus primeros pasos en Python, explicando el uso de comentarios, paréntesis, operadores, palabras reservadas, alcance de las variables y uso de la función print.
order: 5
nav_order: d
permalink: /sintaxis-python
---

# Sintaxis Python
A continuación veremos la sintaxis de Python, viendo como podemos empezar a usar el lenguaje creando nuestras primeras variables y estructuras de control.

El termino sintaxis hace referencia al **conjunto de reglas que definen como se tiene que escribir el código en un determinado lenguaje de programación**. Es decir, hace referencia a la forma en la que debemos escribir las instrucciones para que el ordenador, o más bien lenguaje de programación, nos entienda.

En la mayoría de lenguajes existe una sintaxis común, como por ejemplo el uso de `=` para asignar un dato a una variable, o el uso de `{}` para designar bloques de código, pero Python tiene ciertas particularidades.

**La sintaxis es a la programación lo que la gramática es a los idiomas**. De la misma forma que la frase "Yo estamos aquí" no es correcta, el siguiente código en Python no sería correcto, ya que no respeta las normas del lenguaje.

```python
if ($variable){
    x=9;
}
```

Lo veremos a continuación en detalle, pero Python no soporta el uso de `$` ni hace falta terminar las líneas con `;` como en otros lenguajes, y tampoco hay que usar `{}` en estructuras de control como en el if.

Por otro lado, de la misma forma que un idioma no se habla con simplemente saber todas sus palabras, en la programación no basta con saber la sintaxis de un lenguaje para programar correctamente en él. Es cierto que sabiendo la sintaxis podremos empezar a programar y a hacer lo que queramos, pero **el uso de un lenguaje de programación va mucho más allá de la sintaxis**.

Para empezar a perderle el miedo a la sintaxis de Python, vamos a ver un ejemplo donde vemos [cadenas](/cadenas-python), [operadores aritméticos](/operadores-aritmeticos) y el uso del condicional [if](/if-python).

El siguiente código simplemente define tres valores `a`, `b` y `c`, realiza unas operaciones con ellos y muestra el resultado por pantalla.
```python
# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"

# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2

# Realizamos unas operaciones con a,b,c
d = (a + b) * c

# Definimos una variable booleana
imprimir = True

# Si imprimir, print()
if imprimir:
    print(x, d)

# Salida: El valor de (a+b)*c es 14
```

Como puedes observar, la sintaxis de Python es muy parecida al lenguaje natural o pseudocódigo, lo que hace que sea relativamente fácil de leer. Otra ventaja es que no necesitamos nada más, el código anterior puede ser ejecutado tal cual está. Si conoces otros lenguajes como `C` o `Java`, esto te resultará cómodo, ya que no es necesario crear la típica función `main()`.

## Comentarios

Los comentarios son bloques de texto usados para **comentar** el código. Es decir, para ofrecer a otros programadores o a nuestro *yo* futuro información relevante acerca del código que está escrito. A efectos prácticos, para Python es como si no existieran, ya que no son código propiamente dicho, solo anotaciones.

Los comentarios se inician con `#` y todo lo que vaya después en la misma línea será considerado un comentario.

```python
# Esto es un comentario
```

Al igual que en otros lenguajes de programación, podemos también comentar varias líneas de código. Para ello es necesario hacer uso de triples comillas bien sean simples `'''` o dobles `"""`. Es necesario usarlas para abrir el bloque del comentario y para cerrarlo.

```python
'''
Esto es un comentario
de varias líneas
de código
'''
```

## Indentación y bloques de código

En Python los bloques de código se representan con indentación, y aunque hay un poco de debate con respecto a usar tabulador o espacios, la norma general es usar **cuatro espacios**.

En el siguiente código tenemos un [condicional if](/if-python). Justo después tenemos un `print()` indentado con cuatro espacios. Por lo tanto, todo lo que tenga esa indentación pertenecerá al bloque del if.

```python
if True:
    print("True")
```

Esto es muy importante ya que el código anterior y el siguiente no son lo mismo. De hecho **el siguiente código daría un error** ya que el if no contiene ningún bloque de código, y eso es algo que no se puede hacer en Python.

```python
if True:
print("True")
```
Por otro lado, a diferencia de en otros lenguajes de programación, no es necesario utilizar `;` para terminar cada línea.

```python
# Otros lenguajes como C
# requieren de ; al final de cada línea
x = 10;
```

Sin embargo **en Python no es necesario**, basta con un salto de línea.
```python
x = 5
y = 10
```

Pero se puede usar el punto y coma `;` para tener dos sentencias en la misma línea.

```python
x = 5; y = 10
```

## Múltiples líneas
En algunas situaciones se puede dar el caso de que queramos tener una sola instrucción en varias línea de código. Uno de los motivos principales podría ser que fuera **demasiado larga**, y de hecho en la especificación [PEP8](/python-pep8) se recomienda que las líneas **no excedan los 79 caracteres**.

Haciendo uso de \ se puede **romper el código en varias líneas**, lo que en determinados casos hace que el código sea mucho más legible.
```python
x = 1 + 2 + 3 + 4 +\
    5 + 6 + 7 + 8
```
Si por lo contrario estamos dentro de un bloque rodeado con paréntesis `()`, bastaría con saltar a la siguiente línea.
```python
x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)
```

Se puede hacer lo mismo para [llamadas a funciones](/funciones-en-python/)

```python
def funcion(a, b, c):
    return a+b+c

d = funcion(10,
23,
3)
```


## Creando variables
Anteriormente ya hemos visto como crear una variable y asignarle un valor con el uso de `=`. Existen también otras formas de hacerlo de una manera un poco más sofisticada.

Podemos por ejemplo asignar el mismo valor a diferentes variables con el siguiente código.

```python
x = y = z = 10
```
O también podemos asignar varios valores separados por coma.
```python
x, y = 4, 2
x, y, z = 1, 2, 3
```


## Nombrando variables
Puedes nombrar a tus variables como quieras, pero es importante saber que las **mayúsculas y minúsculas son importantes**. Las variables `x` y `X` son distintas.

Por otro lado existen ciertas normas a la hora de nombrar variables:
* El nombre no puede empezar por un número
* No se permite el uso de guiones `-`
* Tampoco se permite el uso de espacios.

Se muestran unos ejemplos de nombres de variables válidos y no válidos.
```python
# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

# No válido
2variable = 10
var-iable = 10
var iable = 10
```

Una última condición para nombrar a una variable en Python, es **no usar nombres reservados para Python**. Las [palabras reservadas](/palabras-reservadas-python) son utilizadas por Python internamente, por lo que no podemos usarlas para nuestras variables o funciones.

```python
import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
```

De hecho con el siguiente comando puedes ver todas las palabras clave que no puedes usar.
```python
import keyword
print(keyword.kwlist)
```


## Uso de paréntesis
Python soporta todos los operadores matemáticos más comunes, conocidos como [operadores aritméticos](/operadores-aritmeticos/). Por lo tanto podemos realizar sumas, restas, multiplicaciones, exponentes (usando `**`) y otros que no vamos a explicar por ahora. En el siguiente ejemplo realizamos varias operaciones en la misma línea, y almacenamos su resultado en `y`.

```python
x = 10
y = x*3-3**10-2+3
```

Pero el comportamiento del código anterior y el siguiente es distinto, ya que el uso de paréntesis `()` da prioridad a unas operaciones sobre otras.

```python
x = 10
y = (x*3-3)**(10-2)+3
```

El uso de paréntesis no solo se aplica a los operadores aritméticos, sino que también pueden ser aplicados a otros operadores como los [relacionales](/operadores-relacionales/) o de [membresía](/operadores-membresia/) que vemos en otros posts.


## Variables y alcance
Un concepto muy importante cuando definimos una variable, es **saber el alcance o scope que tiene**. En el siguiente ejemplo la variable con valor 10 tiene un alcance **global** y la que tiene el valor 5 dentro de la función, tiene un alcance **local**. Esto significa que cuando hacemos `print(x)`, estamos accediendo a la variable global `x` y no a la `x` definida dentro de la función.

```python
x = 10

def funcion():
    x = 5

funcion()
print(x)
```

No te preocupes si no lo has entendido. Es un concepto un poco complicado de pillar al principio, pero lo veremos más adelante. Te recomendamos leer los siguientes posts para entender mejor las funciones y el alcance de las variables:
* [Funciones en Python y sus argumentos](/funciones-en-python/)
* [Paso por valor y por referencia](/paso-por-valor-y-referencia/)
* [Variable global en Python](/variable-global-python/)


## Uso de la función print()
Por último, en cualquier lenguaje de programación es importante saber lo que va pasando a medida que se ejecutan las diferentes instrucciones. Por ello, es interesante hacer uso de `print()` en diferentes secciones del código, ya que nos permiten ver el valor de las variables y diferente información útil.

Existen muchas formas de usar la función `print()` y te las explicamos en detalle [en este post](/cadenas-python/), pero por ahora basta con que sepas lo básico.

Como ya hemos visto se puede usar `print()` para imprimir por pantalla el texto que queramos.
```python
print("Esto es el contenido a imprimir")
```

También es posible imprimir el contenido de una variable.
```python
x = 10
print(x)
```

Y separando por comas `,` los valores, es posible imprimir el texto y el contenido de variables.

```python
x = 10
y = 20
print("Los valores x, y son:", x, y)
# Salida: Los valores x, y son: 10 20
```


 
