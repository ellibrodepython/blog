---
layout: default
title: 📗 Descargar e instalar Python
parent: 🕺🏻 01. Introducción
description: Descargar e instalar Python 3 para Windows, macOS y Linux. Explicamos como instalar y configurar Python 3 tanto con el IDE PyCharm. Se explica también como usar JupyterLab con Python sin ningún tipo de instalación.
order: 3
nav_order: b
permalink: /descargar-instalar-python
---

# ¿Cómo programar en Python?

Si quieres empezar a programar en Python, en este post te damos dos alternativas de como puedes empezar a hacerlo:
* La primera es usar Python **sin ningún tipo de instalación**. Sin duda la más sencilla y rápida. Para ello usaremos la versión online de JupyterLab.
* Y la segunda es usando **Python con PyCharm**, para lo que tendremos que instalar el propio lenguaje Python y el entorno de desarrollo PyCharm.

¡Empecemos!


## Sin instalación: JupyterLab
Si quieres empezar a programar en Python de manera rápida **sin tener que instalar nada**, existe una alternativa muy útil llamada **JupyterLab**. Se trata de una herramienta desarrollada por Jupyter, un proyecto open-source sin ánimo de lucro que nació en 2014 del proyecto IPython.

JupyterLab es un entorno de desarrollo web (se accede a el a través de Firefox, Chrome u otro navegador) y además de poder instalártelo en tu ordenador, ofrecen un servicio online gratis de usar. Con tan sólo entrar en una dirección web puedes empezar a programar.

Accede a https://jupyter.org/try y busca **"Try JupyterLab"**.

<center><img src="/img/jup-notebook.png" style="width:30%"></center>


Una vez haya cargado la página encontrarás lo siguiente. Se trata del entorno de desarrollo que se nos proporciona. A la izquierda tienes la navegación, donde están todos tus achivos y carpetas. A la derecha se pueden visualizar los ficheros **ipynb**, que es el formato de los Jupyter Notebook por excelencia.

<center><img src="/img/jupyter-gui.png" style="width:70%"></center>


En estos ficheros *ipynb* puedes escribir código Python y ejecutarlo, además de poder mezclarlo con texto, imágenes, animaciones y otras herramientas.

Si creamos un nuevo *Notebook* con File->New->Notebook y seleccionamos como Kernel Python3, podemos empezar a crear nuestro primer código, el famoso "Hola Mundo". Haciendo click en la flecha, se puede ejecutar el código que tenemos seleccionado.

<center><img src="/img/jupyter-helloworld.png" style="width:40%"></center>


Los Notebook son una herramienta muy potente ya que:
* Permiten ejecutar código fragmento a fragmento, viendo el resultado justo en la siguiente línea.
* Se puede mezclar código con otros recursos como imágenes o texto con formato markdown, entre otros recursos.
* Es posible visualizar también gráficas, como las generadas con matplotlib.

Pero también tiene sus desventajas:
* No se trata de un entorno de desarrollo completo, ya que carece de muchas funcionalidades.
* Si usamos la versión web, estaremos limitados por los recursos del servidor en el que se ejecute. La rapidez será mayor en nuestro ordenador.
* Para proyectos grandes de Python no es una alternativa.

Por lo tanto es una herramienta perfecta para empezar, pero si crees que necesitas más, te explicamos como instalar Python y el entorno de desarrollo PyCharm en la siguientes secciones.

## Con instalación: Python + PyCharm
Si por lo contrario buscas algo más completo, deberás instalar Python y un entorno de desarrollo (IDE) en tu ordenador. Necesitarás dos cosas:
* Por un lado necesitarás Python, es decir, el propio lenguaje de programación. Con esto y cualquier editor de texto ya podrías programar, pero no es demasiado agradable.
* Por otro, es conveniente también instalar un entorno de desarrollo, ya que hace que programar sea una tarea mucho más fácil. Existe muchos, como [Atom](https://atom.io/ "Atom"), [Sublime Text](https://www.sublimetext.com/ "Sublime Text") o [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code"), pero nosotros usaremos [PyCharm](https://www.jetbrains.com/es-es/pycharm/ "PyCharm").

### Instalar Python en Windows

Para instalar Python en Windows debes ir a la sección de descargas de la [web oficial](https://www.python.org/downloads/ "web oficial") y seleccionar la última versión. Te recomendamos utilizar la versión 3.x ya que aunque también existen versiones anteriores como las 2.x, Python ya ha dejado de dar soporte a ellas.

Ambas versiones son relativamente similares, pero hay detalles o alguna que otra funcionalidad que varía. En este blog nos centramos en la versión 3, por lo que todo el código que veas será compatible con la misma.

Una vez hayas descargado el ejecutable, ábrelo y realiza la instalación. Es importante que verifiques que se haya seleccionado la opción de "**Add Python 3.x to PATH**"

<center><img src="/img/install-config.png" style="width:50%"></center>

Una vez hayas finalizado, si abres el terminal de comandos de Windows (busca por la aplicación *cmd* o símbolo de sistema) puedes verificar que se ha instalado correctamente ejecutando el siguiente comando.

```shell
python -V
```
Y verás en la salida algo así dependiendo de la versión que hayas instalado.
```shell
Python 3.8.3
```

De hecho como hemos indicado, con esto ya podrías empezar a programar en Python en tu ordenador, pero la verdad que no es demasiado cómodo. En el último apartado te explicaremos como instalar PyCharm, un entorno de desarrollo que nos hará la vida mucho más fácil.

<center><img src="/img/install-python.gif" style="width:50%"></center>


### Instalar Python en macOS

#### Método 1
Existen dos formas diferentes de instalar Python en mac. Empezamos por la más sencilla. Accede a la sección de [descargas de la web oficial de Python](https://www.python.org/downloads/ "descargas de la web oficial de Python") y descarga la última versión. Te recomendamos usar la versión 3, que es la que usamos en todo este blog y la más reciente.

Una vez lo hayas instalado y hayas terminado el proceso de instalación, puedes abrir el terminal y verificar que efectivamente se ha instalado con el siguiente comando.

```shell
python -V
```

Y si el comando devuelve algo así como *Python 3.6.8*, ya estaría instalado. Si tecleas *python* en el terminal ya podrías empezar a teclear comandos Python, pero no es muy cómodo. Más adelante te explicaremos como usar Python con PyCharm.

#### Método 2
La segunda forma de instalar Python en mac es a través del gestor de paquetes *homebrew*. Primero necesitarás instalar XCode con el siguiente comando.

```shell
xcode-select --install
```

Una vez instalado XCode deberás instalar *[Homebrew](https://brew.sh/index_es "Homebrew")* con el siguiente comando.

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Una vez instalado *Homebrew* ya podemos instalar Python a través de su gestor de paquetes. Simplemente ejecuta.

```shell
brew install python3
```

Y por último verifica que Python se ha instalado correctamente.
```shell
python3 -V
```

### Instalar Python en Linux

En la mayoría de distribuciones Linux se puede instalar de manera bastante fácil. Para el caso de Ubuntu 16.10 o más reciente, ejecuta el siguiente comando en el terminal. Dependiendo de la fecha, tal vez te interese instalar una versión más reciente como la 3.8 u otra.

```shell
apt-get update
apt-get install python3.8
```

Si utilizas otra versión diferente de Ubuntu, deberás añadir un repositorio. Te recomendamos [deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa "deadsnakes PPA").

```shell
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
```

Y una vez finalizada la instalación puedes comprobar que se ha instalado correctamente con el siguiente comando.

```shell
python -V
python3 -V
```

### Instalando PyCharm
Llegados a este punto debemos ya tener instalado Python en nuestro ordenador, por lo que vamos a proceder ya a instalar PyCharm.

Antes de nada, una breve introducción a [PyCharm](https://www.jetbrains.com/es-es/pycharm/ "PyCharm"). Se trata de un entorno de desarrollo o IDE (*Integrated Development Environment*) de la empresa JetBrains. Está disponible en las plataformas más comunes como Windows, Linux o macOS y es una herramienta perfecta para escribir código en Python.

Para instalar PyCharm, [accede a la sección de descargas](https://www.jetbrains.com/es-es/pycharm/download/ "accede a la sección de descargas") y selecciona la versión **Community**, que es la versión gratis de desarrollo. Una vez el proceso de instalación haya acabado, deberías ver algo así al abrirlo.

<center><img src="/img/pycharm-init.png" style="width:50%"></center>


A continuación explicaremos como crear y configurar un proyecto, para que puedas empezar a programar en Python dentro del IDE PyCharm.

### Configurando PyCharm

Una vez hayas abierto PyCharm, realiza los siguientes pasos:
* Crear un proyecto nuevo.
* Asigna un nombre y di donde lo quieres guardar.
* Te recomendamos usar *Virtualenv* para los entornos virtuales.

<center><img src="/img/pycharm-venv.png" style="width:50%"></center>


* En **Base Interpreter** selecciona la versión de Python que has descargado.
* El proyecto se habrá creado. Crea un nuevo fichero Python con un nombre.

<center><img src="/img/pycharm-newfile.png" style="width:50%"></center>


* Ya puedes escribir código en el fichero. Empecemos por ejemplo con un *Hola Mundo*

<center><img src="/img/pycharm-helloworld.png" style="width:50%"></center>


* Y en Run->Run o click derecho y Run, podrás ejecutar el código.

<center><img src="/img/pycharm-run.png" style="width:50%"></center>

Una de las características más útiles en PyCharm es que se pueden instalar paquetes de manera muy sencilla a través de su interfaz gráfico. Pongamos que por ejemplo quisieras instalar la librería *numpy*. Ve a *Preferencias*, *Proyecto* y en *Proyect Interpreter* podrás añadir librerías con haciendo click en el`+`.
