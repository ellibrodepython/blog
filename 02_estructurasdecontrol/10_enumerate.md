---
layout: default
title: 📙 Enumerate Python
title_nav: 📙 Iterar con enumerate
parent: 🏄🏻‍♀️ 02. Estructuras de control
description: Python nos da herramientas muy útiles para iterar estructuras de datos, como zip y enumerate.
order: 22
nav_order: i
permalink: /enumerate-python
---

# Enumerate en Python

El uso del [for](/for-python) en Python nos permite iterar colecciones, recorriendo todos los elementos de la misma.

```python
lista = ["A", "B", "C"]

for l in lista:
    print(l)

# Salida:
# A
# B
# C
```

Sin embargo, existen situaciones en las que no solo queremos acceder al elemento *i-ésimo* de la colección, sino que **además queremos el índice**. Una forma de hacerlo sería la siguiente.

```python
lista = ["A", "B", "C"]

indice = 0
for l in lista:
    print(indice, l)
    indice += 1

# Salida:
# 0 A
# 1 B
# 2 C
```

Aunque se trata de una forma perfectamente válida, no es demasiado *pythónica*, y es precisamente donde entra en juego el `enumerate()`. Su uso nos permite ahorrar alguna que otra línea de código, obteniendo un resultado mucho más limpio y claro.

```python
lista = ["A", "B", "C"]

for indice, l in enumerate(lista):
    print(indice, l)

# Salida:
# 0 A
# 1 B
# 2 C
```

Por último, es importante notar que su uso no se limita únicamente a bucles `for`. Podemos convertir el tipo `enumerate` en una [lista](/listas-en-python) de [tuplas](/tuplas-python), donde cada una contiene un elemento de la colección inicial y el índice asociado.

```python
lista = ["A", "B", "C"]

en = list(enumerate(lista))
print(en)

# Salida;
# [(0, 'A'), (1, 'B'), (2, 'C')]
```

Por lo tanto recuerda, la próxima vez que quieras acceder a los índices de una colección, piensa si tal vez `enumerate` puede resolver tu problema de manera más clara y con menos código.