---
layout: default
title: 📙 List comprehensions
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: Las list comprehension o comprensión de listas son una herramienta de Python que nos permite modificar colecciones iterables en una sola línea de código. Al igual que existen para las listas, también pueden ser usadas sobre otros tipos como sets o diccionarios.
order: 23
nav_order: k
permalink: /list-comprehension-python
---

# List comprehensions

Una de las principales ventajas de Python es que una misma funcionalidad puede ser escrita de maneras muy diferentes, ya que su sintaxis es muy rica en lo que se conoce como expresiones idiomáticas o *idiomatic expressions*. Las **list comprehension** o comprensión de listas son una de ellas.

Vayamos al grano, las *list comprehension* nos permiten crear listas de elementos en una sola línea de código. Por ejemplo, podemos crear una lista con los cuadrados de los primeros 5 números de la siguiente forma


```python
cuadrados = [i**2 for i in range(5)]
#[0, 1, 4, 9, 16]
```

De no existir, podríamos hacer lo mismo de la siguiente forma, pero necesitamos alguna que otra línea más de código.


```python
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
#[0, 1, 4, 9, 16]
```

El resultado es el mismo, pero resulta menos claro. Antes de continuar, veamos la sintaxis general de las comprensiones de listas.


```python
# lista = [expresión for elemento in iterable]
```

Es decir, por un lado tenemos el `for elemento in iterable`, que itera un determinado iterable y "almacena" cada uno de los elementos en `elemento` [como vimos en este otro post sobre el for](/for-python/). Por otro lado, tenemos la `expresión`, que es lo que será añadido a la lista en cada iteración.

La expresión puede ser una operación como hemos visto anteriormente `i**2`, pero también puede ser un valor constante. El siguiente ejemplo genera una lista de cinco unos.


```python
unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]
```

La expresión también puede ser una llamada a una función. Se podría escribir el ejemplo anterior del cálculo de cuadrados de la siguiente manera.


```python
def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]
#[0, 1, 4, 9, 16]
```

Como puedes observar, las posibilidades son bastante amplias. Cualquier elemento que sea iterable puede ser usado con las *list comprehensions*. Anteriormente hemos iterado `range()` pero podemos hacer lo mismo para una lista. En el siguiente ejemplo vemos como dividir todos los números de una lista entre 10.


```python
lista = [10, 20, 30, 40 , 50]
nueva_lista = [i/10 for i in lista]
#[1.0, 2.0, 3.0, 4.0, 5.0]
```

## Añadiendo condicionales

En el apartado anterior hemos visto como modificar todos los elementos de un iterable (como una lista) de diferentes maneras. La primera elevando cada elemento al cuadrado, y la segunda dividiendo cada elemento por diez.

Pero, ¿y si quisiéramos realizar la operación sobre el elemento sólo si una determinada condición se cumple? Pues tenemos buenas noticias, porque es posible añadir un condicional `if`. La expresión genérica sería la siguiente.


```python
# lista = [expresión for elemento in iterable if condición]
```

Por lo tanto la `expresión` sólo se aplicará al `elemento` si se cumple la `condición`. Veamos un ejemplo con una frase, de la que queremos saber el número de erres que tiene.


```python
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']
```

Lo que hace el código anterior es iterar cada letra de la frase, y si es una `r`, se añade a la lista. De esta manera el resultado es una lista con tantas letras `r` como la frase original tiene, y podemos calcular las veces que se repite con `len()`.


```python
print(len(erres))
#4
```


## Sets comprehension

Las *set comprehensions* son muy similares a las listas que hemos visto con anterioridad. La única diferencia es que debemos cambiar el `()` por `{}`. Como resulta evidente, dado que los [set](/sets-python/) no permiten duplicados, si intentamos añadir un elemento que ya existe en el set, simplemente no se añadirá.


```python
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}
#{'r'}
```

## Dictionary comprehension

Y por último, también tenemos las comprensiones de [diccionarios](/diccionarios-en-python/). Son muy similares a las anteriores, con la única diferencia que debemos especificar la `key` o llave. Veamos un ejemplo.


```python
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}
```


Como se puede ver, usando `:` asignamos un valor a una llave. Hemos usado también `zip()`, que nos permite iterar dos listas paralelamente. Por lo tanto, en este ejemplo estamos convirtiendo dos listas a un diccionario.

## Conclusiones

Las comprensiones de listas, sets o diccionarios son una herramienta muy útil para hacer que nuestro código resulte más compacto y fácil de leer. Siempre que tengamos una colección iterable que queramos modificar, son una buena opción para evitar tener que escribir bucles for.

Las comprensiones están también muy relacionadas con el concepto de programación funcional y otra funciones que Python nos ofrece como `filter` o `map`, por lo que si no las conoces te recomendamos que leas sobre ellas.

En ciertas ocasiones, las comprensiones no resultan sólo útiles por que puedan ser escritas en una sola línea de código, sino que también pueden llegar a ser más rápidas que otros métodos. Es muy importante por lo tanto medir su tiempo de ejecución para saber si son una buena elección.

Y por último, aunque su uso resulte de lo más Pythónico y elegante (algo que a muchos programadores de Python les encanta), hay que tener cuidado con su uso y no abusar de ellas. Resulta fácil caer en la tentación de acabar escribiendo comprensiones que son tan largas que prácticamente son imposibles de leer, algo que puede no ser muy buena idea.
