---
layout: default
title: 📕 Decoradores
parent: 🕹 04. Funciones
description: Los decoradores son funciones que modifican el comportamiento de otras funciones, ayudan a acortar nuestro código y hacen que sea más Pythonic. Si alguna vez has visto @, estás ante un decorador o decorator, bien sea uno que Python ofrece por defecto o uno que puede haber sido creado ex profeso.
order: 46
nav_order: g
permalink: /decoradores-python
---

# Decoradores

Los decoradores son funciones que **modifican el comportamiento de otras funciones**, ayudan a acortar nuestro código y hacen que sea más Pythonic. Si alguna vez has visto `@`, estás ante un decorador o decorator, bien sea uno que Python ofrece por defecto o uno que puede haber sido creado ex profeso.

Si aún no controlas las funciones te recomendamos que empieces [con este post](/funciones-en-python/ "con este post").

Veamos un ejemplo muy sencillo. Tenemos una función `suma()` que vamos a decorar usando `mi_decorador()`. Para ello, antes de la declaración de la función suma, hacemos uso de `@mi_decorador`.


```python
def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)

# Se va a llamar
# Entra en funcion suma
# Se ha llamado
```


Lo que realiza `mi_decorador()` es definir una nueva función que encapsula o envuelve la función que se pasa como entrada. Concretamente lo que hace es hace uso de dos `print()`, uno antes y otro después de la llamada la función.

Por lo tanto, cualquier función que use `@mi_decorador` tendrá dos print, uno y al principio y otro al final, dando igual lo que realmente haga la función.

Veamos otro ejemplo usando el decorador sobre otra función.


```python
@mi_decorador
def resta(a ,b):
    print("Entra en funcion resta")
    return a - b

resta(5, 3)

# Se va a llamar
# Entra en funcion resta
# Se ha llamado
```


Una vez entendido esto, vamos a entrar un poco más en detalle viendo como Python trata a las funciones, como se puede definir un decorador sin `@`, como se pueden pasar argumentos a los decoradores, y para finalizar, un ejemplo práctico.

## Definiendo decoradores

Antes de nada hay que entender que todo en Python es un objeto, incluso una función. De hecho se puede asignar una función a una variable. Nótese la diferencia entre:
* `di_hola()` llama a la función.
* `di_hola` hace referencia a la función, no la llama.


```python
def di_hola():
    print("Hola")
    
f1 = di_hola() # Llama a la función
f2 = di_hola   # Asigna a f2 la función

print(f1)      # None, di_hola no devuelve nada
print(f2)      # <function di_hola at 0x1077bf158>

#f1()          # Error! No es válido
f2()           # Llama a f2, que es di_hola()

del f2         # Borra el objeto que es la función 
#f2()          # Error! Ya no existe

di_hola()      # Ok. Sigue existiendo
```


Entendido esto, demos un paso más. En Python se pueden definir funciones dentro de otras funciones. La función `operaciones` define `suma()` y `resta()`, y dependiendo del parámetro de entrada `op`, se devolverá una u otra.


```python
def operaciones(op):
    def suma(a, b):
        return a + b
    def resta(a, b):
        return a - b
    
    if op == "suma":
        return suma
    elif op == "resta":
        return resta
    
funcion_suma = operaciones("suma")
print(funcion_suma(5, 7)) # 12

funcion_suma = operaciones("resta")
print(funcion_suma(5, 7)) # -2
```


Si llamamos a la función devuelta con dos operandos, se realizará una operación distinta en función de si se uso suma o resta.

Ahora ya podemos dar la última vuelta de tuerca y **escribir nuestro propio decorador** sin hacer uso de `@`. Por un lado tenemos el `decorador`, que recibe como entrada una función y devuelve otra función decorada. Por el otro la función `suma()` que queremos decorar.


```python
def decorador(func):
    def envoltorio_func(a, b):
        print("Decorador antes de llamar a la función")
        c = func(a, b)
        print("Decorador después de llamar a la función")
        return c
    return envoltorio_func

def suma(a, b):
    print("Dentro de suma")
    return a + b

# Nueva funcion decorada
funcion_decorada = decorador(suma)

funcion_decorada(5, 8)
```



Entonces, haciendo uso de `decorador` y pasando como entrada `suma`, recibimos una nueva función decorada con una funcionalidad nueva, lista para ser usada. Sería el equivalente al uso de `@`.

## Decoradores con parámetros

Tal vez quieras que tu decorador tenga algún parámetro de entrada para modificar su comportamiento. Se puede hacer envolviendo una vez más la función como se muestra a continuación.


```python
def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)
# Imprimer esto antes y después
# Entra en funcion suma
# Imprimer esto antes y después

```

Es importante recalcar que los ejemplos mostrados hasta ahora son didácticos, y no tienen mucha utilidad práctica. Veamos un ejemplo más práctico.

## Ejemplo: logger

Una de las utilidades más usadas de los decoradores son los **logger**. Su uso nos permite escribir en un fichero los resultados de ciertas operaciones, que funciones han sido llamadas, o cualquier información que en un futuro resulte útil para ver que ha pasado.

En el siguiente ejemplo tenemos un uso más completo del decorador `log()` que escribe en un fichero los resultados de las funciones que han sido llamadas.


```python
def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log')
def suma(a, b):
    return a + b

@log('ficherosalida.log')
def resta(a, b):
    return a - b

@log('ficherosalida.log')
def multiplicadivide(a, b, c):
    return a*b/c

suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)
```

Nótese que el decorador puede ser usado sobre funciones que tienen diferente número de parámetros de entrada, y su funcionalidad será siempre la misma. Escribir en el fichero pasado como parámetro los resultados de las operaciones.

## Ejemplo: Uso autorizado

Otro caso de uso muy importante y ampliamente usado en Flask, que es un framework de desarrollo web, es el uso de decoradores para asegurarse de que una función es llamada cuando el usuario se ha autenticado.

Realizando alguna simplificación, podríamos tener un decorador que requiriera que una variable `autenticado` fuera `True`. La función se ejecutará solo si dicha variable global es verdadera, y se dará un error de lo contrario.


```python
autenticado = True

def requiere_autenticación(f):
    def funcion_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return f(*args, **kwargs)
    return funcion_decorada

@requiere_autenticación
def di_hola():
    print("Hola")
    
di_hola()
```


Prueba a cambiar la variable de `True` a `False`.

Y esto es todo. En otros posts veremos el uso de `functools` y porque nos puede ser muy útil.
