---
layout: default
title: 📗 Crear clase
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: Una clase en Python puede ser creada usando la palabra class seguida de dos puntos. Una vez la clase está definida, podemos crear dentro de ella diferentes métodos y atributos.
order: 70
nav_order: j
nav_exclude: true
permalink: /crear-clase-python
---

# Crear clase Python

Crear una [clase en Python](/programacion-orientada-a-objetos/ "clase en Python") se puede hacer un tan sólo dos líneas de código haciendo uso de la palabra `class`.

```python
class MiClase:
    pass
```

## Añadir atributos a la clase
Podemos añadir algún atributo de clase. En este caso tenemos atributos generales que pertenecen a la clase y no a la instancia.
```python
class MiClase:
    atributo1 = "valor1"
    atributo2 = "valor2"
```

## Añadir constructor a la clase
Se podría decir que toda clase tiene un constructor, que recibe unos parámetros de entrada cuando el objeto es creado. Creamos por lo tanto el constructor `__init__`. Nótese la diferencia entre `atributo1` y `argumento1` (pista, atributo de clase vs instancia).
```python
class MiClase:
    atributo1 = "valor1"
    atributo2 = "valor2"
    def __init__(self, argumento1):
        self.argumento1 = argumento1
```

Ya vamos teniendo una clase mucho más completa, pero sigamos.

## Añadir métodos a la clase
A parte de atributos y el constructor, toda clase tiene un conjunto de funciones o métodos que realizan diferentes funcionalidades. Creamos la `funcion1()`.
```python
class MiClase:
    atributo1 = "valor1"
    atributo2 = "valor2"
    def __init__(self, argumento1):
        self.argumento1 = argumento1
    def funcion1(self):
        print("Esta es la función 1")
```

## Crear objeto
A diferencia de la clase, un objeto define una clase particular, con unos atributos particulares para ese objeto. Es decir, el objeto es la instancia de la clase. Se puede crear usando `()` sobre la clase y pasando los argumentos de entrada separados por `,`.
```python
mi_clase = MiClase("Hola")
```

## Acceder a métodos y atributos
Una vez tenemos el objeto `mi_clase`, podemos acceder a todo su contenido, tanto métodos como atributos de clase o de instancia. Simplemente hay que usar el objeto `.` y el método o atributo.

```python
mi_clase.atributo1
mi_clase.atributo2
mi_clase.argumento1
mi_clase.funcion1()
```

Para más detalle, te dejamos otros posts por si te pudieran interesar:
* [Programación orientada a objetos, una introducción a clases, objetos, métodos y atributos](/programacion-orientada-a-objetos/ "Programación orientada a objetos, una introducción a clases, objetos, métodos y atributos")
* [Métodos «normales», estáticos y de clase en Python. Diferencias y usos](/metodos-estaticos-clase-python/ "Métodos «normales», estáticos y de clase en Python. Diferencias y usos")
* [Dando un toque de elegancia con el decorador @property en nuestras clases](/decorador-property-python/ "Dando un toque de elegancia con el decorador @property en nuestras clases")