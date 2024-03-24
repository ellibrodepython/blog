---
layout: default
title: 📙 Polimorfismo
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: El polimorfismo en programación es un concepto muy importante en la programación orientada a objetos, y hace referencia a la capacidad que puede tener un objeto para ofrecer una respuesta distinta en función de su implementación.
order: 72
nav_order: l
nav_exclude: true
permalink: /polimorfismo-en-programacion
---


# Polimorfismo en programación

El **polimorfismo** es uno de los pilares básicos en la [programación orientada a objetos](/programacion-orientada-a-objetos-python), por lo que para entenderlo es importante tener las bases de la POO y la [herencia](/herencia-en-python) bien asentadas.

El término polimorfismo tiene origen en las palabras *poly* (muchos) y *morfo* (formas), y aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas. ¿Pero qué significa esto?

Pues bien, significa que objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos.

En lenguajes de programación como Python, que tiene tipado dinámico, el polimorfismo va muy relacionado con el [duck typing](/duck-typing-python).

Sin embargo, para entender bien este concepto, es conveniente explicarlo desde el punto de vista de un lenguaje de programación con tipado estático como Java. Vamos a por ello.

## Polimorfismo en Java

Vamos a comenzar definiendo una clase `Animal`.

```java
// Código Java
class Animal{ 
    public Animal() {} 
}
```

Y dos clases `Perro` y `Gato` que heredan de la anterior.

```java
// Código Java
class Perro extends Animal {
    public Perro() {}
}

class Gato extends Animal {
    public Gato() {}
}
```

El polimorfismo es precisamente lo que nos permite hacer lo siguiente:

```java
// Código Java
Animal a = new Perro();
```

Recuerda que Java es un lenguaje con tipado estático, lo que significa que el tipo tiene que ser definido al crear la variable.

Sin embargo estamos asignando a una variable `Animal` un objeto de la clase `Perro`. ¿Cómo es esto posible?

Pues ahí lo tienes, **el polimorfismo es lo que nos permite usar ambas clases de forma indistinta**, ya que soportan el mismo "interfaz" (no confundir con el `interface` de Java).

El siguiente código es también correcto. Tenemos un array de `Animal` donde cada elemento toma la forma de `Perro` o de `Gato`.

```java
// Código Java
Animal[] animales = new Animal[10];
animales[0] = new Perro();
animales[1] = new Gato();
```

Sin embargo, no es posible realizar lo siguiente, ya que `OtraClase` no comparte interfaz con `Animal`. Tendremos un error `error: incompatible types`.

```java
// Código Java
class OtraClase { 
    public OtraClase() {} 
}
Animal a = new OtraClase();
animales[0] = new OtraClase();
```

## Polimorfismo en Python

El término polimorfismo visto desde el punto de vista de Python es complicado de explicar sin hablar del [duck typing](/duck-typing-python), por lo que te recomendamos la lectura.

Al ser un lenguaje con tipado dinámico y permitir duck typing, en Python no es necesario que los objetos compartan un interfaz, simplemente basta con que tengan los métodos que se quieren llamar.

Podemos recrear el ejemplo de Java de la siguiente manera. Supongamos que tenemos un clase `Animal` con un método `hablar()`.

```python
class Animal:
    def hablar(self):
        pass
```

Por otro lado tenemos otras dos clases, `Perro`, `Gato` que heredan de la anterior. Además, implementan el método `hablar()` de una forma distinta.

```python
class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
```

A continuación creamos un objeto de cada clase y llamamos al método `hablar()`. Podemos observar que cada animal se comporta de manera distinta al usar `hablar()`.

```python
for animal in Perro(), Gato():
    animal.hablar()

# Guau!
# Miau!
```

En el caso anterior, la variable `animal` ha ido "tomando las formas" de `Perro` y `Gato`. Sin embargo, nótese que al tener tipado dinámico este ejemplo hubiera funcionado igual sin que existiera herencia entre `Perro` y `Gato`, pero esta explicación la dejamos para el capítulo de [duck typing](/duck-typing-python)

Existen otros conceptos muy importantes y relacionados con la [programación orientada a objetos](/programacion-orientada-a-objetos/ "programación orientada a objetos"). Aquí te los dejamos:
* [Herencia](/herencia-en-python/ "Herencia")
* [Cohesión](/cohesion-en-programacion/ "Cohesión")
* [Abstracción](/abstraccion-en-programacion/ "Abstracción")
* [Polimorfismo](/polimorfismo-en-programacion/ "Polimorfismo")
* [Acoplamiento](/acoplamiento-poo/ "Acoplamiento")
* [Encapsulamiento](/encapsulamiento-poo/ "Encapsulamiento")