---
layout: default
title: 📙 Definiendo Excepciones
parent: 🛠 07. Excepciones
description: Al igual que otros lenguajes de programación en Python se puede definir una excepción propia heredando de la clase genérica Exception(). Te lo explicamos de manera sencilla y con ejemplos.
order: 77
nav_order: c
permalink: /definir-excepcion
---

# Definiendo Excepciones

Antes de ver como se define una excepción, te recomendamos otros de nuestros posts que te ayudarán a entenderlo  mejor:
* [Programación Orientada a Objetos](/programacion-orientada-a-objetos/ "Programación Orientada a Objetos")
* [Herencia en Python](/herencia-en-python/ "Herencia en Python")
* [Excepciones en Python](/excepciones-try-except-finally/ "Excepciones en Python")


En los posts anteriores verás como **lanzar y capturar** las excepciones. A continuación explicamos como **definirlas**.

A pesar de que Python define un [conjunto de excepciones por defecto](https://docs.python.org/3/library/exceptions.html "excepciones por defecto de Python"), podrían no ser suficientes para nuestro programa. En ese caso, deberíamos **definir nuestra propia excepción**.

Si queremos crear una excepción, solamente tenemos que crear una clase que herede de la clase `Exception`. Es tan sencillo como el siguiente ejemplo.


```python
# Creamos una excepción personalizada
class MiExcepcionPersonalizada(Exception):
    pass
```

Y ya podríamos lanzarla con `raise` cuando quisiéramos.


```python
raise MiExcepcionPersonalizada()
```


También se pueden pasar parámetros de entrada al lanzarla. Esto es muy útil para dar información adicional a la excepción. En el siguiente ejemplo se pasan dos parámetros. Para ello tenemos que modificar la función `__init__()` de la siguiente manera.


```python
# Creamos nuestra propia excepción heredando
# de la clase Exception
class MiExcepcionPersonalizada(Exception):
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
```

Y una vez hemos creado nuestra excepción, podemos lanzarla con `raise` como ya hemos visto. También es posible acceder a los parámetros pasados como argumentos al lanzar la excepción.


```python
# Lanzamos con raise la excepción que hemos creado
try:
    raise MiExcepcionPersonalizada("ValorPar1", "ValorPar2")
except MiExcepcionPersonalizada as ex:
    p1, p2 = ex.args
    print(type(ex))
    print("parametro1 =", p1)
    print("parametro2 =", p2)

#<class '__main__.MiExcepcionPersonalizada'>
#parametro1 = ValorPar1
#parametro2 = ValorPar2
```

## Ejemplos
Hay un truco muy interesante que nos permite pasar a la excepción un argumento en forma de [diccionario](/diccionarios-en-python/ "diccionario") como se muestra a continuación.
```python
# Se define una excepción
class MiExcepcion(Exception):
    pass

# Se lanza
try:
    raise MiExcepcion({"mensaje":"Mi Mensaje", "informacion":"Mi Informacion"})

# Se captura
except MiExcepcion as e:
    detalles = e.args[0]
    print(detalles)
    print(detalles["mensaje"])
    print(detalles["informacion"])    
    
#{'mensaje': 'Este es el mensaje', 'informacion': 'Esto es la informacion'}
# Mi Mensaje
# Mi Informacion
```

Como se puede ver, los parámetros son accesibles con `[]` ya que se trata de un diccionario.

Una forma un poco más larga de hacer lo mismo sería se la siguiente manera. En este caso los parámetros que se pasan no son accesibles como si fueran un diccionario sino como se de un objeto normal se tratase con `.mensaje` y `.informacion`


```python
class MiExcepcion(Exception):
    def __init__(self, mensaje, informacion):
        self.mensaje = mensaje
        self.informacion = informacion
    
try:
    raise MiExcepcion("Mi Mensaje", "Mi Informacion")
except MiExcepcion as e:
    print(e.mensaje)
    print(e.informacion)
```

Nótese que para los ejemplos hemos usado *mensaje* en *informacion*, pero estas variables pueden ser las que se te ocurran, y por supuesto tampoco tienen porque ser dos, podrían ser mas.