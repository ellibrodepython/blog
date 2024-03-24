---
layout: default
title: 📕 Interfaces y Abstract Base Class
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: Las Abstract Base Class o ABC en Python nos permiten la creación de interfaces formales, que pueden ser usados por otras clases que implementen dicho interfaz.
order: 67
nav_order: g
permalink: /abstract-base-class
---

# Interfaces y Abstract Base Class (ABC)

En la [programación orientada a objetos](/programacion-orientada-a-objetos-python), un interfaz define al conjunto de métodos que tiene que tener un objeto para que pueda cumplir una determinada función en nuestro sistema. Dicho de otra manera, un interfaz define como se comporta un objeto y lo que se puede hacer con el.

Piensa en el mando a distancia del televisor. Todos los mandos nos ofrecen el mismo interfaz con las mismas funcionalidades o métodos. En *pseudocódigo* se podría escribir su interfaz como:

```
# Pseudocódigo
interface Mando{
	def siguiente_canal():
	def canal_anterior():
	def subir_volumen():
	def bajar_volumen():
}
```

Es importante notar que los interfaces no poseen una implementación *per se*, es decir, no llevan código asociado. El interfaz se centra en el **qué** y no en el **cómo**.

Se dice entonces que una determinada clase implementa una interfaz, cuando añade código a los métodos que no lo tenían (denominados abstractos). Es decir, **implementar un interfaz consiste en pasar del qué se hace al cómo se hace**.

Podríamos decir entonces que los mandos de Samsung y LG implementan nuestro interfaz `Mando`, ya que ambos tienen los métodos definidos, pero con implementaciones diferentes. Esto es debido a que cada empresa resuelve el mismo problema con un enfoque diferente, pero lo que se ofrece visto desde el exterior es lo mismo.

Aunque lo veremos más adelante, ya podemos adelantar que Python no posee la *keyword* `interface` como otros lenguajes de programación. A pesar de esto, existen dos formas de definir interfaces en Python:
* Interfaces informales
* Interfaces formales

Dependiendo de la magnitud y tipo del proyecto en el que trabajemos, es posible que los interfaces informales sean suficientes. Sin embargo, a veces no bastan, y es donde entran los interfaces formales y las metaclases, ambos conceptos bastante avanzados pero que la mayoría de programadores tal vez pueda ignorar.

## Interfaces informales
Los interfaces informales pueden ser definidos con una simple clase que no implementa los métodos. Volviendo al ejemplo de nuestro interfaz *mando a distancia*, lo podríamos escribir en Python como:

```python
class Mando:
    def siguiente_canal(self):
        pass
    def canal_anterior(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass
```

Una vez definido nuestro interfaz informal, podemos usarlo mediante [herencia](/herencia-en-python). Las clases `MandoSamsung` y `MandoLG` implementan el interfaz `Mando` con código particular en los métodos. Recuerda, pasamos del **qué hace** al **cómo se hace**.

```python
class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")
```

Análogamente creamos `MandoLG`.

```python
class MandoLG(Mando):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")
```

Como hemos dicho, esto es una solución perfectamente válida en la mayoría de los casos, pero existe un problema con el que entenderás perfectamente porqué lo llamamos interfaz informal.

Al heredar de la clase `Mando`, no se obliga a `MandoSamsung` o `MandoLG` a implementar todos los métodos. Es decir, ambas clases podrían no tener código para todos los métodos, y esto es algo que puede causar problemas.

El razonamiento es el siguiente. Si `Mando` es un interfaz que como tal no implementa ningún método (tan sólo define los métodos), ¿no sería acaso importante asegurarse de que las clases que usan dicho interfaz implementan los métodos?

Si un método queda sin implementar, podríamos tener problemas en el futuro, ya que al llamar a dicho método no tendríamos código que ejecutar. Es cierto que se podría resolver cambiando `pass` por `raise NotImplementedError()`, pero el error lo obtendríamos en tiempo de ejecución.

Hasta aquí los interfaces informales. Nótese que este tipo de interfaces es posible en Python debido a una de sus características estrella, el [duck typing](/duck-typing-python), por lo que te recomendamos que leas acerca de este concepto tan importante en Python.

## Interfaces formales

Una vez tenemos el contexto de lo que son los interfaces informales, ya estamos en condiciones de entender los interfaces formales.

Los interfaces formales pueden ser definidos en Python utilizando el módulo por defecto llamado ABC (*Abstract Base Classes*). Los [abc](https://docs.python.org/3/library/abc.html) fueron añadidos a Python en la [PEP3119](https://www.python.org/dev/peps/pep-3119).

Simplemente definen una forma de crear interfaces (a través de metaclases) en los que se definen unos métodos (pero no se implementan) y donde se fuerza a las clases que usan ese interfaz a implementar los métodos. Veamos unos ejemplos.

El interfaz más sencillo que podemos crear es de la siguiente manera, heredando de `abc.ABC`.

```python
from abc import ABC
class Mando(ABC):
	pass
```

La siguiente sintaxis es también válida, y aunque se sale del contenido de este capítulo, es importante que asocies el módulo `abc` con las metaclases.

```python
from abc import ABCMeta
class Mando(metaclass=ABCMeta):
    pass
```

Pero veamos un ejemplo concreto continuando con nuestro ejemplo del mando a distancia. Podemos observar como se usa el [decorador](/decoradores-python) `@abstractmethod`.

Un método abstracto es un método que no tiene una implementación, es decir, que no lleva código. Un método definido con este decorador, forzará a las clases que implementen dicho interfaz a codificarlo.

Veamos como queda nuestro interfaz formal `Mando`.

```python
from abc import abstractmethod
from abc import ABCMeta

class Mando(metaclass=ABCMeta):
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass
```

Lo primero a tener en cuenta es que no se puede crear un objeto de una clase interfaz, ya que sus métodos no están implementados.

```python
mando = Mando()
# TypeError: Can't instantiate abstract class Mando with abstract methods bajar_volumen, canal_anterior, siguiente_canal, subir_volumen
```

Sin embargo si que podemos heredar de `Mando` para crear una clase `MandoSamsung`. **Es muy importante que implementemos todos los métodos**, o de lo contrario tendremos un error. Esta es una de las diferencias con respecto a los interfaces informales.

```python
class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")
```

Y como de costumbre podemos crear un objeto y llamar a sus métodos.

```python
mando_samsung = MandoSamsung()
mando_samsung.bajar_volumen()
# Samsung->Bajar
```

Siguiendo con el ejemplo podemos definir la clase `MandoLG`.

```python
class MandoLG(Mando):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")
```

Y creamos un objeto de `MandoLG`.
```python
mando_lg = MandoLG()
mando_lg.bajar_volumen()
# LG->Bajar
```

Llegados a este punto tenemos por lo tanto dos conceptos diferentes claramente identificados:
* Por un lado tenemos nuestro interfaz `Mando`. Se trata de una clase que define el comportamiento de un mando genérico, pero sin centrarse en los detalles de cómo funciona. Se centra en el **qué**.
* Por otro lado tenemos dos clases `MandoSamsung` y `MandoLG` que implementan/heredan el interfaz anterior, añadiendo un código concreto y diferente para cada mando. Ambas clases representan el **cómo**.

Hasta aquí hemos visto como crear un interfaz formal sencilla usando `abc` con métodos abstractos, pero existen más funcionalidades que merece la pena ver. Vamos a por ello.


## Clases virtuales

Como ya sabemos, se considera que una clase es subclase o `issubclass` de otra si hereda de la misma, como podemos ver en el siguiente ejemplo.

```python
class ClaseA:
    pass
class ClaseB(ClaseA):
    pass

print(issubclass(ClaseB, ClaseA))
# True
```

Pero, ¿y si queremos que se considere a una clase la padre cuando no existe herencia entre ellas?

Es aquí donde entran las clases virtuales. Usando `register()` podemos registrar a una ABC como clase padre de otra. En el siguiente ejemplo `FloatABC` se registra como clase virtual padre de [float](/float-python).

```python
from abc import ABCMeta

class FloatABC(metaclass=ABCMeta):
    pass

FloatABC.register(float)
```

Y esto implica que el comportamiento de `issubclass` se ve modificado.

```python
print(issubclass(float, FloatABC))
# True
```

Análogamente podemos realizar lo mismo con una clase definida por nosotros.

```python
@FloatABC.register
class MiFloat():
    pass

x = MiFloat()
print(issubclass(MiFloat, FloatABC))
# True
```

## Métodos abstractos

Como ya hemos visto los métodos abstractos son aquellos que son declarados pero no tienen una implementación. También hemos visto como Python nos obliga a implementarlos en la clases que heredan de nuestro interfaz. Esto es posible gracias al [decorador](/decoradores-python) `@abstractmethod`.

```python
from abc import ABC, abstractmethod
class Clase(metaclass=ABCMeta):
    @abstractmethod
    def metodo_abstracto(self):
        pass
```

Sin embargo, también es posible combinar el decorador `@abstractmethod` con los decoradores `@classmethod` y `@staticmethod` que ya vimos [anteriormente](/metodos-estaticos-clase-python). Nótese que `@abstractmethod` debe ser usado siempre justo antes del método.

Como recordatorio, un método de clase es llamado sobre la clase y no sobre el objeto, pudiendo modificar la clase pero no el objeto.
```python
class Clase(ABC):
    @classmethod
    @abstractmethod
    def metodo_abstracto_de_clase(cls):
        pass
```

Análogamente podemos definir un `@staticmethod`. Se trata de un método que no permite realizar modificaciones ni de la clase ni del objeto, ya que no lo recibe como parámetro.

```python
class Clase(ABC):
    @staticmethod
    @abstractmethod
    def metodo_abstracto_estatico():
        pass
```

Y por último también podemos combinarlo con el decorador [property](/decorador-property-python).

```python
class Clase(ABC):
    @property
    @abstractmethod
    def metodo_abstracto_propiedad(self):
        pass
```


## Abstract Base Classes y colecciones

Python nos ofrece un conjunto de *Abstract Base Classes* que podemos usar para crear nuestras propias clases, denominado [collections.abc](https://docs.python.org/3/library/collections.abc.html#module-collections.abc). Es por tanto importante echarles un vistazo, ya que tal vez exista ya la que necesitemos.

Podemos por ejemplo crear una clase `MiSet` que use `abc.Set`, pero que tenga un comportamiento ligeramente distinto. En este caso, deberemos implementar los [métodos mágicos](/metodos-magicos-python) `__iter__`, `__contains__` y `__len__`, ya que son definidos como abstractos en el abc.


```python
from collections import abc
class MiSet(abc.Set):
    def __init__(self, iterable):
        self.elements = []
        for value in iterable:
            if value not in self.elements:
                self.elements.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return "".join(str(i) for i in self.elements)
```

Como podemos ver, heredamos ciertas funcionalidades como los operadores `&` y `|` que pueden ser usados sobre nuestra nueva clase.

```python
s1 = MiSet("abcdefg")
s2 = MiSet("efghij")

print(s1 & s2)
print(s1 | s2)
# efg
# abcdefghij
```
