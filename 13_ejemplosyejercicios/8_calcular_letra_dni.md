---
layout: default
title: 📙 Calcular letra DNI
parent: 🔬 13. Ejemplos y ejercicios
description: Calcular la letra del DNI se puede hacer obteniendo el módulo 23 del DNI.
order: 98
nav_order: f
permalink: /calcular-letra-dni
---

# Letra DNI

<div>
    <label for="dni">Introduce DNI:</label>
    <input type="text" id="dni" maxlength="8" placeholder="12345678">
    <button type="button" onclick="calcularLetra()">Calcular Letra</button>
    <p id="resultado"></p>
</div>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        window.calcularLetra = function() {
            const letras = "TRWAGMYFPDXBNJZSQVHLCKE";
            const numeroDni = document.getElementById("dni").value;

            if (!/^\d{8}$/.test(numeroDni)) {
                document.getElementById("resultado").innerText = "Error: Introduce un número de 8 dígitos.";
                return;
            }

            const resto = numeroDni % 23;
            const letra = letras[resto];
            document.getElementById("resultado").innerText = `${numeroDni}${letra}`;
        };
    });
</script>

# Calcular letra DNI en Python

En España todo Documento Nacional de Identidad (DNI) está compuesto por 8 dígitos y una letra al final.
Esta letra actúa a modo de *checksum*. Es decir, la letra se calcula a partir de los dígitos del DNI.

Podemos escribir una función en Python que dado un DNI nos devuelva el DNI con la letra de la siguiente manera.

```python
def letra_dni(dni):
    if len(str(dni)) != 8:
        raise Exception("El DNI debe tener 8 dígitos")
    LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return f"{dni}{LETRAS_DNI[int(dni) % 23]}"

print(letra_dni('00000000'))
# 00000000T
```

Como puedes ver:
* Se comprueba que el DNI tiene 8 dígitos.
* La letra se calcula usando el módulo 23 del DNI.
* Se elige la letra de la secuencia.
* Si el resultado es 0, se toma la `T`, si es 1 la `R`, etc.
