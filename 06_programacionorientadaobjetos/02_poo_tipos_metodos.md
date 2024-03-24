---
layout: default
title: 📙 Tipos de métodos
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: Existen varios tipos de métodos y pueden ser clasificados en tres. Los de instancia son los "normales" que pueden acceder al contenido de la clase y el objeto. Los classmethod solamente pueden acceder al contenido de la clase. Por último, los staticmethod no pueden ni a la clase ni al objeto.
order: 62
nav_order: b
permalink: /metodos-estaticos-clase-python
---


# Métodos en Python: instancia, clase y estáticos
En otros posts hemos visto como se pueden crear métodos con `def` dentro de una clase, pudiendo recibir parámetros como entrada y modificar el estado (como los atributos) de la instancia. Pues bien, haciendo uso de los decoradores, es posible crear diferentes tipos de métodos:
* Lo métodos de instancia "normales" que ya hemos visto como `metodo()`
* Métodos de clase usando el decorador `@classmethod`
* Y métodos estáticos usando el decorador `@staticmethod`

En la siguiente clase tenemos un ejemplo donde definimos los tres tipos de métodos.


```python
class Clase:
    def metodo(self):
        return 'Método normal', self

    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls

    @staticmethod
    def metodoestatico():
        return "Método estático"
```

Veamos su comportamiento en detalle uno por uno.

## Métodos de instancia

Los **métodos de instancia** son los métodos normales, de toda la vida, que hemos visto anteriormente. Reciben como parámetro de entrada `self` que hace referencia a la instancia que llama al método. También pueden recibir otros argumentos como entrada.

<p class="alert alert-info">
<b>Para saber más:</b> El uso de "self" es totalmente arbitrario. Se trata de una convención acordada por los usuarios de Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre. Lo mismo ocurre con "cls", que veremos a continuación.
</p>



```python
class Clase:
    def metodo(self, arg1, arg2):
        return 'Método normal', self
```

Y como ya sabemos, una vez creado un objeto pueden ser llamados.


```python
mi_clase = Clase()
mi_clase.metodo("a", "b")
# ('Método normal', <__main__.Clase at 0x10b9daa90>)
```


En vista a esto, los **métodos de instancia**:
* Pueden **acceder y modificar los atributos del objeto**.
* Pueden **acceder a otros métodos**.
* Dado que desde el objeto `self` se puede acceder a la clase con ` self.__class__`, también **pueden modificar el estado de la clase**

## Métodos de clase (classmethod)

A diferencia de los métodos de instancia, los métodos de clase reciben como argumento `cls`, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero no a la instancia.


```python
class Clase:
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls
```

Se pueden llamar sobre la clase.


```python
Clase.metododeclase()
# ('Método de clase', __main__.Clase)
```




Pero también se pueden llamar sobre el objeto.


```python
mi_clase.metododeclase()
# ('Método de clase', __main__.Clase)
```





Por lo tanto, los **métodos de clase**:
* **No** pueden acceder a los atributos de la instancia.
* Pero **si pueden** modificar los atributos de la clase.


## Métodos estáticos (staticmethod)

Por último, los métodos estáticos se pueden definir con el decorador `@staticmethod` y no aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que **no pueden modificar el estado ni de la clase ni de la instancia**. Pero por supuesto pueden aceptar parámetros de entrada.


```python
class Clase:
    @staticmethod
    def metodoestatico():
        return "Método estático"
```


```python
mi_clase = Clase()
Clase.metodoestatico()
mi_clase.metodoestatico()

# 'Método estático'
# 'Método estático'
```


Por lo tanto el uso de los **métodos estáticos** pueden resultar útil para indicar que un método no modificará el estado de la instancia ni de la clase. Es cierto que se podría hacer lo mismo con un método de instancia por ejemplo, pero a veces resulta importante indicar de alguna manera estas peculiaridades, evitando así futuros problemas y malentendidos.

En otras palabras, los métodos estáticos se podrían ver como funciones normales, con la salvedad de que van ligadas a una clase concreta.