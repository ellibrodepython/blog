---
layout: default
title: 📗 Cohesión
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: La cohesión hace referencia al grado de relación entre los elementos de un módulo. En el diseño de una función, es importante pensar bien la tarea que va a realizar, intentando que sea única y bien definida. Cuantas más cosas diferentes haga la función sin relación entre sí, más complicado será el código de entender y reutilizar.
order: 73
nav_order: m
nav_exclude: true
permalink: /cohesion-en-programacion
---


# Cohesión en Programación

La **cohesión** hace referencia al grado de **relación entre los elementos de un módulo**. En el diseño de una función, es importante pensar bien la tarea que va a realizar, intentando que sea única y bien definida. Cuantas más cosas diferentes haga una función sin relación entre sí, más complicado será el código de entender. Existen por lo tanto dos tipos de cohesión:
* Por un lado tenemos la cohesión **débil** que indica que la relación entre los elementos es baja. Es decir, no pertenecen a una única funcionalidad.
* Por otro la cohesión **fuerte**, que debe ser nuestro objetivo al diseñar programas. La cohesión fuerte indica que existe una alta relación entre los elementos existentes dentro del módulo.

Existe también otro concepto llamado acoplamiento que explicamos en [otro post](/acoplamiento-poo/ "otro post"). Normalmente acoplamiento débil se relaciona con cohesión fuerte o alta.

Veámoslo con un ejemplo. Tenemos una función `suma()` que suma dos números. El problema es que además de sumar dos números, los convierte a `float()` y además pide al usuario que introduzca por pantalla el número. Podría parecer que esas otras dos funcionalidades no son para tanto, pero si por ejemplo una persona quiere usar nuestra función `suma()` pero ya tiene los números y no quiere pedirlos por pantalla, no le serviría nuestra función.


```python
# Mal. Cohesión débil
def suma():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)

suma()
```

Para que la función tuviese una cohesión fuerte, sería conveniente que la `suma` realizara una única tarea bien definida, que es sumar.


```python
# Bien. Cohesión fuerte
def suma(numeros):
    total = 0
    for i in numeros:
        total = total + i
    return total
```

Evidentemente un ejemplo tan sencillo como el explicado no tiene implicaciones demasiado graves, pero es importante buscar que las funciones realicen una única tarea (o conjunto) pero relacionadas entre sí. Diseñar código con cohesión fuerte nos permite:
* Reducir la complejidad del módulo, ya que tendrá un menor número de operaciones.
* Se podrá reutilizar los módulos más fácilmente
* El sistema será más fácilmente mantenible.


Existen otros conceptos muy importantes y relacionados con la [programación orientada a objetos](/programacion-orientada-a-objetos/ "programación orientada a objetos"). Aquí te los dejamos:
* [Herencia](/herencia-en-python/ "Herencia")
* [Cohesión](/cohesion-en-programacion/ "Cohesión")
* [Abstracción](/abstraccion-en-programacion/ "Abstracción")
* [Polimorfismo](/polimorfismo-en-programacion/ "Polimorfismo")
* [Acoplamiento](/acoplamiento-poo/ "Acoplamiento")
* [Encapsulamiento](/encapsulamiento-poo/ "Encapsulamiento")