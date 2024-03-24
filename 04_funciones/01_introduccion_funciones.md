---
layout: default
title: 📗 Funciones en Python
parent: 🕹 04. Funciones
description: Las funciones en Python al igual que en otros lenguajes de programación, permiten ejecutar cierto código sobre unas variables de entrada para proporcionar una salida. Son muy importantes ya que proporcionan modularidad y reusabilidad a nuestro código.
order: 40
nav_order: a
permalink: /funciones-en-python
---

# Funciones en Python

Anteriormente hemos usado funciones nativas que vienen con Python como `len()` para calcular la longitud de una lista, pero al igual que en otros lenguajes de programación, también podemos definir **nuestras propias funciones**. Para ello hacemos uso de `def`.


```python
def nombre_funcion(argumentos):
    código
    return retorno
```

Cualquier función tendrá un **nombre**, unos **argumentos de entrada**, un **código** a ejecutar y unos **parámetros de salida**. Al igual que las funciones matemáticas, en programación nos permiten realizar diferentes operaciones con la entrada, para entregar una determinada salida que dependerá del código que escribamos dentro. Por lo tanto, es totalmente análogo al clásico `y=f(x)` de las matemáticas.


```python
def f(x):
    return 2*x
y = f(3)
print(y) # 6
```


Algo que diferencia en cierto modo las funciones en el mundo de la programación, es que no sólo realizan una operación con sus entradas, sino que también parten de los siguientes principios:
* El principio de **reusabilidad**, que nos dice que si por ejemplo tenemos un fragmento de código usado en muchos sitios, la mejor solución sería pasarlo a una función. Esto nos evitaría tener código repetido, y que modificarlo fuera más fácil, ya que bastaría con cambiar la función una vez.
* Y el principio de **modularidad**, que defiende que en vez de escribir largos trozos de código, es mejor crear módulos o funciones que agrupen ciertos fragmentos de código en funcionalidades específicas, haciendo que el código resultante sea más fácil de leer.

## Pasando argumentos de entrada

Empecemos por la función más sencilla de todas. Una función sin parámetros de entrada ni parámetros de salida.


```python
def di_hola():
    print("Hola")
```

Hemos declarado o definido la función. El siguiente paso es llamarla con `di_hola()`. Si lo realizamos veremos que se imprime Hola.


```python
di_hola() # Hola
```



Vamos a complicar un poco las cosas pasando un argumento de entrada. Ahora si pasamos como entrada un nombre, se imprimirá Hola y el nombre.


```python
def di_hola(nombre):
    print("Hola", nombre)
di_hola("Juan")
# Hola Juan
```



Python permite pasar argumentos también de otras formas. A continuación las explicamos todas.

### Argumentos por posición

Los argumentos por posición o **posicionales** son la forma más básica e intuitiva de pasar parámetros. Si tenemos una función `resta()` que acepta dos parámetros, se puede llamar como se muestra a continuación.


```python
def resta(a, b):
    return a-b
resta(5, 3) # 2
```




Al tratarse de parámetros posicionales, se interpretará que el primer número es la `a` y el segundo la `b`. El número de parámetros es fijo, por lo que si intentamos llamar a la función con solo uno, dará error.


```python
#resta(1) # Error! TypeError
```

Tampoco es posible usar mas argumentos de los tiene la función definidos, ya que no sabría que hacer con ellos. Por lo tanto si lo intentamos, Python nos dirá que toma 2 posicionales y estamos pasando 3, lo que no es posible.


```python
#TypeError: resta() takes 2 positional arguments but 3 were given
#resta(5,4,3) # Error
```

### Argumentos por nombre

Otra forma de llamar a una función, es usando el nombre del argumento con `=` y su valor. El siguiente código hace lo mismo que el código anterior, con la diferencia de que los argumentos no son posicionales.


```python
resta(a=3, b=5) # -2
```



Al indicar en la llamada a la función el nombre de la variable y el valor, el orden ya no importa, y se podría llamar de la siguiente forma.


```python
resta(b=5, a=3) # -2
```



Como es de esperar, si indicamos un argumento que no ha sido definido como parámetro de entrada, tendremos un error.


```python
#resta() got an unexpected keyword argument 'c'
#resta(b=5, c=3) # Error!
```

### Argumentos por defecto

Tal vez queramos tener una función con algún parámetro opcional, que pueda ser usado o no dependiendo de diferentes circunstancias. Para ello, lo que podemos hacer es asignar un valor **por defecto** a la función. En el siguiente caso `c` valdría cero salvo que se indique lo contrario.


```python
def suma(a, b, c=0):
    return a+b+c
suma(5,5,3) # 13
```



Dado que el parámetro `c` tiene un valor por defecto, la función puede ser llamada sin ese valor.


```python
suma(4,3) # 7
```



Podemos incluso asignar un valor por defecto a todos los parámetros, por lo que se podría llamar a la función sin ningún argumento de entrada.


```python
def suma(a=3, b=5, c=0):
    return a+b+c
suma() # 8
```


Las siguientes llamadas a la función también son válidas


```python
suma(1)     # 6
suma(4,5)   # 9
suma(5,3,2) # 10
```


O haciendo uso de lo que hemos visto antes y usando los nombres de los argumentos.


```python
suma(a=5, b=3) #8
```


## Argumentos de longitud variable

En el ejemplo con argumentos por defecto, hemos visto que la función puede ser llamada con diferente número de argumentos de entrada, pero esto no es realmente una función con argumentos de longitud variable, ya que existe un número máximo.

Imaginemos que queremos una función `suma()` como la de antes, pero en este caso necesitamos que sume todos los números de entrada que se le pasen, sin importar si son 3 o 100. Una primera forma de hacerlo sería con una lista.


```python
def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
suma([1,3,5,4]) # 13
```


La forma es válida y cumple nuestro requisito, pero realmente no estamos trabajando con argumentos de longitud variable. En realidad tenemos un solo argumento que es una lista de números.

Por suerte, Python tiene una herramienta muy potente. Si declaramos un argumento con `*`, esto hará que el argumento que se pase sea empaquetado en una tupla de manera automática. No confundir `*` con los punteros en otros lenguajes de programación, no tiene nada que ver.


```python
def suma(*numeros):
    print(type(numeros))
    # <class 'tuple'>
    total = 0
    for n in numeros:
        total += n
    return total
suma(1, 3, 5, 4) # 13
```




El resultado es igual que el anterior, y podemos ver como efectivamente `numeros` es de la clase `tuple`. También podemos hacer otras llamadas con diferente número de argumentos


```python
suma(6) # 6
suma(6, 4, 10) # 20
suma(6, 4, 10, 20, 4, 6, 7) # 57
```



Usando doble `**` es posible también tener como parámetro de entrada una lista de elementos almacenados en forma de clave y valor. En este caso podemos iterar los valores haciendo uso de `items()`.


```python
def suma(**kwargs):
    suma = 0;
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma

suma(a=5, b=20, c=23) # 48
```



De igual manera, podemos pasar un diccionario como parámetro de entrada.


```python
def suma(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma
di = {'a': 10, 'b':20}
suma(**di) # 30
```




## Sentencia return

El uso de la sentencia `return` permite realizar dos cosas:
* Salir de la función y transferir la ejecución de vuelta a donde se realizó la llamada.
* Devolver uno o varios parámetros, fruto de la ejecución de la función.

En lo relativo a lo primero, una vez se llama a `return` se para la ejecución de la función y se vuelve o retorna al punto donde fue llamada. Es por ello por lo que el código que va después del `return` no es ejecutado en el siguiente ejemplo.


```python
def mi_funcion():
    print("Entra en mi_funcion")
    return
    print("No llega")
mi_funcion() # Entra en mi_funcion
```


Por ello, sólo llamamos a `return` una vez hemos acabado de hacer lo que teníamos que hacer en la función.

Por otro lado, se pueden **devolver parámetros**. Normalmente las funciones son llamadas para realizar unos cálculos en base a una entrada, por lo que es interesante poder devolver ese resultado a quien llamó a la función.


```python
def di_hola():
    return "Hola"
di_hola()
# 'Hola'
```



También es posible devolver mas de una variable, separadas por `,`. En el siguiente ejemplo tenemos una función que calcula la suma y media de tres números, y devuelve su resultado.


```python
def suma_y_media(a, b, c):
    suma = a+b+c
    media = suma/3
    return suma, media
suma, media = suma_y_media(9, 6, 3)
print(suma)  # 18
print(media) # 6.0
```


## Documentación

Ahora que ya tenemos nuestras propias funciones creadas, tal vez alguien se interese en ellas y podamos compartírselas. Las funciones pueden ser muy complejas, y leer código ajeno no es tarea fácil. Es por ello por lo que es importante **documentar** las funciones. Es decir, añadir comentarios para indicar como deben ser usadas.


```python
def mi_funcion_suma(a, b):
    """
    Descripción de la función. Como debe ser usada,
    que parámetros acepta y que devuelve
    """
    return a+b
```

Para ello debemos usar la triple comilla `"""` al principio de la función. Se trata de una especie de comentario que podemos usar para indicar como la función debe ser usada. No se trata de código, es un simple comentario un tanto especial, conocido como `docstring`.

Ahora cualquier persona que tenga nuestra función, podrá llamar a la función `help()` y obtener la ayuda de como debe ser usada.


```python
help(mi_funcion_suma)
```



Otra forma de acceder a la documentación es la siguiente.


```python
print(mi_funcion_suma.__doc__)
```



<p class="alert alert-info">
<b>Para saber más:</b> Las descripciones de las funciones suelen ser un poco mas detalladas de lo que hemos mostrado. En <a href="https://www.python.org/dev/peps/pep-0257/"> la PEP257</a> se define en detalle como debería ser.
</p>

## Anotaciones en funciones

Existe una funcionalidad relativamente reciente en Python llamada **function annotation** o anotaciones en funciones. Dicha funcionalidad nos permite añadir metadatos a las funciones, indicando los tipos esperados tanto de entrada como de salida.


```python
def multiplica_por_3(numero: int) -> int:
    return numero*3

multiplica_por_3(6) # 18
```




Las anotaciones son muy útiles de cara a la documentación del código, pero no imponen ninguna norma sobre los tipos. Esto significa que se puede llamar a la función con un parámetro que no sea `int`, y no obtendremos ningún error.


```python
multiplica_por_3("Cadena")
# 'CadenaCadenaCadena'
```