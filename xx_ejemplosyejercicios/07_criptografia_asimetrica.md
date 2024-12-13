---
layout: default
title: 📙 Criptografía Asimétrica
description: La criptografía asimétrica o criptografía de clave pública es un sistema criptográfico donde existen dos claves relacionadas matemáticamente, una pública y una privada. Puede ser usada para encriptar información o firmar mensajes.
order: 97
nav_order: e
permalink: /criptografia-asimetrica
nav_exclude: true
---

# Criptografía Asimétrica

La criptografía asimétrica, también conocida como criptografía de clave publica, es un sistema criptográfico donde existen dos claves relacionadas matemáticamente, una pública y otra privada.
La pública se puede derivar de la privada, pero no al revés.
* 🔑 **Clave privada**: Bajo ningún concepto debe ser revelada. Se usa para i) desencriptar la información encriptada con la pública y ii) firmar contenido.
* 🗝️ **Clave pública**: Puede ser compartida con cualquier persona. Se usa para i) encriptar información y ii) verificar un contenido firmado.

La criptografía asimétrica ofrece dos funcionalidades:
* **Encriptado**: Si encriptamos un mensaje con una clave pública 🗝️, dicho mensaje solo podrá ser desencriptado por la clave privada 🔑 correspondiente.
* **Firma digital**: Si queremos verificar el origen o integridad de un mensaje, podemos firmarlo con la clave privada 🔑. Usando la clave pública 🗝️ cualquiera podrá verificar la autenticidad del mismo.

En otras palabras, nos permite tanto ocultar información (encriptado) como verificar que un mensaje ha sido creado por el usuario apropiado (firma digital).

La criptografía asimétrica es un avance con respecto a la criptografía simétrica, donde la clave de encriptado y desencriptado es la misma.
Esto supone un problema, ya que dicha clave simétrica debe ser secreta y solo conocida por emisor y receptor.
Al compartirla, podría ser revelada a usuarios no autorizados, lo que supone un riesgo.
La criptografía asimétrica soluciona esto, ya que la clave usada para encriptar es pública y no necesita ser protegida.

Por otro lado en criptografía simétrica, el número de claves a gestionar es mayor. Supongamos $n$ usuarios que desean comunicarse entre sí.
Con criptografía simétrica necesitaríamos $n(n-1)/2$ claves, ya que necesitamos una clave para cada par de usuarios.
Sin embargo con criptografía asimétrica únicamente $2n$, ya que las claves públicas se pueden reutilizar y un usuario no necesita asignar una diferente a cada resto de usuarios.

Algunas aplicaciones prácticas:
* Blockchain: La firma digital se emplea para garantizar que solo el que posee la clave privada 🔑 puede gastar fondos de una determinada cuenta.
* Correo electrónico: El encriptado permite una comunicación confidencial usando la clave pública 🗝️ del receptor para el encriptado.

A continuación veremos cómo implementar el encriptado y la firma digital usando Python.
Nótese que se trata de un ejemplo didáctico no preparado para producción.

## Encriptación en Python

Encriptar un mensaje con la clave pública permite que sólo el que posea la clave privada equivalente pueda desencriptarlo.
A continuación veremos cómo encriptar un mensaje con criptografía de curva elíptica, usando la conocida curva `secp256k1` en Python.
Para ello utilizaremos la librería `ecies`, que puede ser instalada con:

```python
pip install eciespy
```

Antes de nada debemos generar una `clave_privada` 🔑 y una `clave_publica` 🗝️. Lo podemos hacer de la siguiente manera.
Nótese que una clave privada es simplemente un número aleatorio muy grande con mucha entropía.
Aunque estuvieras años generando claves privadas, nunca encontrarías dos iguales.
Podemos ver también que la `clave_publica` se deriva de la `clave_privada`.

```python
from ecies import encrypt, decrypt
from ecies.utils import generate_eth_key, generate_key

eth_k = generate_eth_key()
clave_privada = eth_k.to_hex()
clave_publica = eth_k.public_key.to_hex()

print(clave_privada)
# 0x1a3d7b9a75cc2967cb2f34f276d35e60d8c72ffe9a902f2b00eb27c1ffab5ce8

print(clave_publica)
# 0x5af46da61431d3b66c3a5f5368c520c5b16ca14776c87fb6a57009befaaa9f73931dd1368a703830af31d4fdafbc23d1809717d991f18d1d2e8b5a525d3eb4a4
```

Ahora imagina que quieres comunicarte con nosotros de manera privada.
Te compartimos nuestra `clave_publica`, y con ella puedes encriptar el mensaje.
Ahora, el `mensage_encriptado` únicamente puede ser desencriptado por la persona que posea la `clave_privada`.
En este caso, nosotros.

```python
mensaje = b'Mensaje secreto para El Libro de Python'
mensage_encriptado = encrypt(clave_publica, mensaje)

print(mensage_encriptado.hex())
# 0454fad22693a4f49648e521d201d026bac7d2752d1079e255d66e12c81db529a2ad01293ca22b1249fdcd9dd0714341b7a2e5ec1961b8ee1d832f41fca8b941855badb6414dec47151f9632630c9ea7b28a195cad70d0fc2527e1870cec178f7f6fd219c01c8d03fd8f2120be3e12293e6d3563237f71bd158d2ed710a0082a50678876bfda3c75
```

Como nosotros somos los únicos que conocemos dicha `clave_privada`, podemos desencriptar el mensaje, obteniendo el mensaje en claro.

```python
mensaje_desencriptado = decrypt(clave_privada, mensage_encriptado)

print(mensaje_desencriptado)
# b'Mensaje secreto para El Libro de Python'
```

Ahora imaginemos que nuestro `mensaje_encriptado` cae en malas manos.
Por suerte esa persona no conoce nuestra `clave_privada` y tiene `otra_clave_privada`.
Si esta persona intenta desencriptar el mensaje, obtendrá una [excepción](https://ellibrodepython.com/excepciones-try-except-finally).
No podrá desencriptar el mensaje, y por lo tanto no podrá ver el contenido del mensaje.

```python
otra_clave_privada = generate_key().to_hex()
mensaje_desencriptado_error = decrypt(otra_clave_privada, mensage_encriptado)

# Error: ValueError: MAC check failed
```

La magia de las matemáticas, y más en concreto, lo difícil que es factorizar números primos, protegen nuestro mensaje.
Teóricamente con capacidad de computación y tiempo infinito, nuestra encriptación podría romperse, pero en la práctica es muy difícil.
Al menos por ahora, mientras los ordenadores cuánticos no sean una realidad.

## Firma Digital en Python

A continuación veremos cómo crear una firma digital usando Python.
Para ello firmamos un mensaje con nuestra clave privada, lo que permite que cualquiera pueda verificar que nosotros hemos creado dicho mensaje, haciendo uso de nuestra clave pública.
Usaremos la librería `cryptography`:

```python
pip install cryptography
```

Antes de nada necesitamos crear una `clave_privada` 🔑 y derivar de ella la `clave_publica` 🗝️.
Similar al ejemplo anterior, pero en este caso usamos otra librería.

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

# generamos una clave privada y derivamos la pública
clave_privada = ec.generate_private_key(ec.SECP256R1())
clave_publica = clave_privada.public_key()
```

Si tienes curiosidad de ver que pinta tiene la clave privada, la puedes imprimir de la siguiente manera.
Existen diferentes formatos para representarla.
Y recuerda, si la usas en casos reales, jamás la compartas con nadie.

```python
from cryptography.hazmat.primitives import serialization

pem = clave_privada.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print(pem)
```

Ahora viene lo importante. Usando `sign`, podemos crear nuestra firma digital.
Como podemos ver, únicamente necesitamos nuestra clave privada y el mensaje a firmar.
El `SHA256` es simplemente la función [hash](https://ellibrodepython.com/hash-python) utilizada para "resumir" nuestro mensaje.
Es decir, lo que realmente se firma no es el mensaje entero, sino el hash del mismo, en este caso el `SHA256` del mensaje.
Esto es más eficiente, ya que el hash tiene un tamaño fijo y posiblemente menor que el mensaje.
Y la gran ventaja es que este hash, representa de manera unívoca a el mensaje.

```python
firma = clave_privada.sign(
    b"Envía 1 € a la dirección 0x1234",
    ec.ECDSA(hashes.SHA256())
)

print(firma.hex())
# 304502205abea2fb8d3be8a8b9caddd175ebd67edb38fbae051c618134eb5b529e17af1e022100a75540b213806e3d831f785246c7caf0ad171ff220fda356aa248e54583b1d93
```

Una vez tenemos la firma, podemos enviársela a cualquier persona junto con el mensaje.
Por ejemplo, esta firma y mensaje podrían ser una transacción en la blockchain.
Esta actúa como una firma manuscrita, donde se garantiza que el creador conocía la `clave_privada`.

Ahora, un tercero podría verificar que el mensaje fue efectivamente creado por el conocedor de `clave_privada`.
Para esto sólo se necesita `clave_publica`. Una clave pública que cualquiera puede conocer.

```python
clave_publica.verify(
        firma,
        b"Envia 1 euro a la direccion 0x1234",
        ec.ECDSA(hashes.SHA256())
)
```

Imaginemos que alguien ha interceptado la comunicación y ha alterado el mensaje, cambiando la dirección.
En vez de solicitar 1 euro a `0x1234` se solicita a `0x5678`.
Si esto fuera una aplicación real, alguien podría engañar al receptor y hacerle enviar fondos a una dirección distinta.

Sin embargo, si intentamos verificar la firma con `verify` podemos ver obtendremos una excepción `InvalidSignature`.
Es decir, la firma no es válida, ya que el mensaje se ha visto alterado.
Nos hemos protegido de un atacante modificando el mensaje.

```python
clave_publica.verify(
        firma,
        b"Envia 1 euro a la direccion 0x5678",
        ec.ECDSA(hashes.SHA256())
)
# Error: cryptography.exceptions.InvalidSignature
```

No olvides capturar la excepción como explicamos [aquí](https://ellibrodepython.com/excepciones-try-except-finally).
Es importante notar lo mismo pasa si la firma se cambia o si la clave pública que estamos usando no corresponde con la privada que creó la firma original.
La firma digital asegura la integridad del mensaje.


