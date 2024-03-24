---
layout: default
title: 📗 Acoplamiento
parent: 🏄‍♂️ 06. Programación orientada a objetos
description: El encapsulamiento o encapsulación en programación es un concepto relacionado con la programación orientada a objetos, y hace referencia al ocultamiento de los estado internos de una clase al exterior. Dicho de otra manera, encapsular consiste en hacer que los atributos o métodos internos a una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.
order: 69
nav_order: i
nav_exclude: true
permalink: /acoplamiento-poo
---

# Acoplamiento en programación

El acoplamiento en programación (denominado *coupling* en Inglés) es un concepto que mide la dependencia entre dos módulos distintos de software, como pueden ser por ejemplo las clases. El acoplamiento puede ser de dos tipos:
* Acoplamiento **débil**, que indica que no existe dependencia de un módulo con otros. Esto debería ser la meta de nuestro software.
* Acoplamiento **fuerte**, que por lo contrario indica que un módulo tiene dependencias internas con otros.

El término acoplamiento está muy relacionado con la [cohesión](/cohesion-en-programacion/ "cohesión"), ya que acoplamiento débil suele ir ligado a cohesión fuerte. En general lo que buscamos en nuestro código es que tenga acoplamiento débil y cohesión fuerte, es decir, que no tenga dependencias con otros módulos y que las tareas que realiza estén relacionadas entre sí. Un código así es fácil de leer, de reusar, mantener y tiene que ser nuestra meta. Nótese que se suele emplear alta y baja para designar fuerza y débil respectivamente.

Si aún no te hemos convencido de porque buscamos código débilmente acoplado, veamos lo que pasaría con un código fuertemente acoplado:
* Debido a las dependencias con otros módulo, un cambio en un modulo ajeno al nuestro podría tener un "efecto mariposa" en nuestro código, aún sin haber modificado directamente nuestro módulo.
* Si un módulo tiene dependencias con otros, reduce la reusabilidad, ya que para reusarlo deberíamos copiar también las dependencias.

Veamos un ejemplo usando clases y objetos en Python. Tenemos una `Clase1` que define un atributo de clase `x`. Por otro lado la `Clase2` basa el comportamiento del método `mi_metodo()` en el valor de `x` de la `Clase1`. En este ejemplo existe acoplamiento fuerte, ya que existe una dependencia con una variable de otro módulo.


```python
class Clase1:
    x = True
    pass

class Clase2:
    def mi_metodo(self, valor):
        if Clase1.x:
            self.valor = valor

mi_clase = Clase2()
mi_clase.mi_metodo("Hola")
mi_clase.valor
```



Puede parecer un ejemplo trivial, pero cuando el software se va complicando, no es nada raro acabar haciendo cosas de este tipo casi sin darnos cuenta. Hay veces que dependencias externas pueden estar justificadas, pero hay que estar muy seguro de lo que se hace.

Este tipo de dependencias también puede hacer el código muy difícil de depurar. Imaginemos que nuestro código de la `Clase2` funciona perfectamente, pero de repente alguien hace un cambio en la `Clase1`. Un cambio tan sencillo como el siguiente.


```python
Clase1.x = False
```

Este cambio estaría modificando el comportamiento de nuestra clase y nos preguntaríamos ¿porqué ha dejado de funcionar mi código si no he tocado nada? A veces atribuimos estos comportamientos a la magia o radiación cósmica, pero simplemente tenemos código con acoplamiento fuerte.

Existen otros conceptos muy importantes y relacionados con la [programación orientada a objetos](/programacion-orientada-a-objetos/ "programación orientada a objetos"). Aquí te los dejamos:
* [Herencia](/herencia-en-python/ "Herencia")
* [Cohesión](/cohesion-en-programacion/ "Cohesión")
* [Abstracción](/abstraccion-en-programacion/ "Abstracción")
* [Polimorfismo](/polimorfismo-en-programacion/ "Polimorfismo")
* [Acoplamiento](/acoplamiento-poo/ "Acoplamiento")
* [Encapsulamiento](/encapsulamiento-poo/ "Encapsulamiento")