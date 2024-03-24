---
layout: default
title: 📗 Abstracción
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: La abstracción en programación es un termino que hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en como puede ser usada, lo que se conoce como el interfaz.
order: 68
nav_order: h
nav_exclude: true
permalink: /abstraccion-en-programacion
---


# Abstracción en programación

La abstracción es un termino que hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en como puede ser usada, lo que se conoce como **interfaz**. Si has oído hablar del enfoque **caja negra**, es un concepto muy relacionado. Dicho en otras palabras, la abstracción consiste en ocultar toda la complejidad que algo puede tener por dentro, ofreciéndonos unas funciones de alto nivel, por lo general sencillas de usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.

Una analogía del mundo real podría ser la televisión. Se trata de un dispositivo muy complejo donde han trabajado gran cantidad de ingenieros de diversas disciplinas como telecomunicaciones o electrónica. ¿Os imagináis que para cambiar de canal tuviéramos que saber todos los entresijos del aparato?. Pues bien, se nos ofrece una abstracción de la televisión, un **mando a distancia**. El mando nos abstrae por completo de la complejidad de los circuitos y señales, y nos da una interfaz sencilla que con unos pocos botones podemos usar.

Algo muy parecido sucede en la programación orientada a objetos. Si tuviéramos una clase `Televisor`, en su interior podría haber líneas y líneas de código super complejas, pero una buena abstracción sería la que simplemente ofreciera los métodos `encender()`, `apagar()` y `cambiar_canal()` al exterior.

Un concepto relacionado con la abstracción, serían las **clases abstractas** o más bien los **métodos abstractos**. Se define como clase abstracta la que contiene métodos abstractos, y se define como método abstracto a un método que ha sido declarado pero no implementado. Es decir, que no tiene código.

Es posible crear métodos abstractos en Python con decoradores como `@absttractmethod`, pero esto lo dejamos para otro post.

Existen otros conceptos muy importantes y relacionados con la [programación orientada a objetos](/programacion-orientada-a-objetos/ "programación orientada a objetos"). Aquí te los dejamos:
* [Herencia](/herencia-en-python/ "Herencia")
* [Cohesión](/cohesion-en-programacion/ "Cohesión")
* [Abstracción](/abstraccion-en-programacion/ "Abstracción")
* [Polimorfismo](/polimorfismo-en-programacion/ "Polimorfismo")
* [Acoplamiento](/acoplamiento-poo/ "Acoplamiento")
* [Encapsulamiento](/encapsulamiento-poo/ "Encapsulamiento")