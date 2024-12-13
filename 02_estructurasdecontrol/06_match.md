---
layout: default
title: 📙 Match en Python
title_nav: 📙 Match
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: El match en Python se introdujo en la version 3.10. Es similar al switch pero mucho mas potente.
order: 18
nav_order: f
permalink: /match-python
---

## Match en Python

Python ofrece algo similar al *switch* de otros lenguajes de programación desde la versión `3.10`.

Se trata del `match`. Cada `case` define un camino posible. El `_` es la opción por defecto, que se ejecuta si la entrada no coincide con ningún caso.

```python
hora = 8
match hora:
    case 8:
        print("Desayuno")
    case 14:
        print("Comida")
    case 21:
        print("Cena")
    case _:
        print("No toca comer")
# Desayuno
```

El `match` nos permite realizar lo mismo que con múltiples `if/elif` como hemos visto anteriormente. Ambos códigos son equivalentes.

```python
if hora == 8:
    print("Desayuno")
elif hora == 14:
    print("Comida")
elif hora == 21:
    print("Cena")
else:
    print("No toca comer")
```

También podemos tener en nuestros `case` múltiples condiciones, donde `|` es interpretado como un `or`.

```python
mes = 4
match mes:
    case 12 | 1 | 2: print("Invierno")
    case 3 | 4 | 5: print("Primavera")
    case 6 | 7 | 8: print("Verano")
    case 9 | 10 | 11: print("Otoño")
    case _: print("Error")
# Primavera
```

Aunque no acaba ahí la cosa. Podemos hacer *matching* de prácticamente cualquier cosa como una tupla.

```python
coordenada = (0, 1)
match coordenada:
    case (0, 0):
        print("Coordenada en origen")
    case (x, 0):
        print(f"Coordenada en eje x: {x}")
    case (0, y):
        print(f"Coordenada en eje y: {y}")
    case (x, y):
        print(f"Coordenada en: {x}, {y}")
    case _:
        print("Error")

# Coordenada en eje y: 1
```