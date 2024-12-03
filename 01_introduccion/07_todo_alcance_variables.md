---
layout: default
title: 📙 Alcance variables
parent: 🕺🏻 01. Introducción
description: El alcance de variables en Python se refiere a la región específica del código donde una variable puede ser accedida o utilizada. Esto depende de dónde y cómo se declara la variable dentro del programa.
order: 8
nav_order: g
permalink: /alcance-variables-python
---

# Alcance variables en Python

Python clasifica los alcances de acuerdo con el modelo `LEGB`, que determina el orden en que se buscan las variables. Las siglas `LEGB` corresponden a:

Local: Variables definidas dentro de una función o bloque, accesibles únicamente dentro de ese contexto. Se crean al inicio de la ejecución de la función y desaparecen cuando esta termina.

```python
def saludo():
    mensaje = "¡Hola, mundo!"  # Variable local
    print(mensaje)

saludo()
print(mensaje)  # Esto generará un error porque 'mensaje' es local a la función.
```
En este caso, la variable `mensaje` se define y utiliza dentro de la función `saludo`. Fuera de esta función, la variable no existe y no se puede acceder.

Enclosing: Se refiere a las variables definidas en una función exterior que encapsula otra función. Estas variables no son locales para la función más interna, pero tampoco son globales.

```python
def funcion_exterior():
    mensaje = "Hola desde la función exterior"  # Variable en el alcance 'enclosing'

    def funcion_interior():
        print(mensaje)  # La función interior accede a la variable de la exterior

    funcion_interior()

funcion_exterior()
```
Salida: `Hola desde la función exterior`

En este caso, mensaje no es ni local para `funcion_interior` ni global, sino que pertenece al alcance de `funcion_exterior`. Este es un ejemplo de una variable con alcance enclosing.

Global: Variables definidas en el nivel superior del script(/ejecutar-script-python) o programa, fuera de cualquier función. Son accesibles en todo el archivo, pero pueden ser modificadas dentro de una función solo si se usa la palabra clave `global`.

```python
mensaje = "Hola desde el alcance global"  # Variable global

def imprimir_mensaje():
    print(mensaje)  # Accediendo a la variable global

imprimir_mensaje()

print(mensaje)  # También accesible fuera de las funciones
```
Salida: `Hola desde el alcance global`
        `Hola desde el alcance global`

En este caso, `mensaje` se define fuera de cualquier función(/funciones-python), por lo que es global y puede ser utilizada tanto dentro como fuera de las funciones(/funciones-python).

Built-in: Variables y funciones predefinidas de Python que están disponibles en cualquier parte del código, como `len()`, `range()` y `print()`.

```python
from math import sqrt  # 'sqrt' es una función built-in del módulo 'math'

numero = 16
raiz_cuadrada = sqrt(numero)  # Usamos la función built-in para calcular la raíz cuadrada
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
```
Salida: `La raíz cuadrada de 16 es 4.0`

En este caso, utilizamos una función(/funciones-python) built-in del módulo estándar `math`, que amplía las funcionalidades predefinidas de Python.

