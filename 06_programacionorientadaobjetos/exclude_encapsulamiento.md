---
layout: default
title: 📗 Encapsulamiento
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: El encapsulamiento o encapsulación en programación es un concepto relacionado con la programación orientada a objetos, y hace referencia al ocultamiento de los estado internos de una clase al exterior. Dicho de otra manera, encapsular consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.
order: 71
nav_order: k
nav_exclude: true
permalink: /encapsulamiento-poo
---

# Encapsulamiento en programación

El encapsulamiento o encapsulación en programación es un concepto relacionado con la programación orientada a objetos, y hace referencia al ocultamiento de los estado internos de una clase al exterior. Dicho de otra manera, encapsular consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.

Para la gente que conozca Java, le resultará un termino muy familiar, pero en Python es algo distinto. Digamos que Python por defecto no oculta los atributos y métodos de una clase al exterior. Veamos un ejemplo con el lenguaje Python.


```python
class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
mi_clase.atributo_clase
mi_clase.atributo_instancia

# 'Hola'
# 'Que tal'
```



Ambos atributos son perfectamente accesibles desde el exterior. Sin embargo esto es algo que tal vez no queramos. Hay ciertos métodos o atributos que queremos que pertenezcan sólo a la clase o al objeto, y que sólo puedan ser accedidos por los mismos. Para ello podemos usar la doble `__` para nombrar a un atributo o método. Esto hará que Python los interprete como "privados", de manera que no podrán ser accedidos desde el exterior.


```python
class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!
```



Y como curiosidad, podemos hacer uso de `dir` para ver el listado de métodos y atributos de nuestra clase. Podemos ver claramente como tenemos el `metodo_normal` y el `atributo` de clase, pero no podemos encontrar `__mi_metodo` ni `__atributo_clase`.


```python
print(dir(mi_clase))
#['_Clase__atributo_clase', '_Clase__mi_metodo', '_Clase__variable',
#'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#'__str__', '__subclasshook__', '__weakref__', 'atributo_clase', 'metodo_normal']
```


Pues bien, en realidad si que podríamos acceder a `__atributo_clase` y a `__mi_metodo` haciendo un poco de trampa. Aunque no se vea a simple vista, si que están pero con un nombre distinto, para de alguna manera ocultarlos y evitar su uso. Pero podemos llamarlos de la siguiente manera, pero por lo general **no es una buena idea**.


```python
mi_clase._Clase__atributo_clase
# 'Hola'
mi_clase._Clase__mi_metodo()
# 'Haz algo'
```

Existen otros conceptos muy importantes y relacionados con la [programación orientada a objetos](/programacion-orientada-a-objetos/ "programación orientada a objetos"). Aquí te los dejamos:
* [Herencia](/herencia-en-python/ "Herencia")
* [Cohesión](/cohesion-en-programacion/ "Cohesión")
* [Abstracción](/abstraccion-en-programacion/ "Abstracción")
* [Polimorfismo](/polimorfismo-en-programacion/ "Polimorfismo")
* [Acoplamiento](/acoplamiento-poo/ "Acoplamiento")
* [Encapsulamiento](/encapsulamiento-poo/ "Encapsulamiento")