---
layout: default
title: 📙 Switch en Python
title_nav: 📙 Switch
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: El switch es una herramienta similar al if combinado con varios elif, que apesar de existir en varios lenguajes de programación, no existe en Python. Te damos un truco para emularlo.
order: 18
nav_order: e
permalink: /switch-python
---

# Switch en Python

El switch es una herramienta que nos permite ejecutar diferentes secciones de código dependiendo de una condición. Su funcionalidad es similar a usar varios [if](/if-python), pero por desgracia **Python no tiene un switch** propiamente dicho. Sin embargo, hay formas de simular su comportamiento que te explicamos a continuación.

## Introducción al switch

Ya sabemos que el uso del [if](/if-python) junto con `else` y `elif` nos permite ejecutar un código determinado dependiendo de una `condicion`, como podemos ver en el siguiente código.

```python
if condicion == 1:
    print("Haz a")
elif condicion == 2:
    print("Haz b")
elif condicion == 3:
    print("Haz c")
else:
    print("Haz d")
```

La misma funcionalidad se podría escribir de la siguiente manera haciendo uso del `switch`. Como puedes ver su uso tal vez resulte algo más limpio, y de hecho en determinadas ocasiones es más rápido.

```javascript
// Ojo, esto no es Python
switch(condicion) {
  case 1:
    // haz a
    break;
  case 2:
    // haz b
    break;
  case 3:
    // haz c
    break;
  default:
    // haz x
}
```

Pero tenemos un pequeño problema. **En Python no existe el switch**, por lo que si intentas ejecutar el código anterior, tendrás un error.

Uno tal vez podría decir: bueno, que más da, uso if/elif/else y ya esta. La verdad que en la mayoría de los casos, sería indiferente usar `if` o `switch`, pero si analizamos el comportamiento que existe por debajo, funcionan de manera distinta. A pesar de que en Python no existe, te damos un truco que puede en cierto modo emular su funcionamiento.

## Diferencia if y switch

Una de las principales diferencias, es que usando `if` con `elif`, no todos los bloques tienen el mismo tiempo de acceso. Todas las condiciones van siendo evaluadas hasta que se cumple y se sale. Imaginemos que tenemos 100 condiciones. 

```python
if condicion == 1:
    print("1")
elif condicion == 2:
    print("2")

# ... hasta 100
elif condicion == 100:
    print("3")

else:
    print("x")
```

El tiempo de ejecución será distinto si la `condicion` es 1 o es 70 por ejemplo:

* Si es 1: Se evalúa el primer `if`, y como se cumple la condición se ejecuta y se sale.
* Si es 70: Se va evaluando cada condición, hasta llegar al 70. Es decir, tienen que evaluarse 70 condiciones.

Sin embargo, en el [switch](/switch-pyton) todos los elementos tienen el mismo tiempo de acceso. Esto se debe a que por debajo esta normalmente implementado con *lookup tables*.

Si trabajamos con un gran número de condiciones, el uso del [switch](/switch) sobre el [if](/if-python) podría notarse.

Dado que en Python no tenemos esta herramienta, te explicamos un truco para simularlo. No obstante, si realmente te preocupan estas micro optimizaciones, tal vez no deberías usar Python.

## Emulando switch en Python

Una forma de tener una especie de [switch](/switch-python) en Python es haciendo uso de un [diccionario](diccionario-python). Por lo tanto podríamos convertir el siguiente código.

```python
def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None
```

En el siguiente:

```python
def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)
```

Es importante notar que `opera2` necesita de `()` para realizar la llamada a la función, ya que lo que se devuelve en realidad es una función [lambda](/lambda-python).

```python
opera1('suma', 5, 9)
# Salida: 14

opera2('suma', 5, 9)()
# Salida: 14
```

## Tiempo Ejecución switch vs if

Como hemos indicado anteriormente, usar `switch` en vez de `if` puede ser más rápido. Aunque Python no nos ofrece un `switch` propiamente dicho, lo podemos implementar con [diccionarios](/diccionarios-en-python). A continuación veremos varios experimentos donde analizaremos el tiempo de ejecución de dos opciones distintas.

Empecemos con un problema a resolver. Imaginemos que queremos convertir números de decimal a binario. Aunque esta **no es la forma correcta de hacerlo**, usaremos este ejemplo con fines didácticos. Empecemos por definir las dos formas de hacerlo.

**La primera forma** es usando `if` y `elif`.

```python
def usa_if(decimal):
    if decimal == '0':
        return "000"
    elif decimal == '1':
        return "001"
    elif decimal == '2':
        return "010"
    elif decimal == '3':
        return "011"
    elif decimal == '4':
        return "100"
    elif decimal == '5':
        return "101"
    elif decimal == '6':
        return "110"
    elif decimal == '7':
        return "111"
    else:
        return "NA"
```

**La segunda forma** es usando diccionarios simulando un `switch`.

```python
tabla_switch = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
    }
def usa_switch(decimal):
    return tabla_switch.get(decimal, "NA")
```

Ambas funciones `usa_if` y `usa_switch` realizan lo mismo, pero están implementadas de manera distinta. A continuación mediremos el [tiempo de ejecución](/tiempo-ejecucion-python) de ambas para saber cuál es más rápida. Vamos a crear primero un [decorador](/decoradores-python) que nos permita medir el tiempo que una [función](/funciones-en-python) tarda en ejecutarse.

```python
import time
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(f"Entrada: {args[1]}. Tiempo: {time.time() - inicio}")
        return c
    return funcion_medida
```

Y ahora vamos a crear una función que llame miles de veces a otra. Esto es debido a que necesitamos realizar varias llamadas a la función para obtener un resultado fiable. Dado que si midiéramos una sola ejecución de un `if`, a penas tardaríamos unos microsegundos.

```python
@mide_tiempo
def repite_funcion(funcion, entrada):
    return [funcion(entrada) for i in range(10000000)]
```

Ahora que ya tenemos todo lo que necesitamos para el experimento, vamos a llamar a nuestra funciones con diferentes parámetros. Estos son los resultados:

```python
for i in range(8):
    repite_funcion(usa_if, str(i))

for i in range(8):
    repite_funcion(usa_switch, str(i))

# Usando if:
# Entrada: 0. Tiempo: 2.167248249053955
# Entrada: 1. Tiempo: 2.4989960193634033
# Entrada: 2. Tiempo: 2.898904800415039
# Entrada: 3. Tiempo: 3.0172407627105713
# Entrada: 4. Tiempo: 3.7285051345825195
# Entrada: 5. Tiempo: 3.828972101211548
# Entrada: 6. Tiempo: 4.256570100784302
# Entrada: 7. Tiempo: 4.421134948730469

# Usando switch:
# Entrada: 0. Tiempo: 2.640446186065674
# Entrada: 1. Tiempo: 2.765054941177368
# Entrada: 2. Tiempo: 2.6275320053100586
# Entrada: 3. Tiempo: 2.561228036880493
# Entrada: 4. Tiempo: 2.5796279907226562
# Entrada: 5. Tiempo: 2.5939972400665283
# Entrada: 6. Tiempo: 2.5642037391662598
# Entrada: 7. Tiempo: 2.54691219329834
```

Por lo tanto, podemos concluir lo siguiente:
* Usando if el tiempo de ejecución no es siempre el mismo, ya que dependiendo del valor (0-7) tendrán que evaluarse hasta 8 condiciones.
* Usando switch obtenemos un tiempo ligeramente mayor para el `"0"`, pero el tiempo de ejecución apenas varía cuando cambiamos la entrada.

Visto esto, no se puede concluir que una forma sea mejor que otra, todo dependerá del problema que necesites resolver, pero la próxima vez que te enfrentes a un problema similar, ya tendrás las herramientas para tomar una decisión razonada al respecto.