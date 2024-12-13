---
layout: default
title_nav: 📙 Argparse en Python
title: Argparse en Python
parent: 🚀 09. Test y Documentación
description: Un Command Line Interface o Interfaz de Línea de Comandos es un método que permite a los usuarios interactuar con nuestro código, pudiendo ser usado para pasar variables al mismo. Es posible crearlos usando argparse en Python.
order: 87
nav_order: c
permalink: /python-argparse
---

# Argparse en Python

## Introducción al Command Line Interface

Los *Command Line Interface* o interfaces de línea de comandos (comúnmente abreviado como *CLI*) son una herramienta que ofrecen gran cantidad de programas para interactuar con ellos. Si alguna vez has usado el comando `ls` o `mkdir` de Linux, ya has usado un *CLI*.

El comando `ls` permite listar directorios y ficheros.
```console
$ ls -ta
```

El comando `mkdir` permite la creación de directorios, de ahí su nombre de *make dir*.
```console
$ mkdir -p foo
```

En ambos comandos podemos identificar tres partes:
* Por un lado tenemos el **comando** `ls` o `mkdir`, que determina el código o librería que se va a usar.
* Después tenemos las **opciones** como `-ta` o `-p`, que modifican el comportamiento del comando que precede. Por ejemplo, la opción `-t` ordena los ficheros por orden de modificación.
* Por ultimo tenemos los **argumentos** que se le pasan al comando. Pueden no existir como en el caso de `ls`, o tener uno como en el caso de `mkdir`, que indica el nombre del fichero a crear.

Los *CLI* son una herramienta perfecta para exponer tu código a que pueda ser usado por otras personas, de manera sencilla y encapsulando el contenido que está en el interior. De ahí su nombre de interfaz, que no es gráfico, sino de línea de comandos.

## Command Line Interfaces en Python

Vamos a ver un ejemplo más relacionado con Python. Imagina que nos han encargado hacer un software para resolver un problema determinado, y que ya tenemos todo el código listo y funcionando. Por las características del proyecto, dicho software no tendrá un interfaz gráfico de usuario, pero si que será necesario recibir diferentes parámetros para cambiar el comportamiento del programa. Es decir, **tenemos unas variables que serán recibidas desde fuera**.

Supongamos que tenemos el siguiente código, donde tenemos dos parámetros `a` y `b` que se suman, restan o multiplican en función del valor de `operacion`.

```python
# calculadora.py

# Tipo de operacion: suma/resta/multiplicación
operacion = "suma"

# Parámetros de la operación
a = 4
b = 7

if operacion == "suma":
    print(a+b)
elif operacion == "resta":
    print(a-b)
elif operacion == "multiplicacion":
    print(a*b)
```

Lo que queremos por tanto es que los parámetros `a`, `b` y `operacion` sean recibidos desde fuera de nuestro programa, a través de la línea de comandos.

Imaginémonos que la persona que va a usar este código ni si quiera sabe Python, pero quiere usar nuestro software como una calculadora. En este caso necesitaremos abstraer al usuario del código, y darle una ventana al exterior desde la que pueda simplemente decir el valor de `a`, `b` y la `operacion`, y obtener el resultado.

Nuestro objetivo es por tanto buscar una manera en la que un usuario pueda pasar por terminal los valores de `a`, `b` y `operacion` para que sean usados por el código. Una forma sería la siguiente.

```console
$ python calculadora.py 5 2 suma
```

Otra opción es usando nombres para los argumentos.
```console
$ python calculadora.py --a=5 --b=2 --operacion=suma
```

Este será por tanto el problema que resolveremos a lo largo de este artículo, utilizando diferentes maneras y explorando las opciones que Python nos ofrece.

## Creando un CLI sin argparse

La primera forma que tenemos de que un script reciba argumentos desde el terminal es usando el módulo [sys](https://docs.python.org/3/library/sys.html).

```python
# calculadora.py
import sys
print(sys.argv)
```

La siguiente llamada captura todo lo que se pasa después de `python`. Como puedes ver, el primer elemento `argv[0]` nos devuelve el nombre del script. Por otro lado, se capturan todos y cada uno de los argumentos que se pasan a la derecha del mismo.

```console
$ python calculadora.py 5 2 suma
['calculadora.py', '5', '2', 'suma']
```

Con esta [lista](/listas-en-python) ya tendríamos todo lo que necesitamos para usar nuestra `calculadora.py`, pero existe una manera mucho mejor de tratar los argumentos, y es usando la librería `argparse`. Veamos como funciona.


## Creando un CLI con argparse

La librería [argparse](https://docs.python.org/3/library/argparse.html) fue introducida en Python en la [PEP389](https://www.python.org/dev/peps/pep-0389/) y permite crear *CLI* para todo tipo de proyectos, ofreciendo un amplio abanico de posibilidades útiles hasta en los proyectos más complejos.

### Introducción a argparse

Vamos a comenzar con una primera aproximación de lo que sería el uso de `argparse`, creando un interfaz para nuestra calculadora mostrada anteriormente:
* Importamos la librería.
* Creamos un `ArgumentParser`.
* Añadimos argumentos.
* Y *parseamos* los argumentos.

```python
# script.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("b")
parser.add_argument("operacion")

args = parser.parse_args()
variables = vars(args)
print(variables)
```

Si llamamos al código anterior en el terminal, podemos ver como ya tenemos todo lo necesario para nuestra calculadora.

```console
$ python script.py 7 7 suma
{'a': '7', 'b': '7', 'operacion': 'suma'}
```

Con esta primera aproximación ya tendríamos todas las variables que necesitamos en el [diccionario](/diccionarios-en-python) `variables`, pero aunque pueda parecer que ya hemos resuelto nuestro problema, tenemos los siguientes problemas:
* Estamos usando parámetros **posicionales**, lo que significa que estamos obligados a pasar primero `a`, después `b` y por último `c`. Si pasamos los argumentos en otro orden, romperemos el programa.
* No especificamos los **tipos de las variables**, por defecto todas son [string](/cadenas-python) cuando en realidad `a` y `b` deberían ser [integer](/entero-en-python). Esto es un problema ya que 7+7 con cadenas es 77.
* El parámetro `operacion` debería tomar sólo **valores discretos**, ya que únicamente queremos suma/resta/multiplicación. Deberíamos forzar un error si se pasa una operación no soportada.
* Por defecto, **todos los parámetros son obligatorios**, pero esto puede no ser siempre el caso. Imagina que por defecto queremos sumar, en el caso de que no se especifique la `operacion`.
* Por último, no estamos ofreciendo ninguna **documentación**, por lo que la persona que tenga nuestro software no sabrá como usarlo.

En vista a lo anterior, podemos realizar las siguientes modificaciones en el código para hacerlo más correcto. Fijémonos en los cambios.
* El uso de `-a` y `--numero_a` permite indicar el nombre del parámetro que estamos pasando, por lo que ya no será necesario hacerlo en un orden fijo. Se utiliza un guión para la abreviación del argumento y dos para el nombre completo.
* Añadimos `type` a cada argumento.
* Añadimos `choices` a la operación, para que de un error si seleccionamos una no soportada.
* Ponemos la operación como parámetro opcional `required=False` y asignamos un valir por defecto `default` en el caso de que no se proporcione.
* Añadimos documentación con `description` y `help` para que un usuario ajeno a nuestro código sepa utilizarlo.

Poniéndolo todo junto en nuestro programa `calculadora.py`, tendríamos algo como lo siguiente.

```python
# calculadora.py
import argparse

parser = argparse.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b')
parser.add_argument('-a', '--numero_a', type=int, help='Parámetro a')
parser.add_argument('-b', '--numero_b', type=int, help='Parámetro b')
parser.add_argument('-o', '--operacion',
                    type=str,
                    choices=['suma', 'resta', 'multiplicacion'],
                    default='suma', required=False,
                    help='Operación a realizar con a y b')

args = parser.parse_args()

if args.operacion == 'suma':
    print(args.numero_a + args.numero_b)
elif args.operacion == 'resta':
    print(args.numero_a - args.numero_b)
elif args.operacion == 'multiplicacion':
    print(args.numero_a * args.numero_b)
```

Como vemos a continuación, hay diferentes formas de realizar la llamada a nuestro *script* y son todas equivalentes. La forma más sencilla es **usando las abreviaciones** como se muestra a continuación.
```console
$ python calculadora.py -a 1 -b 4 -o suma
5
```

Pero es también posible **usar el nombre completo**.
```console
$ python calculadora.py --numero_a 7 --numero_b 3 --operacion multiplicacion
21
```

O también podemos **usar el signo igual** `=` para realizar la asignación.

```console
$ python calculadora.py -a=7 -b=3 --operacion=multiplicacion
21
```

Podemos **alterar el orden** de los parámetros ya que no son posicionales.

```console
$ python calculadora.py -b=3 --operacion=multiplicacion -a=7
21
```

Una vez vistas como se realizarían las llamadas, veamos otras características. Por ejemplo, para acceder a la **documentación** usamos `--help`.

```console
$ python calculadora.py --help

usage: calculadora.py [-h] [-a NUMERO_A] [-b NUMERO_B] [-o {suma,resta,multiplicacion}]

Calculadora, suma/resta/multiplica a y b

optional arguments:
  -h, --help            show this help message and exit
  -a NUMERO_A, --numero_a NUMERO_A
                        Parámetro a
  -b NUMERO_B, --numero_b NUMERO_B
                        Parámetro b
  -o {suma,resta,multiplicacion}, --operacion {suma,resta,multiplicacion}
                        Operación a realizar con a y b

```

Obtendremos un error si usamos un tipo incorrecto. Por ejemplo `a` no puede ser una cadena.

```console
$ python calculadora.py -a=Hola -b=Hola --operacion=multiplicacion
usage: calculadora.py [-h] [-a NUMERO_A] [-b NUMERO_B] [-o {suma,resta,multiplicacion}]
calculadora.py: error: argument -a/--numero_a: invalid int value: 'Hola'
```

Por otro lado `operacion` sólo puede tomar los valores suma/resta/multiplicación, por lo que **un valor diferente dará error**.

```console
python calculadora.py -a=7 -b=3 -o=Hola
usage: calculadora.py [-h] [-a NUMERO_A] [-b NUMERO_B] [-o {suma,resta,multiplicacion}]
calculadora.py: error: argument -o/--operacion: invalid choice: 'Hola' (choose from 'suma', 'resta', 'multiplicacion')
```

Por último, el parámetro `operacion` es **opcional**, tomando el valor de `suma` por defecto.

```python
$ python calculadora.py -a=7 -b=3
10
```

Como podemos observar el uso de `type`, `help`, `choice`, `default` y `required` nos ofrecen funcionalidades extra que hacen que nuestra *CLI* sea más completa. Si bien es cierto que son los más usados, Python ofrece otra muchas funcionalidades que vemos a continuación.

### Usando abreviaciones

Es común soportar el uso de argumentos con `-` y `--` como hemos visto anteriormente, siendo su uso heredado de [gnu](https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html). Normalmente se usa `-` para una abreviación, y `--` para el nombre completo, siendo el segundo el usado para nombrar a la variable que almacenará el argumento.

Por otro lado, Python permite usar abreviaciones del argumento automáticamente. Es decir, si definimos `--operacion`, el argumento `--oper` funcionará correctamente.

```python
# abreviaciones.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--operacion')

args = parser.parse_args()
print(vars(args))
```

Las siguiente llamadas son todas válidas y producen el mismo resultado.

```console
$ python abreviaciones.py -o suma
{'operacion': 'suma'}

$ python abreviaciones.py --operacion suma
{'operacion': 'suma'}

$ python abreviaciones.py --opera suma
{'operacion': 'suma'}

$ python abreviaciones.py --op suma
{'operacion': 'suma'}
```

### Cambiar el prefijo de los argumentos

Anteriormente hemos visto como por defecto los argumentos se pasan usando `-`, pero es posible también cambiar el prefijo usando `prefix_chars` al crear el `ArgumentParser`.

```python
# cambio_prefijo.py
import argparse

parser = argparse.ArgumentParser(prefix_chars='+')
parser.add_argument('+a')
parser.add_argument('+b')

args = parser.parse_args()
print(vars(args))
```

Ahora si queremos consultar la ayuda, deberemos usar el nuevo prefijo.
```console
$ python cambio_prefijo.py +h

usage: cambio_prefijo.py [+h] [+a A] [+b B]

optional arguments:
  +h, ++help  show this help message and exit
  +a A
  +b B
```

Y podemos pasar parámetros de la siguiente manera.
```console
$ python cambio_prefijo.py +a 10 +b 7
{'a': '10', 'b': '7'}
```

### Pasando argumentos desde un archivo

Cuando trabajamos con un número muy elevado de argumentos, puede resultar interesante moverlos a un fichero, lo que nos permitirá simplificar la llamada y hacerla más legible. ¿Te imaginas pasar 20 argumentos por el terminal?. A continuación vemos un ejemplo donde los argumentos se pasan dentro de un fichero, por lo que nuestro *script* sólo recibe el nombre del fichero.

```python
# argumentos_fichero.py
import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

parser.add_argument('-a')
parser.add_argument('-b')
parser.add_argument('-c')
parser.add_argument('-d')
parser.add_argument('-e')
parser.add_argument('-f')

args = parser.parse_args()
print(vars(args))
```

Asumiendo que tenemos el siguiente contenido almacenado en `args.txt`.
```
-a=3
-b=10
-c=1
-d=0
-e=11
-f=9
```

Podemos llamar a nuestro *script* de la siguiente forma, simplificando la llamada a un solo argumento, lo que en ciertas ocasiones puede resultar mucho más elegante.
```console
$ python argumentos_fichero.py @args.txt
{'a': '3', 'b': '10', 'c': '1', 'd': '0', 'e': '11', 'f': '9'}
```

Por último, es importante notar que el uso del fichero es una opción añadida, por lo que sigue siendo posible utilizar los argumentos como hemos visto anteriormente, o incluso combinarlos, siendo el último el que tiene prioridad.

```console
$ python argumentos_fichero.py @args.txt -a 200
{'a': '200', 'b': '10', 'c': '1', 'd': '0', 'e': '11', 'f': '9'}
```

### Argumentos excluyentes

Otra utilidad muy importante es la definición de grupos *mutually exclusive* o mutuamente excluyentes. Su uso nos permite hacer que dos argumentos no puedan ser utilizados a la vez, es decir, que sean excluyentes. Para ello creamos un grupo con `add_mutually_exclusive_group` y los argumentos que añadamos al mismo no podrán ser usados simultáneamente.

```python
# excluyentes.py
import argparse

parser = argparse.ArgumentParser()
grupo = parser.add_mutually_exclusive_group()

grupo.add_argument('-f', '--foo')
grupo.add_argument('-b', '--bar')

args = parser.parse_args()
print(vars(args))
```

La siguiente llamada por tanto no es posible, ya que estamos utilizando ambos argumentos.

```console
$ python excluyentes.py -f 3 -b 10

usage: excluyentes.py [-h] [-f FOO | -b BAR]
excluyentes.py: error: argument -b/--bar: not allowed with argument -f/--foo
```


### Usando acciones para los argumentos

Otra característica muy útil que nos ofrece `argparse`, es el uso de acciones personalizadas para cada argumento utilizando `action`. Esto nos permite modificar como el argumento que introducimos es *parseado* y almacenado en la variable, pudiendo usar acciones por defecto o definirlas nosotros mismos.

Las acciones que `argparse` nos ofrece por defecto son las siguientes:
* **store**: Es el comportamiento por defecto que hemos visto anteriormente. Simplemente almacena el valor que se pasa con el argumento en una variable.
* **store_const**: Almacena una constante en la variable, cuyo valor debemos especificar en `const`.
* **store_true**: Almacena el [booleano](/booleano-python) `True` en la variable. Muy útil para definir *flags* que no reciben un valor concreto.
* **store_false**: Análogo al anterior pero almacena `False`.
* **append**: Añade el argumento a una lista. Útil cuando un argumento es pasado múltiples veces.
* **append_const**: Similar a `append` pero almacena en la lista la constante especificada en `const`.
* **count**: Cuenta el número de veces que un determinado argumento es pasado.
* **help**: Muestra la ayuda del programa y finaliza sin hacer nada más.
* **version**: Muestra la versión del programa y finaliza la ejecución.

Veamos unos ejemplos con cada tipo de acción. Como ya hemos visto anteriormente, el uso de `store` no tiene ningún misterio ya que es el comportamiento que tenemos por defecto.
```python
# store.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store')
args = parser.parse_args()
print(vars(args))
```

Y podemos llamar a nuestro *script* como ya sabemos.
```console
$ python store.py -a 3
{'a': '3'}
```

Por otro lado, `store_const` permite almacenar una constante determinada por el valor de `const`.
```python
# store_const.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store_const', const="99")
args = parser.parse_args()
print(vars(args))
```

La llamada al *script* se hace de la siguiente manera, pero nótese que el argumento no acepta parámetros a continuación. Resulta lógico, puesto que ya estamos diciendo que queremos almacenar `const`.
```console
$ python store_const.py -a
{'a': '99'}

$ python store_const.py -a 1
usage: store_const.py [-h] [-a]
store_const.py: error: unrecognized arguments: 1
```

También podemos usar `store_true` para almacenar `True` en la variable o `store_false` para almacenar `False`.
```python
# store_true_false.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='store_true')
parser.add_argument('-b', action='store_false')
args = parser.parse_args()
print(vars(args))
```

Y podemos llamar al script de la siguiente manera.
```console
$ python store_true_false.py -a -b
{'a': True, 'b': False}

$ python store_true_false.py -ab
{'a': True, 'b': False}
```

Por otro lado, podemos usar `append` para pasar el mismo argumento varias veces, siendo cada valor almacenado en la misma lista.

```python
# append.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='append')
args = parser.parse_args()
print(vars(args))
```

Pasamos el argumento `-a` tres veces con distintos valores y podemos ver como son almacenados en una lista.
```console
$ python append.py -a 1 -a 2 -a 3
{'a': ['1', '2', '3']}
```

Análogamente podemos usar `append_const`, que almacena el valor de `const` en la lista.
```python
# append_const.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='append_const', const=0)
args = parser.parse_args()
print(vars(args))
```

Podemos llamarlo de la siguiente manera. Es importante notar que dado que el argumento no acepta valores, podemos usar un solo `-`.

```console
$ python append_const.py -a -a -a
{'a': [0, 0, 0]}

$ python append_const.py -aaa
{'a': [0, 0, 0]}
```

Por otro lado, el uso de `count` cuenta el número de veces que un argumento es pasado.

```python
# count.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action='count')
args = parser.parse_args()
print(vars(args))
```

Si pasamos múltiples veces el mismo argumento, la variable incrementará en uno cada vez.
```console
$ python count.py -a -a -a
{'a': 3}

$ python count.py -aaa
{'a': 3}
```

Por último, podemos usar `help` y `version` para mostrar la ayuda del programa y su versión respectivamente. Si bien es cierto que por defecto la ayuda se muestra con `-h`, esta funcionalidad nos permite modificarlo, usando por ejemplo nombre en español.

```python
# help_version.py
import argparse
parser = argparse.ArgumentParser()
parser.version = '1.0'
parser.add_argument('--ayuda', action='help')
parser.add_argument('--version', action='version')
args = parser.parse_args()
print(vars(args))
```

La siguiente llamada muestra la ayuda.
```console
$ python help_version.py --ayuda

usage: help_version.py [-h] [--ayuda] [--version]

optional arguments:
  -h, --help  show this help message and exit
  --ayuda
  --version   show program's version number and exit
```

Y de la siguiente manera podemos mostrar la versión, previa definición en el campo `version` del *parser*.
```console
$ python help_version.py --version
1.0
```

Hasta aquí hemos visto las acciones que Python nos ofrece por defecto, que deberían cubrir prácticamente todos los casos de uso que se nos puedan ocurrir. Sin embargo, si necesitáramos una funcionalidad que no existiera, siempre podríamos crear una acción personalizada creando una clase que herede de `argparse.Action`. Una vez creada e implementada dicha clase, bastaría con pasarla como `action`.

### Argumentos con múltiples valores

Hasta ahora hemos visto que los valores que pasamos a los argumentos han sido o uno o ninguno, pero es también posible que un argumento consuma múltiples valores. Los valores consumidos pueden ser modificados con `nargs` y son:
* `n`: Se consumen `n` valores por el argumento, y se almacenen en una lista.
* `?`: Se consume un sólo valor, que puede ser opcional.
* `*`: Para un número arbitrario de valores, y son almacenados en una lista.
* `+`: Similar a `*` pero requiere al menos un valor.
* `argparse.REMAINDER`: Consume todos los valores hasta el final.

Veamos unos ejemplos que es como sin duda se entiende mejor. Empecemos definiendo un **número concreto de valores** a consumir.
```python
# argumentos_variables1.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', nargs=5)
args = parser.parse_args()
print(vars(args))
```

Dado que el número de argumentos es fijo, la primera llamada es válida mientras que la segunda no.

```console
$ python argumentos_variables1.py -a 1 2 3 4 5
{'a': ['1', '2', '3', '4', '5']}

$ python argumentos_variables1.py -a 1 2
usage: argumentos_variables1.py [-h] [-a A A A A A]
argumentos_variables1.py: error: argument -a: expected 5 arguments
```

Para el caso de **un sólo valor opcional** tenemos el siguiente ejemplo.

```python
# argumentos_variables2.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', nargs='?')
args = parser.parse_args()
print(vars(args))
```

El *script* puede ser llamado con o sin ningún valor, almacenando `None` si no se pasa ningún valor, y por supuesto asumiendo que no se a definido un valor `default`.
```console
$ python argumentos_variables2.py -a 
{'a': None}

$ python argumentos_variables2.py -a 1
{'a': '1'}
```

También podemos pasar **un número arbitrario de valores**.
```python
# argumentos_variables3.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', nargs='?')
args = parser.parse_args()
print(vars(args))
```

Todas las siguiente llamadas son válidas, ya que no se especifica un número concreto de argumentos. Nótese que también puede no pasarse ningún argumento.
```console
$ python argumentos_variables3.py -a
{'a': None}

$ python argumentos_variables3.py -a 1
{'a': ['1']}

$ python argumentos_variables3.py -a 1 2 3
{'a': ['1', '2', '3']}
```

Relacionado con el anterior, también podemos pasar **un número arbitrario de valores con al menos uno**.

```python
# argumentos_variables4.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', nargs='+')
args = parser.parse_args()
print(vars(args))
```

Es decir, podemos pasar un número arbitrario de parámetros pero deberemos pasar al menos uno, por lo que la primera llamada falla.
```console
$ python argumentos_variables4.py -a
usage: argumentos_variables4.py [-h] [-a A [A ...]]
argumentos_variables4.py: error: argument -a: expected at least one argument

$ python argumentos_variables4.py -a 1 2
{'a': ['1', '2']}
```

Por último si usamos `argparse.REMAINDER` se tomarán todos los valores restantes hasta el final del comando. Dado que se toman todos los valores hasta el final, es importante declarar este argumento al final de todo, de lo contrario podríamos tenemos comportamiento inesperados.

```python
# argumentos_variables5.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a')
parser.add_argument('-b', nargs=argparse.REMAINDER)
args = parser.parse_args()
print(vars(args))
```

```console
$ python argumentos_variables5.py -a 10 -b 1 2 3 4 5
{'a': '10', 'b': ['1', '2', '3', '4', '5']}
```

### Cambiar el nombre de la variable

Hasta ahora hemos visto como el nombre del argumento y el de la variable en la que se almacena es el mismo, es decir, el argumento `--operacion` se almacena el la variable `operacion` por defecto. Imaginemos que queremos que sea otro. Pues bien, es posible mediante el uso de `dest`.

```python
# uso_dest.py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='otro_nombre')
args = parser.parse_args()
print(vars(args))
```

Como podemos ver, el argumento ya no es almacenado en la variable `a`, sino que se usará como variable `otro_nombre`.

```console
$ python uso_dest.py -a PythonMola
{'otro_nombre': 'PythonMola'}
```

## Conclusiones

Llegados a este punto, ya hemos visto todas las funcionalidades que [argparse](https://docs.python.org/3/library/argparse.html) nos ofrece. Recuerda que si tienes dudas puedes consultar la documentación oficial de Python, que aunque sea más complicada de leer, es la que debe ser usada como referencia.

Recapitulemos lo que hemos aprendido en este capítulo:
* Hemos visto qué son los *Command Line Interface* y su utilidad a la hora de ofrecer un punto de entrada a nuestro código, algo ideal cuando queremos compartirlo con otras personas para que lo usen.
* Hemos visto cómo se pueden crear CLI sencillos mediante el uso de la librería `sys`. Se trata de una opción perfectamente válida pero cuya funcionalidad es muy limitada.
* Y por último, hemos visto como crear CLI con la librería nativa de Python `argparse`, el estándar *de facto* usado, explorando desde las funcionalidades más básicas a las más avanzadas.


