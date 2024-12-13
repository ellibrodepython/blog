---
layout: default
title: 📙 Nombrar Variables en Python
title_nav: 📙 Nombrando Variables
parent: 🚀 09. Test y Documentación
description: El uso del guión o barra baja en Python para nombrar variables, funciones o métodos modifica en ciertas ocasiones el comportamiento de los mismos. Existen varios tipos, como los métodos mágicos.
order: 86
nav_order: b
permalink: /guion-bajo-python
---

# Nombrando Variables en Python

Estoy seguro de que alguna vez has visto métodos, atributos o funciones que tienen algún tipo de guión o barra baja `_` en su nombre. La verdad que al principio puede resultar un poco confuso, ya algunos pueden tenerlo al principio otros pueden tener incluso doble barra baja y otros pueden tenerlo al principio y al final. Todo un lío. Veamos las posibilidades:
* Barra baja al principio `_nombre`
* Barra baja al final `nombre_`
* Doble barra baja al principio `__nombre`
* Doble barra baja al principio y final `__nombre__`
* Barra baja sin contenido `_`

Es importante notar que el uso de `_` puede significar dos cosas. Por un lado puede significar una **mera convención** que no alterará el comportamiento de nuestro código. Por otro lado, en algunos casos su uso **si modifica** el comportamiento y su uso es relevante. Lo vemos a continuación.

## Al inicio: _nombre

El uso de `_` antes del nombre de una variable, como podría ser `_mi_variable` no modifica el comportamiento del código. Su uso es una mera convención que ha sido acordada por los usuarios de Python, y que indica que esa variable **no debería ser accedida desde fuera de la clase**, pero puede serlo.


```python
class Clase:
    def __init__(self):
        self._variable = 10

mi_clase = Clase()

# No se debería hacer, pero se puede
mi_clase._variable # 10
```




Su uso si que puede modificar el comportamiento del código usado con funciones. Una función es definida con `_` no es importada por defecto si usamos `from x import *`.

## Al Final: nombre_

Para entender el uso de la barra baja al final de una variable o función, es importante saber que Python tiene un determinado conjunto de palabras reservadas o **keywords**. Estas palabras no pueden ser usadas, porque de serlo Python se confundiría y no sabría como interpretarlas. Si por el motivo que sea, queremos llamar a una variable con el mismo nombre que una palabra reservada, podemos hacer algo así como `class_`. El siguiente código muestra que pasa si intentamos usar una palabra reservada para llamar a una variable.


```python
#class = 5 # Error! class es una palabra reservada
```

Podemos usar `_` para solucionarlo. Nótese que a diferencia de otras formas de usar `_` en este caso **no modifica comportamiento**, por lo que su uso es arbitrario.


```python
class_ = 5
def_ = 10
```

## Doble al Principio: __nombre

A diferencia del uso de una sola barra baja, el uso de la doble `__` en un atributo o método hace que Python lo oculte al exterior. Existe un concepto muy interesante y particular de Python llamado **name mangling**, del que te recomendamos leer más.

Por lo tanto, en el siguiente ejemplo `__nombre` no será accesible desde el exterior de la clase. Por supuesto si que podría accederse desde la propia clase.


```python
class Clase:
    def __init__(self):
        self.__variable = 10

mi_clase = Clase()
#mi_clase.__variable # Error! No es accesible
```

## Doble al Principio y Final: __nombre__

Por último, el uso de `__` al principio y al final de un nombre tiene especial relevancia cuando es **aplicado a métodos**. De hecho, a lo largo de este post ya has visto el uso de `__init__` varias veces. Se trata de una forma que usa Python para designar a los conocidos como [métodos mágicos](/metodos-magicos-python) como pueden ser también el `__call__` o el `__le__`. Por norma general, es mejor no definir métodos propios con estos nombres, y limitarse a utilizar los que Python ya ofrece.


```python
class Clase:
    def __init__(self):
        print("Init")
```


## Descartando Variables con Barra Baja

Su uso suele ser común cuando queremos descartar una variable que por ejemplo pueda devolver una función. Veamos un ejemplo de una función que devuelve dos parámetros, la suma y la resta de dos variables.


```python
def sumayresta(a, b):
    return (a+b), (a-b)
```

Tal vez queramos sólo el valor de la suma y no nos interese el valor de la resta. Para ello podríamos hacer lo siguiente.


```python
suma, _ = sumayresta(5, 5)
# 10
```

Es una forma de decir "no me interesa esta variable", pero como no se puede dejar el hueco vacío, se usa `_` para rellenarlo.