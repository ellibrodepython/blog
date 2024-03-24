---
layout: default
title: 📙 Anotaciones en Funciones
parent: 🕹 04. Funciones
description: Las anotaciones en funciones o function annotations en Python permiten añadir información sobre los argumentos de entrada y salida de una función. Son comúnmente utilizados para indicar el tipo que el argumento debe tener (int, list, str), fueron introducidos en Python 3 y su uso es totalmente opcional. Son especialmente útiles en Python debido a que no tiene un tipado estático como otros lenguajes de programación.
order: 43
nav_order: d
permalink: /function-annotations
---

# Anotaciones en Funciones


## Function Annotations en Python

Las **anotaciones en funciones** o *function annotations* de Python nos permiten añadir el tipo de los argumentos de entrada y salida de una [función](/funciones-en-python). A continuación podemos ver un ejemplo con la función `suma()`, que recibe dos argumentos `a`, `b` y cuyo tipo se espera que sea [int](/entero-en-python).

```python
def suma(a: int, b: int) -> int:
    return a + b

print(suma(7, 3))
# Salida: 10
```

Sin embargo es muy importante notar que **Python ignora las anotaciones**. Es decir, son una mera nota en el código que indica el tipo esperado, pero el siguiente código no daría ningún error. Más adelante explicaremos cómo realizar el chequeo de tipos.

```python
suma(7.0, 3.0)
```

Las anotaciones en funciones fueron introducidas en la [PEP3107](https://www.python.org/dev/peps/pep-3107/) para Python 3, y más adelante se introdujo la [PEP484](https://www.python.org/dev/peps/pep-0484/) especificando la semántica que se debe usar.

## Motivación y Necesidad de las Anotaciones

Python es un lenguaje de programación con tipado dinámico y [duck typing](/duck-typing-python), lo que significa que los tipos ([int](/entero-en-python), [string](/cadenas-python), etc) le dan igual. Precisamente esto es lo que hace que el siguiente código funcione. La función `imprime` puede ser llamada con cualquier tipo, ya que Python no realiza ninguna comprobación del tipo de `var`.

```python
def imprime(var):
    print(var)

imprime(1.0)      # 1.0
imprime(3)        # 3
imprime("Python") # Python
```

Sin embargo, en ciertas ocasiones esto nos puede traer problemas. ¿Y si queremos que la función `imprime` sólo acepte que `var` sea de un tipo concreto? Pues bien, las **anotaciones en funciones** o *function annotations* como acabamos de ver nos permiten especificar los tipos que se esperan recibir.

## Ejemplos de Function Annotations

Antes de nada es importante notar que las anotaciones en funciones no definen *per se* una semántica propia. Es decir, podemos escribir lo que se nos ocurra después de cada argumento. Las anotaciones pueden ser accedidas usando `__annotations__`.

```python
def suma(a: 'parametro 1', b: 'parametro 2') -> 'retorno':
    return a + b

print(suma.__annotations__)
# Salida:
# {'a': 'parametro 1',
#  'b': 'parametro 2',
#  'return': 'retorno'}
```

Aunque como hemos dicho se puedan realizar anotaciones arbitrarias, suele ser común usar tipos de Python como [int](/entero-en-python), [str](/cadenas-python) o [float](/float-python). En el siguiente ejemplo podemos ver como se combina una anotación con un valor por defecto `[]`.


```python
def filtrar_pares(salida: 'list' = []) -> 'list':
    return [i for i in salida if i%2 == 0]

print(filtrar_pares([1, 2, 3, 4, 5, 6]))
# Salida: [2, 4, 6]
```

También es posible usar como anotaciones clases definidas por nosotros, como `ClaseA`.

```python
class ClaseA:
    pass

def funcion(a: ClaseA) -> ClaseA:
    return a

a = ClaseA()
funcion(a)
```

Por último, las anotaciones no están limitadas a los argumentos de las funciones, sino que también se pueden asignar a variables que declaremos.

```python
pi: float = 3.14

print(pi)
# Salida: 3.14
```

Sin embargo, como ya hemos visto anteriormente, Python no da error cuando los tipos no se corresponden como en el ejemplo anterior.

```python
# Ojo: No sería correcto, pero Python no da error
pi: int = 3.14

print(pi)
# Salida: 3.14
```

Entonces uno se puede preguntar, ¿y para que sirven las function annotation, si Python las ignora? Pues bien, aunque las ignore, tenemos herramientas que nos permiten saber cuando no se están respetando. Lo vemos a continuación con el análisis estático del código.


## Uso de mypy y Static Type Checking

Una primera forma de verificar que las funciones se llaman con los parámetros especificados por las anotaciones, sería lo siguiente. Sin embargo el error que obtendríamos sería en **tiempo de ejecución**. Es decir, nos encontraríamos con el error una vez el código estuviera ejecutándose. Por lo tanto, no recomendamos el uso del siguiente código.

```python
# Nota: Ejemplo didáctico, no recomendado
def suma(a: int, b: int) -> int:
    if isinstance(a, suma.__annotations__['a']) and isinstance(b, suma.__annotations__['b']):
        return a + b
    else:
        raise Exception("Error de tipos")

print(suma(7, 3))
# Salida: 10

print(suma(7.0, 3.0))
# Salida: Exception: Error de tipos
```

Afortunadamente, tenemos herramientas como `mypy` que nos permiten hacer un **chequeo estático de los tipos**, obteniendo el error antes de que el código se ejecute. Lo podemos instalar de la siguiente manera.

```console
$ pip instal mypy
```

Y volviendo al ejemplo anterior de la `suma`, podemos ver como el siguiente código si que pasaría los checks de `mypy`.

```python
# suma_correcta.py
def suma(a: int, b: int) -> int:
    return a + b

print(suma(7, 3))
```

```console
$ mypy suma_correcta.py 
Success: no issues found in 1 source file
```

Sin embargo si cambiamos los tipos de los parámetros de entrada, obtendremos un error.

```python
# suma_incorrecta.py
def suma(a: int, b: int) -> int:
    return a + b

print(suma(7.0, "3"))
```

```console
$ mypy suma_incorrecta.py
suma_incorrecta.py:5: error: Argument 1 to "suma" has incompatible type "float"; expected "int"
suma_incorrecta.py:5: error: Argument 2 to "suma" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)
```

Como hemos indicado, la ventaja de `mypy` es que realiza un análisis estático, es decir, sin ejecutar el código. Esto es algo muy importante ya que si de verdad queremos reforzar que se verifiquen los tipos, no tendría mucho sentido hacerlo en tiempo de ejecución, ya que sería demasiado tarde y tendríamos un error.
