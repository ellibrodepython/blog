---
layout: default
title: 📗 Excepciones en Python
parent: 🛠 07. Excepciones
description: Las excepciones son una herramienta que la mayoría de los lenguajes de programación tienen, y que permiten tratar los posibles errores que ocurren en tiempo de ejecución de una manera determinada, evitando que el programa se pare abruptamente.
order: 75
nav_order: a
permalink: /excepciones-try-except-finally
---


# Excepciones en Python

Las excepciones en Python son una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. Se trata de una **forma de controlar el comportamiento de un programa cuando se produce un error**.

Esto es muy importante ya que salvo que tratemos este error, **el programa se parará**, y esto es algo que en determinadas aplicaciones no es una opción válida.

Imaginemos que tenemos el siguiente código con dos variables `a` y `b` y realizamos su división `a/b`.


```python
a = 4
b = 2
c = a/b
```

Pero imaginemos ahora que por cualquier motivo las variables tienen otro valor, y que por ejemplo `b` tiene el valor `0`. Si intentamos hacer la división entre cero, **este programa dará un error** y su ejecución terminará de manera abrupta.


```python
a = 4; b = 0
print(a/b)
# ZeroDivisionError: division by zero
```

Ese "error" que decimos que ha ocurrido es lanzado por Python (*raise* en Inglés) ya que la división entre cero es una operación que matemáticamente no está definida.

Se trata de la excepción `ZeroDivisionError`. En [el siguiente enlace](https://docs.python.org/3/library/exceptions.html "el siguiente enlace"), tenemos un listado de todas las excepciones con las que nos podemos encontrar.

Veamos un ejemplo con otra excepción. ¿Que pasaría si intentásemos sumar un número con un texto? Evidentemente esto no tiene ningún sentido, y Python define una excepción para esto llamada `TypeError`.


```python
print(2 + "2")
```


En base a esto es **muy importante controlar las excepciones**, porque por muchas comprobaciones que realicemos es posible que en algún momento ocurra una, y si no se hace nada **el programa se parará**.

¿Te imaginas que en un avión, un tren o un cajero automático tiene un error que lanza `raise` una excepción y se detiene por completo?

Una primera aproximación al control de excepciones podría ser el siguiente ejemplo. Podemos realizar una comprobación manual de que no estamos dividiendo por cero, para así evitar tener un error tipo `ZeroDivisionError`.

Sin embargo es complicado escribir código que contemple y que prevenga todo tipo de excepciones. Para ello, veremos más adelante el uso de `except`.

```python
a = 5
b = 0
# A través de esta comprobación prevenimos que se divida entre cero.
if b!=0:
    print(a/b)
else:
    print("No se puede dividir!")
```

## Uso de raise

También podemos ser nosotros los que levantemos o lancemos una excepción. Volviendo a los ejemplos usados en el apartado anterior, **podemos ser nosotros los que levantemos** `ZeroDivisionError` o `NameError` usando `raise`. La sintaxis es muy fácil.


```python
raise ZeroDivisionError("Información de la excepción")
```


O podemos lanzar otra de tipo `NameError`.


```python
raise NameError("Información de la excepción")
```


Se puede ver como el `string` que hemos pasado se imprime a continuación de la excepción. Se puede llamar también sin ningún parámetro como se hace a continuación.


```python
raise ZeroDivisionError
```

Visto esto, ya sabemos como una excepción puede ser lanzada. Existen dos maneras principalmente:
* Hacemos una operación que no puede ser realizada (como dividir por cero). En este caso Python se encarga de lanzar automáticamente la excepción.
* O también podemos lanzar nosotros una excepción manualmente, usando `raise`.
* Habría un tercer caso que sería lanzar una excepción que no pertenece a las definidas por defecto en Python. Pero eso [te lo explicamos aquí](/definir-excepcion/ "te lo explicamos aquí").

A continuación veremos que podemos hacer para controlar estas excepciones, y que hacer cuando se lanza una para que no se interrumpa la ejecución del programa.


## Uso de try y except

La buena noticia es que las excepciones que hemos visto antes, **pueden ser capturadas** y manejadas adecuadamente, **sin que el programa se detenga**. Veamos un ejemplo con la división entre cero.


```python
a = 5; b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("No se ha podido realizar la división")
```

En este caso no verificamos que `b!=0`. Directamente intentamos realizar la división y en el caso de que se lance la excepción `ZeroDivisionError`, la capturamos y la tratamos adecuadamente.

La diferencia con el ejemplo anterior es que ahora no se para el programa y se puede seguir ejecutando. Prueba a ejecutar el código y ver que pasa. Verás como el programa ya no se para.

Entonces, lo que hay dentro del `try` es la sección del código que podría lanzar la excepción que se está capturando en el `except`. Por lo tanto cuando ocurra una excepción, se entra en el `except` pero **el programa no se para**.

<p align="center">
  <img src="/wp-content/uploads/2020/05/image-1590050192892.png">
</p>

También se puede capturar diferentes excepciones como se ve en el siguiente ejemplo.


```python
try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except TypeError:
    print("Problema de tipos!")
```

Puedes también hacer que un determinado número de excepciones se traten de la misma manera con el mismo bloque de código. Sin embargo suele ser más interesante tratar a diferentes excepciones de diference manera.


```python
try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except (ZeroDivisionError, TypeError):
    print("Excepcion ZeroDivisionError/TypeError")
```

Otra forma si no sabes que excepción puede saltar, puedes usar la clase genérica  `Exception`. En este caso se controla cualquier tipo de excepción. De hecho todas las excepciones heredan de `Exception`. [Ver documentación](https://docs.python.org/3/library/exceptions.html "Ver documentación").


```python
try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception:
    print("Ha habido una excepción")
```

No obstante hay una forma de saber que excepción ha sido la que ha ocurrido.


```python
try:
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception as ex:
    print("Ha habido una excepción", type(ex))

# Ha habido una excepción <class 'TypeError'>
```


## Uso de else

Al ya explicado `try` y `except` le podemos añadir un bloque más, el `else`. Dicho bloque **se ejecutará si no ha ocurrido ninguna excepción**. Fíjate en la diferencia entre los siguientes códigos.

<p align="center">
  <img src="/wp-content/uploads/2020/05/image-1590050215188.png">
</p>

```python
try:
    # Forzamos una excepción al dividir entre 0
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

#Entra en except, ha ocurrido una excepción
```



Sin embargo en el siguiente código la división se puede realizar sin problema, por lo que el bloque `except` no se ejecuta pero el `else` si es ejecutado.


```python
try:
    # La división puede realizarse sin problema
    x = 2/2
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")

#Entra en else, no ha ocurrido ninguna excepción
```


## Uso de finally

A los ya vistos bloques `try`, `except` y `else` podemos añadir un bloque más, el `finally`. Dicho bloque **se ejecuta siempre**, haya o no haya habido excepción.

Este bloque se suele usar si queremos ejecutar algún tipo de **acción de limpieza**. Si por ejemplo estamos escribiendo datos en un fichero pero ocurre una excepción, tal vez queramos borrar el contenido que hemos escrito con anterioridad, para no dejar datos inconsistenes en el fichero.

<p align="center">
  <img src="/wp-content/uploads/2020/05/image-1590050229328.png">
</p>

En el siguiente código vemos un ejemplo. Haya o no haya excepción el código que haya dentro de `finally` será ejecutado.


```python
try:
    # Forzamos excepción
    x = 2/0
except:
    # Se entra ya que ha habido una excepción
    print("Entra en except, ha ocurrido una excepción")
finally:
    # También entra porque finally es ejecutado siempre
    print("Entra en finally, se ejecuta el bloque finally")

#Entra en except, ha ocurrido una excepción
#Entra en finally, se ejecuta el bloque finally
```


## Ejemplos

Un ejemplo muy típico de excepciones es en el **manejo de ficheros**. Se intenta abrir, pero se captura una posible excepción. De hecho si entras en la documentación de [open](https://docs.python.org/3/library/functions.html#open "open") se indica que `OSError` es lanzada si el fichero no puede ser abierto.


```python
# Se intenta abrir un fichero y se captura una posible excepción
try:
    with open('fichero.txt') as file:
        read_data = file.read()
except:
    # Se entra aquí si no pudo ser abierto
    print('No se pudo abrir')
```


Como ya hemos comentado, en el `except` también se puede capturar una excepción concreta. Dependiendo de nuestro programa, tal vez queramos tratar de manera distinta diferentes tipos de excepciones, por lo que es una buena práctica especificar que tipo de excepción estamos tratando.


```python
# Se intenta abrir un fichero y se captura una posible excepción
try:
    with open('fichero.txt') as file:
        read_data = file.read()
# Capturamos una excepción concreta
except OSError:
    print('OSError. No se pudo abrir')
```


En este otro ejemplo vemos el uso de los bloques `try`, `except`, `else` y `finally` todos juntos.


```python
try:
    # Se fuerza excepción
    x = 2/0
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en el else, no ha ocurrido ninguna excepción")
finally:
    print("Entra en finally, se ejecuta el bloque finally")
```


También se puede capturar una excepción de tipo `SyntaxError`, que hace referencia a errores de sintaxis. Sin embargo el código debería estar libre de este tipo de fallos, por lo que tal vez nunca deberías usar esto.


```python
try:
    print("Hola"))
except SyntaxError:
    print("Hay un error de sintaxis")
```
