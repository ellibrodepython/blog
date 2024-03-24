---
layout: default
title: 📕 Context Managers
parent: 🛠 07. Excepciones
description: Los gestores de contexto o context managers son una herramienta de Python que nos permite ejecutar dos secciones de código al usar el bloque with. La primera sección se ejecuta al entrar al bloque, y la segunda al salir del mismo, siendo esta segunda ejecutada siempre (aunque ocurra una excepción). Son típicamente usados junto a recursos como ficheros.
order: 78
nav_order: d
permalink: /context-managers-python
---

# Gestores de contexto

Tal vez nunca hayas oído hablar de los gestores de contexto o *context managers*, pero si has trabajado con [ficheros](/leer-archivos-python/) ya los has usado sin darte cuenta. Si alguna vez has visto la cláusula `with`, todo lo que pasa por debajo hace uso de los gestores de contexto.

Realmente no ofrecen ninguna funcionalidad nueva, pero permiten ahorrar código eliminando todo lo que sea repetitivo o *boilerplate*. En pocas palabras, permiten ejecutar dos tareas de manera automática, la primera al entrar al `with` y la segunda al salir del mismo.

El ejemplo más típico es el siguiente. Abrimos un fichero, escribimos contenido en él, y lo cerramos.


```python
# Haciendo uso de los context managers
with open('fichero.txt', 'w') as fichero:
    fichero.write('Hola!')
```

¿Cómo que lo cerramos? Pues sí, aunque no se especifique expresamente, por debajo Python ejecutará la función `close()` cuando se salga del bloque `with`. Es importante notar también que la variable `fichero` no será accesible fuera del `with`, únciamente dentro.

El siguiente código es totalmente equivalente al anterior, pero sin hacer uso de los *context managers*, simplemente de [las excepciones](/definir-excepcion/).


```python
# Sin usar los context managers
fichero = open('fichero.txt', 'w')
try:
    fichero.write('Hola!')
finally:
    fichero.close()
```

Como puedes ver, nos podemos ahorrar algunas líneas de código usando los gestores de contexto. Su uso también nos permite dotar a nuestro código de mayor expresivadad, una de las grandes ventajas de Python.

Su uso se extiende también a otras clases como `Lock` y es también común verlos en bases de datos. Siempre que tengamos unos recursos que son bloqueados para ser usados, y después necesiten ser liberados pase lo que pase (aunque ocurra una excepción), los gestores de contexto serán una buena idea.

Llegados a este punto ya sabemos usar los gestores de contexto que vienen con Python, pero ¿y si quisiéramos definir uno nosotros? A continuación lo vemos.

## Implementación con clases

Si quieres definir tu propio gestor de contexto, existen dos formas de hacerlo:
* Con una **clase**: Implementando los métodos *dunder* `__enter__` y `__exit__` en tu clase.
* Con **decoradores**: Usando el decorador `@contextmanager`.

Veamos la primera forma usando [clases](/programacion-orientada-a-objetos/). Lo primero que tenemos que hacer es definir nuestra clase, e implementar los siguientes métodos:
* `__init__`: Este método es llamado automáticmente al entrar al bloque `with`. Lo que devuelva este método será asignado a la variable que especifiquemos a continuación del `as`. Es común que esto sea el recurso que vamos a utilizar, un fichero por ejemplo.
* `__exit__`: Este método será llamado al salir del `with` y contiene las tareas de limpieza que queremos ejecutar. Lo más importante es que este método se llama siempre, incluso aunque ocurra una excepción. Sería por lo tanto equivalente al uso del bloque `except`. Trabajando con ficheros, aquí se cerraría el archivo que ha sido abierto anteriormente.

Veamos un ejemplo. Implementamos los métodos descritos con un simple `print()` para ver lo que pasa. Podemos ver como efectivamente son llamados.


```python
class MiGestor:
    def __enter__(self):
        print("Entra en __enter__")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Entra en __exit__")

with MiGestor() as f:
    print("Hola")
    
# Entra en __enter__
# Hola
# Entra en __exit__
```


Como se puede ver, Python llama por debajo a ambos métodos, primero al `__enter__` y después al `__exit__`.

Vamos a complicarlo un poco más. Como hemos indicado, el método `__exit__` es ejecutado aunque ocurra una excepción. Vamos por lo tanto a forzar una y ver que pasa.


```python
with MiGestor() as f:
    raise Exception
    
# Entra en __enter__
# Entra en __exit__
```

Como era de esperar, el contenido del método `__exit__` también es ejecutado. Tal vez te hayas fijado en los atributos de entrada del método. Son usados para obtener más información sobre la excepción que ocurrió y poder actuar en consecuencia. Son los siguientes:
* **exc_type**: Tipo de excepción que fue lanzada. En nuestro ejemplo sería `<class 'Exception'>`
* **exc_value**: Valor de la excepción en el caso de que fuera proporcionado.
* **traceback**: Objecto `traceback` con más información acerca de la excepción.

Una vez sabido esto, ya estamos en condiciones de implementar nuestro propio gestor de contexto con un ejemplo un poco más realista. Vamos a crear nuestro propia clase que envuelva a un fichero con un gestor de contexto. Esta clase abrirá y cerrará un fichero haciendo uso de los gestores de contexto.


```python
class MiClaseFichero:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def __enter__(self):
        self.fichero = open(self.nombre_fichero, 'w')
        return self.fichero

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichero:
            self.fichero.close()
```

Vayamos parte por parte:
* En el `__init__` guardamos el nombre del fichero que queremos crear, nada nuevo.
* En el `__enter__` creamos un fichero, lo almacenamos en nuestra clase, y devolvemos la referencia que será usada dentro del `with`.
* Por último en el `__exit__` cerramos el fichero si estaba abierto.

Una vez definida la clase, ya estamos en condiciones de usarla como hemos visto anteriormente.


```python
with MiClaseFichero("fichero.txt") as fichero:
    fichero.write("Hola!")
```

Por supuesto se trata de un ejemplo didáctico, si quieres leer un fichero simplemente usa las funciones que Python proporciona por defecto.

## Implementación con decoradores

La programación orientada a objetos es muy útil, pero no conviene abusar de ella. Tal vez te encuentres en una situación donde no sea realmente necesario crear una clase. Por suerte, también podemos definir gestores de contexto con [decoradores](/decoradores-python/).

Para ello puedes usar la librería [contextlib](https://docs.python.org/3/library/contextlib.html). Su uso es muy similar pero tal vez sea un poco más complejo si no conoces los [generadores](/yield-python/) y el uso del `yield`.


```python
from contextlib import contextmanager

@contextmanager
def gestor_fichero(nombre_fichero):
    try:
        fichero = open(nombre_fichero, 'w')
        yield fichero
    finally:
        fichero.close()
```

Como puedes ver, el contenido del `try` sería el equivalente al contenido del `__enter__` y el `finally` al del `__exit__`. Una vez tenemos definida nuestra función, podemos usarla de la misma forma que hemos visto anteriormente.


```python
with gestor_fichero("fichero.txt") as fichero:
    fichero.write("Hola!")
```

# Anidando diferentes `with`

Es posible también anidar diferentes `with`, es decir, realizar una nueva llamada al `with` sin haber salido del bloque anterior.

Esto puede dar lugar a códigos de lo más creativos como el que mostramos a continuación. Se trata de un generador de índices, como el que se podría encontrar en un libro. Cada vez que se crea un nuevo bloque `with`, se añade un nuevo nivel y se van numerando de cero a `n`, lo que modifica la función `print`.


```python
class Indice:
    def __init__(self):
        self.level = -1
        self.numeracion = [0]

    def __enter__(self):
        self.level += 1
        self.numeracion.append(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.numeracion[self.level] = 0
        self.numeracion.pop()
        self.level -= 1

    def print(self, text):
        self.numeracion[self.level] += 1
        numer = [str(i) for i in self.numeracion[:self.level+1]]
        print(f"{'  '*self.level}{'.'.join(numer)} {text}")
```

Usando la clase `Indice`, podemos generar el índice de un libro. La llamada a la función `print` del índice tendrá una funcionalidad distinta dependiendo de en que bloque se encuentre su llamada. Es decir, la función imprime algo diferente dependiendo del **contexto** en el que se esté, entendiendo por contexto el número de bloques `with` que haya anidados.


```python
with Indice() as indice:
    indice.print('Apartado')
    with indice:
        indice.print('Apartado')
        indice.print('Apartado')
        indice.print('Apartado')
        indice.print('Apartado')
        with indice:
            indice.print('Apartado')
            indice.print('Apartado')
            with indice:
                indice.print('Apartado')
                indice.print('Apartado')
    indice.print('Apartado')
    indice.print('Apartado')
    
# 1 Apartado
#   1.1 Apartado
#   1.2 Apartado
#   1.3 Apartado
#   1.4 Apartado
#     1.4.1 Apartado
#     1.4.2 Apartado
#       1.4.2.1 Apartado
#       1.4.2.2 Apartado
# 2 Apartado
# 3 Apartado
```