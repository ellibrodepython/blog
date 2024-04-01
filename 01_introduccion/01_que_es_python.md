---
layout: default
title: 📗 ¿Qué es Python?
title_nav: 📗 ¿Qué es Python?
parent: 🕺🏻 01. Introducción
description: ¿Qué es Python? Te explicamos que es y para que sirve el lenguaje de programación Python. También porque es tan usado y porque cada vez hay más gente que lo usa. Es un lenguaje de programación fácil de usar, multiplataforma y con una comunidad de desarrolladores enorme.
order: 2
nav_order: a
permalink: /que-es-python
---

# ¿Qué es Python? Introducción

Si has llegado hasta aquí es posible que quieras aprender Python, o tal vez simplemente tengas curiosidad por saber algo más de este lenguaje de programación tan popular. En este post te intentaremos convencer de **porqué debes aprender Python**, sin importar en que trabajes o cual sea tu sector.

Aprovechamos de paso a darte la bienvenida a nuestro libro, un lugar donde podrás encontrar tutoriales de Python **completamente gratis** desde lo más básico a conceptos avanzados, y con diferentes aplicaciones: análisis de datos, automatización de tareas, web scraping, machine learning, data science, desarrollo de videojuegos, interfaces gráficos o finanzas.

Dicho esto, empecemos. A diferencia de lo que mucha gente puede pensar, Python es un lenguaje que data de los años **1990s**, y su creación se le atribuye al neerlandés Guido van Rossum<sup><a href="https://es.wikipedia.org/wiki/Guido_van_Rossum" target="_blank" rel="noopener noreferrer">[1]</a></sup>. Recibió su nombre por los humoristas Monty Python.

Su última versión es Python 3, y es la que te recomendamos usar ya que las anteriores ya tienen soporte oficial. En este blog usaremos esta siempre para todo.

De acuerdo con StackOverflow insights<sup><a href="https://insights.stackoverflow.com/trends" target="_blank" rel="noopener noreferrer">[2]</a></sup> en la siguiente gráfica podemos ver el número de preguntas vistas en la plataforma acerca de Pyhton. Podemos ver que Python lleva casi dos años en el podio, una auténtica burrada.

<center><img src="/img/python-evolution.png"></center>

De hecho un estudio realizado hace un tiempo en el 2017<sup><a href="https://stackoverflow.blog/2017/09/06/incredible-growth-python/" target="_blank" rel="noopener noreferrer">[3]</a></sup> ya ponía a Python como uno de los favoritos en los países con mayores ingresos como Alemania, Reino Unido o Estados Unidos entre otros.

> Python was the most visited tag on Stack Overflow within high-income nations

Podemos ver por lo tanto que existe una tendencia clara y seguramente el interés en Python vaya a seguir creciendo en los próximos años. Estos son los motivos por lo que ha crecido tanto y lo seguirá haciendo:
* Se trata de un lenguaje **fácil de aprender**, con una sintaxis muy sencilla que se asemeja bastante al *pseudocódigo*. En otras palabras, **poco código hace mucho**.
* Su uso **no está ligado a un sector concreto**. Por ejemplo el lenguaje R es útil para análisis de datos, pero no puede ser usado para desarrollo web. Python vale para todo.
* Tiene una **comunidad enorme**, además de gran cantidad de librerías para hacer prácticamente cualquier cosa, literalmente.
* Es un lenguaje **multiplataforma**, por lo que el mismo código es compatible en cualquier plataforma (Windows, macOS, Linux) sin hacer nada.
* Por lo general se puede hacer desarrollos en Python **más rápidamente** que en otros lenguajes, acortando la duración de los proyectos.

## Usos de Python
Como hemos dicho Python es un lenguaje muy transversal, usado en diferentes industrias y para diferentes fines. Veamos algunos de las empresas que usan Python:
* YouTube usa Python<sup><a href="http://highscalability.com/youtube-architecture" target="_blank" rel="noopener noreferrer">[4]</a></sup> en la parte del servidor, unida a otros lenguajes como Java o Go.
* Netflix usa Python<sup><a href="https://www.genbeta.com/desarrollo/netflix-explica-donde-como-utiliza-python-aprendizaje-automatico-automatizacion-pasando-seguridad" target="_blank" rel="noopener noreferrer">[5]</a></sup> par automatizar tareas, explorar datos y labores de aprendizaje automático entre otras.
* La NASA usa Python<sup><a href="https://code.nasa.gov/" target="_blank" rel="noopener noreferrer">[6]</a></sup> en gran cantidad de programas científicos.
* JPMorgan<sup><a href="https://www.enterprisetimes.co.uk/2018/10/10/jpmorgan-wants-its-financial-analysts-to-be-able-to-code/" target="_blank" rel="noopener noreferrer">[7]</a></sup> ya dijo hace varios años que se esperaba de sus analistas financieros supieran Python.

Python es también usado para fines muy diversos como son los siguientes:
* **Desarrollo Web**: Existen frameworks como [Django](http://www.djangoproject.com/ "Django"), [Pyramid](http://www.pylonsproject.org/ "Pyramid"), [Flask](http://flask.pocoo.org/ "Flask") o [Bottle](http://bottlepy.org/ "Bottle") que permiten desarrollar páginas web a todos los niveles.
* **Ciencia y Educación**: Debido a su sintaxis tan sencilla, es una herramienta perfecta para enseñar conceptos de programación a todos los niveles. En lo relativo a ciencia y cálculo numérico, existen gran cantidad de librerías como [SciPy](http://scipy.org/ "SciPy") o [Pandas](http://pandas.pydata.org/ "Pandas").
* **Desarrollo de Interfaces Gráficos**: Gran cantidad de los programas que utilizamos tienen un interfaz gráfico que facilita su uso. Python también puede ser usado para desarrollar GUIs con librerías como [Kivy](http://kivy.org/ "Kivy") o [pyqt](http://www.riverbankcomputing.co.uk/software/pyqt/intro "pyqt").
* **Desarrollo Software**: También es usado como soporte para desarrolladores, como para testing.
* **Machine Learning**: En los último años ha crecido el número de implementaciones en Python de librerías de aprendizaje automático como [Keras](https://keras.io/ "Keras"), [TensorFlow](https://www.tensorflow.org/ "TensorFlow"), [PyTorch](https://pytorch.org/ "PyTorch") o [sklearn](https://scikit-learn.org/ "sklearn").
* **Visualización de Datos**: Existen varias librerías muy usadas para mostrar datos en gráficas, como [matplotlib](https://matplotlib.org/ "matplotlib"), [seaborn](https://seaborn.pydata.org/ "seaborn") o [plotly](https://plot.ly/python/ "plotly").
* **Finanzas y Trading**: Gracias a librerías como [QuantLib](https://www.quantlib.org/ "QuantLib") o  [qtpylib](https://qtpylib.io/docs/latest/ "qtpylib") y a su facilidad de uso, es cada vez más usado en estos sectores.

De hecho a día de hoy prácticamente cualquier API, librería o servicio que existe en el mundo tiene una versión para Python, bien sea de manera nativa o a través de un *wrapper*.

## Comunidad

La comunidad de Python es inmensa, con alrededor de 8.2 millones de personas en el mundo (a fecha de 2019)<sup><a href="https://www.zdnet.com/article/programming-languages-python-developers-now-outnumber-java-ones/" target="_blank" rel="noopener noreferrer">[8]</a></sup>, una cifra que supera ya a los usuarios de Java.

Es importante el tamaño de la comunidad, porque cuanto más grande sea, mayor soporte se le dará al lenguaje y mayor número de personas compartirán sus problemas y se ayudarán a resolverlos.

Otra de las características de la comunidad Python son las famosas **PyCon**, unas convenciones anuales llevadas a cabo en gran número de países, donde los desarrolladores se reúnen para compartir ideas.

<center><img src="/img/python-conf.png"></center>


Es también importante mencionar la **Python Software Foundation**, una organización sin ánimo de lucro que se dedica a **promover**, **proteger** y **desarrollar** el lenguaje Python.



## Características de Python

Como cualquier otro lenguaje, Python tiene una serie de características que lo hacen diferente al resto. Las explicamos a continuación:
* Es un lenguaje **interpretado**, no compilado.
* Usa **tipado dinámico**, lo que significa que una variable puede tomar valores de distinto tipo.
* Es **fuertemente tipado**, lo que significa que el tipo no cambia de manera repentina. Para que se produzca un cambio de tipo tiene que hacer una conversión explícita.
* Es **multiplataforma**, ya que un código escrito en macOS funciona en Windows o Linux y vice versa.

Tal vez algunos de estos conceptos puedan resultarte extraños si estás empezando en el mundo de la programación. El siguiente código pretende ilustrar algunas de las características de Python.

Algunas cosas curiosidad que en otros lenguajes no pasan. La función acepta un parámetro **entrada** pero no se especifica su tipo. La `x` almacena primero una cadena, luego un float y luego un integer. La función `funcion()` es llamada con un int, pero su valor se divide entre 2 y el resultado es convertido automáticamente en un float.
```python
def funcion(entrada):
    return entrada/2 
    
x = "Hola"
x = 7.0
x = int(x)
x = funcion(x)
print(x)
print(type(x))

# 3.5
# <class 'float'>
```

## The Zen of Python
El **Zen de Python** es una colección de los 19 principios que influyen en el diseño del lenguaje. De alguna manera, muestran la filosofía del mismo y pueden ser encontrados en la PEP20<sup><a href="https://www.python.org/dev/peps/pep-0020/" target="_blank" rel="noopener noreferrer">[9]</a></sup> Las PEP o *Python Enhancement Prososals* son unos documentos que ofrecen información a la comunidad de Python, bien describiendo alguna característica nueva o dando información en general.

Son las siguientes, y aunque alguna pueda parecer lógica, a veces resultan no serlo tanto cuando no se cumplen:

> 1. Bello es mejor que feo.
2. Explícito es mejor que implícito.
3. Simple es mejor que complejo.
4. Complejo es mejor que complicado.
5. Plano es mejor que anidado.
6. Espaciado es mejor que denso.
7. La legibilidad es importante.
8. Los casos especiales no son lo suficientemente especiales como para romper las reglas.
9. Sin embargo la practicidad gana a la pureza.
10. Los errores nunca deben pasar silenciosamente.
11. A menos que se silencien explícitamente.
12. Frente a la ambigüedad, evitar la tentación de adivinar.
13. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
14. A pesar de que esa manera no sea obvia a menos que seas Holandés (el creador lo era)
15. Ahora es mejor que nunca.
16. A pesar de que nunca es muchas veces mejor que *ahora* mismo.
17. Si la implementación es difícil de explicar, es una mala idea.
18. Si la implementación es fácil de explicar, puede que sea una buena idea.
19. Los namespaces son una gran idea, ¡tengamos más de esos!

¿Qué opinas? ¿Te hemos convencido para aprender Python? A continuación te explicaremos cómo instalar Python para que puedas empezar a dar tus primeros pasos.