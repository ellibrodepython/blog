---
layout: default
title: Leer Archivo en Python
title_nav: 📙 Leer archivos
parent: 📥 08. Ficheros
description: Para leer archivos en Python podemos usar la función open() de la librería estándar. Dicha función nos devuelve un objeto que podemos usar para leer el fichero usando diferentes métodos como read(), readline() o readlines(). Es importante una vez abierto el fichero cerrarlo con close().
order: 80
nav_order: a
permalink: /leer-archivos-python
---

# Leer archivos en Python

Al igual que en otros lenguajes de programación, en Python es posible **abrir ficheros y leer su contenido**. Los ficheros o archivos pueden ser de lo más variado, desde un simple texto a contenido binario. Para simplificar nos centraremos en **leer un fichero de texto**. Si quieres aprender como escribir en un fichero te lo explicamos en este otro [post](/escribir-archivos-python/).

Imagínate entonces que tienes un fichero de texto con unos datos, como podría ser un `.txt` o un `.csv`, y quieres leer su contenido para realizar algún tipo de procesado sobre el mismo. Nuestro fichero podría ser el siguiente.


```
# contenido del fichero ejemplo.txt
Contenido de la primera línea
Contenido de la segunda línea
Contenido de la tercera línea
Contenido de la cuarta línea
```

Podemos abrir el fichero con la función `open()` pasando como argumento el nombre del fichero que queremos abrir.


```python
fichero = open('ejemplo.txt')
```

## Método `read()`

Con `open()` tendremos ya en `fichero` el contenido del documento listo para usar, y podemos imprimir su contenido con `read()`. El siguiente código imprime **todo el fichero**.


```python
print(fichero.read())
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea
```


## Método `readline()`

Es posible también leer un **número de líneas determinado** y no todo el fichero de golpe. Para ello hacemos uso de la función `readline()`. Cada vez que se llama a la función, se lee una línea.


```python
fichero = open('ejemplo.txt')
print(fichero.readline())
print(fichero.readline())
# Contenido de la primera línea
# Contenido de la segunda línea
```



Es **muy importante saber** que una vez hayas leído todas las línea del archivo, la función ya no devolverá nada, porque se habrá llegado al final. Si quieres que `readline()` funcione otra vez, podrías por ejemplo volver a leer el fichero con `open().`

Otra forma de usar `readline()` es pasando como argumento un número. Este número leerá un **determinado número de caracteres**. El siguiente código lee todo el fichero carácter por carácter.


```python
fichero = open('ejemplo.txt')
caracter = fichero.readline(1)
while caracter != "":
    #print(caracter)
    caracter = fichero.readline(1)
```

## Método `readlines()`

Existe otro método llamado `readlines()`, que devuelve una lista donde **cada elemento es una línea del fichero**.


```python
fichero = open('ejemplo.txt')
lineas = fichero.readlines()
print(lineas)
#['Contenido de la primera línea\n', 'Contenido de la segunda línea\n',
#'Contenido de la tercera línea\n', 'Contenido de la cuarta línea']
```


De manera muy sencilla podemos iterar las líneas e imprimirlas por pantalla.


```python
fichero = open('ejemplo.txt')
lineas = fichero.readlines()
for linea in lineas:
    print(linea)
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea
```


## Argumentos de `open()`

Hasta ahora hemos visto la función `open()` con tan sólo un argumento de entrada, el nombre del fichero. Lo cierto es que existe un segundo argumento que es importante especificar. Se trata del **modo de apertura del fichero**. En [la documentación oficial](https://docs.python.org/3/library/functions.html#open "la documentación oficial") se explica en detalle.
* 'r': Por defecto, para leer el fichero.
* 'w': Para escribir en el fichero.
* 'x': Para la creación, fallando si ya existe.
* 'a': Para añadir contenido a un fichero existente.
* 'b': Para abrir en modo binario.

Por lo tanto lo estrictamete correcto si queremos leer el fichero sería hacer lo siguiente. Aunque el modo `r` sea por defecto, es una buena práctica indicarlo para darle a entender a otras personas que lean nuestro código que no queremos modificarlo, tan solo leerlo.


```python
fichero = open('ejemplo.txt', 'r')
```

## Cerrando el fichero

Otra cosa que debemos hacer cuando trabajamos con ficheros en Python, es **cerrarlos una vez que ya hemos acabado con ellos**. Aunque es verdad que el fichero normalmente acabará siendo cerrado automáticamente, es importante especificarlo para evitar tener comportamientos inesperados.

Por lo tanto si queremos cerrar un fichero sólo tenemos que usar la función `close()` sobre el mismo. Por lo tanto tenemos tres pasos:
* Abrir el fichero que queramos. En modo texto usaremos 'r'.
* Usar el fichero para recopilar o procesar los datos que necesitábamos.
* Cuando hayamos acabado, cerramos el fichero.


```python
fichero = open('ejemplo.txt', 'r')
# Usar la variable fichero
# Cerrar el fichero
fichero.close()
```

Existen otras formas de hacerlo, como con el uso de **excepciones** que veremos en otros posts. Un ejemplo sería el siguiente. No pasa nada si aún no entiendes el uso del `try` y `finally`, por ahora quédate con que la sección `finally` **se ejecuta siempre** sin importar si hay un error o no. De esta manera el `close()` siempre será ejecutado.


```python
fichero = open('ejemplo.txt')
try:
    # Usar el fichero
    pass
finally:
    # Esta sección es siempre ejecutada
    fichero.close()
```

Y por si no fuera poco, existe otra forma de cerrar el fichero automáticamente. Si hacemos uso se `with()`, el fichero **se cerrará automáticamente una vez se salga de ese bloque** de código.


```python
with open('ejemplo.txt') as fichero:
    # Usar el fichero. Se cerrará automáticamente
    pass
```

## Ejemplos

Como ya hemos visto `readline()` lee línea por línea el fichero. También hacemos uso de un bucle while para leer líneas mientras que no se haya llegado al final. Es por eso por lo que comparamos `linea != ''`, ya que se devuelve un string vació cuando se ha llegado al final.


```python
with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()

#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea
```

Nos podemos ahorrar alguna línea de código si hacemos lo siguiente, ya que `readlines()` nos devuelve directamente una lista que podemos iterar con las líneas.


```python
with open('ejemplo.txt', 'r') as fichero:
    for linea in fichero.readlines():
        print(linea, end='')
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea
```


Pero puede ser simplificado aún más de la siguiente manera. Nótese que usamos el `end=''` para decirle a Python que no imprima el salto de línea `\n` al final del print.


```python
with open('ejemplo.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')
#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea
```
