---
layout: default
title: 📙 Ejecutando scripts
parent: 🕺🏻 01. Introducción
description: Ejecutar script Python
order: 9
nav_order: h
permalink: /ejecutar-script-python
---

# Ejecutar Script en Python

Ejecutar un script en Python es sencillo y se puede hacer de varias maneras, Generalmente los entornos de desarrollo tienen un boton **▷** de color verde, sin embargo puede ser diferente dependiendo de tu entorno. Aquí tienes las opciones más comunes:

### Desde la terminal o linea de comandos
* Ubica el script: Asegúrate de estar en el directorio donde se encuentra el archivo `.py`.
* Para **ejecutar el script** escribe el siguiente comando:
  
```shell
python nombre_del_script.py
```

### Desde un Entorno de Desarrollo Integrado:
* PyCharm: Abre tu proyecto, selecciona el archivo y haz clic en el botón de **Play** o ejecuta con **Shift + F10**.
* Visual Studio Code: Abre el archivo y presiona **F5** para ejecutar.
* Thonny: Haz clic en el botón **Ejecutar** o presiona **F5**.

### Desde el interprete interactivo de python
* Abre tu Python en tu terminal
  
```shell
python
```

* Importa y ejecuta tu `script` usando:

```shell
import nombre_del_script
```
Esto ejecutara el contenido del `script` una vez.

### Con un Doble Clic en el Archivo (Windows):
Si el archivo tiene extensión `.py` y está asociado con **Python**, al hacer doble clic se ejecutará. Sin embargo, si el script requiere interacción, la ventana se cerrará rápidamente. Usa la terminal para evitar esto.

## Argumentos script
Los argumentos de **script** en Python son valores que puedes pasar a tu programa cuando lo ejecutas desde la terminal o línea de comandos. Esto permite que el **script** sea más flexible y reciba datos externos al momento de su ejecución.

### Como funcionan los argumentos de script
Acceso a los argumentos de script
* En Python, los argumentos se acceden mediante el módulo `sys`, específicamente la lista `sys.argv`.
* ```python
  import sys #Importando el modulo sys
  ```

### Contenido de sys.argv
`sys.argv` es una lista de cadenas donde
  * El primer elemento `(sys.argv[0])` es el nombre del archivo del script.
  * Los siguientes elementos `(sys.argv[1:])` son los argumentos proporcionados.

Por ejemplo:
Script: `my_script.py
```python
import sys #Importando el modulo sys

# Accediendo a los argumentos
print(f"Nombre del script: {sys.argv[0]}")
if len(sys.argv) > 1:
    print("Argumentos proporcionados:", sys.argv[1:])
else:
    print("No se proporcionaron argumentos.")
```

**Ejecucion en terminal:**
```shell
python mi_script.py hola mundo
```

**Salida:**
```shell
Salida: Nombre del script: mi_script.py
        Argumentos proporcionados: ['hola', 'mundo']
```

## Manejo avanzado con argparse
Para scripts más complejos, el módulo `argparse` permite manejar argumentos con mayor flexibilidad y claridad.

Por ejemplo:
script: `mi_script_avanzado.py`
```python
import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Ejemplo de argumentos")

# Agregar argumentos
parser.add_argument("nombre", help="Tu nombre")
parser.add_argument("--edad", type=int, help="Tu edad", required=False)

# Parsear los argumentos
args = parser.parse_args()

print(f"Hola, {args.nombre}!")
if args.edad:
    print(f"Tienes {args.edad} años.")
```

**Ejecucion en terminal:**
```shell
python mi_script_avanzado.py Juan --edad 18
```

**Salida:**
```shell
Hola, Juan!
Tienes 18 años.
```

## Ventajas de usar argumentos de script
  * Permiten personalizar la ejecución del programa.
  * Ayudan a evitar modificar el código directamente.
  * Facilitan el uso del script en diferentes escenarios.
