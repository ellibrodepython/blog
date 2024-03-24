---
layout: default
title: 📙 Escribir archivos
parent: 📥 08. Ficheros
description: Te explicamos como escribir archivos en Python. En Python al igual que en otros lenguajes de programación es posible escribir el contenido de diferentes variables en un archivo, como podría ser un txt o un csv. Para ello es necesario hacer uso de la función open() con el argumento "w" o "a".
order: 81
nav_order: b
permalink: /escribir-archivos-python
---

# Escribir archivos en Python

A continuación te explicamos **como escribir datos en un fichero usando Python**. Imagínate que tienes unos datos que te gustaría guardar en un fichero para su posterior análisis. Te explicamos como guardarlos en un fichero, por ejemplo, `.txt`. Si también quieres aprender como leer un fichero en Python [te lo explicamos en este otro post](/leer-archivos-python/ "te lo explicamos en este otro post").

Lo primero que debemos de hacer es crear un objeto para el fichero, con el nombre que queramos. Al igual que vimos en el post de leer ficheros, además del nombre se puede pasar un segundo parámetro que indica el modo en el que se tratará el fichero. Los más relevantes en este caso son los siguientes. Para más información consulta [la documentación oficial](https://docs.python.org/3/library/functions.html#open "la documentación oficial").
* 'w': Borra el fichero si ya existiese y crea uno nuevo con el nombre indicado.
* 'a': Añadirá el contenido al final del fichero si ya existiese (*append* end Inglés)
* 'x': Si ya existe el fichero se devuelve un error.

Por lo tanto con la siguiente línea estamos creando un fichero con el nombre *datos_guardados.txt*.


```python
# Abre un nuevo fichero
fichero = open("datos_guardados.txt", 'w')
```

Si por lo contrario queremos añadir el contenido al ya existente en un fichero de antes, podemos hacerlo en el modo *append* como hemos indicado.


```python
# Abre un nuevo y añade el contenido al final
fichero = open("datos_guardados.txt", 'a')
```

## Método `write()`

Ya hemos visto como crear el fichero. Veamos ahora como podemos añadir contenido. Empecemos escribiendo un texto.


```python
fichero = open("datos_guardados.txt", 'w')
fichero.write("Contenido a escribir")
fichero.close()
```

Por lo tanto si ahora abrimos el fichero `datos_guardados.txt`, veremos como efectivamente contiene una línea con *Contenido a escribir*. ¿A que es fácil?

Es **muy importante** el uso de `close()` ya que si dejamos el fichero abierto, podríamos llegar a tener un comportamiento inesperado que queremos evitar. Por lo tanto, siempre que se abre un fichero **es necesario cerrarlo** cuando hayamos acabado.

Compliquemos un poco más las cosas. Ahora vamos a guardar una lista de elementos en el fichero, donde cada elemento de la lista se almacenará en una línea distinta.


```python
# Abrimos el fichero
fichero = open("datos_guardados.txt", 'w')

# Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Plátano"]

# Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")

# Cerramos el fichero
fichero.close()
```

Si te fijas, estamos almacenando la línea mas `\n`. Es importante añadir el salto de línea porque por defecto no se añade, y si queremos que cada elemento de la lista se almacena en una línea distinta, será necesario su uso.

## Método `writelines()`

También podemos usar el método `writelines()` y pasarle una lista. Dicho método se encargará de guardar todos los elementos de la lista en el fichero.


```python
fichero = open("datos_guardados.txt", 'w')
lista = ["Manzana", "Pera", "Plátano"]

fichero.writelines(lista)
fichero.close()

# Se guarda
# ManzanaPeraPlátano
```

Tal vez te hayas dado cuenta de que en realidad lo que se guarda es *ManzanaPeraPlátano*, todo junto. Si queremos que cada elemento se almacene en una línea distinta, deberíamos añadir el salto de línea en cada elemento de la lista como se muestra a continuación.


```python
fichero = open("datos_guardados.txt", 'w')
lista = ["Manzana\n", "Pera\n", "Plátano\n"]

fichero.writelines(lista)
fichero.close()

# Se guarda
# Manzana
# Pera
# Plátano
```

## Uso del `with`

Podemos ahorrar una línea de código si hacemos uso de lo siguiente. En este caso nos podemos ahorrar la llamada al `close()` ya que se realiza automáticamente. El código anterior se podría reescribir de la siguiente manera.


```python
lista = ["Manzana\n", "Pera\n", "Plátano\n"]
with open("datos_guardados.txt", 'w') as fichero:
     fichero.writelines(lista)
```
## Ejemplos escribir ficheros en Python
El uso de 'x' hace que **si el fichero ya existe se devuelve un error**. En el siguiente código creamos un fichero e inmediatamente después intentamos crear un fichero con el mismo nombre con la opción 'x'. Por lo tanto se devolverá un error.


```python
f = open("mi_fichero.txt", "w")
# f = open("mi_fichero.txt", "x")
# Error! Ya existe
```

En este otro ejemplo vamos a usar un fichero para establecer una comunicación entre dos funciones. A efectos prácticos puede no resultar muy útil, pero es un buen ejemplo para mostrar la lectura y escritura de ficheros.

Tenemos por lo tanto una función `escribe_fichero()` que recibe un mensaje y lo escribe en un fichero determinado. Y por otro lado tenemos una función `lee_fichero()` que devuelve el mensaje que está escrito en el fichero.

Date cuenta lo interesante del ejemplo, ya que podríamos tener estos dos códigos ejecutándose en diferentes maquinas o procesos, y **podrían comunicarse a través del fichero**. Por un lado se escribe y por el otro se lee.


```python
# Escribe un mensaje en un fichero
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write(mensaje)

# Leer el mensaje del fichero        
def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    # Borra el contenido del fichero para dejarlo vacío
    f = open('fichero_comunicacion.txt', 'w')
    f.close()
    return mensaje

escribe_fichero("Esto es un mensaje")
print(lee_fichero())
```
