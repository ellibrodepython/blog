---
layout: default
title: 📙 moviepy, edición de vídeo
parent: 🚜 14. Usando paquetes externos
description: Edita, corta y pega vídeos usando Python y la libería moviepy
order: 98
nav_order: a
permalink: /moviepy-python
---

# moviepy: Editar vídeo con Python

Seguramente alguna vez habrás editado un vídeo usando una aplicación como Vegas, After Effects o Premiere, pero ¿y si te digo que también se puede editar vídeo con Python?. La librería moviepy nos permite cortar, unir, rotar y mucho más. Se trata de un paquete open source para Python, y que por supuesto es compatible con Linux, macOS y Windows. A continuación te enseñamos sus posibilidades.

Lo primero de todo, deberás instalar el paquete. Si ya tienes pip instalado, llama el siguiente comando en el terminal.

```python
pip install moviepy
```

Vale, ya tenemos el paquete instalado, empecemos a usarlo. La mayoría de funcionalidades de moviepy, giran en torno a la clase VideoFileClip y AudioFileClip. La primera permite trabajar con vídeo y la segunda con audio.

Importa el paquete

```python
from moviepy.editor import *
```

Abre un video que tengas

```python
video = VideoFileClip("video_ejemplo.mp4")
```

Una vez hemos abierto el vídeo, ya lo tenemos en video almacenado y podemos empezar a hacer cosas con el. A continuación te enseñamos.

## Rotar vídeo

Si llamamos al método rotate() y le pasamos un número como entrada con los grados que queremos rotar el vídeo, nos devolverá un VideoFileClip rotado. Si queremos guardar el vídeo tan solo hay que llamar a write_videofile() y decirle el nombre que queremos.

```python
from moviepy.editor import *
video = VideoFileClip("video_ejemplo.mp4").rotate(180)
video.write_videofile("rotado.mp4")
```

## Acelerar

Podemos también acelerar o ralentizar el vídeo haciendo uso de los efectos fx. Te dejamos el siguiente código para que pruebes, donde 2 indica que queremos el vídeo dos vez más rápido. Valores menores a uno significará más lento.

```python
from moviepy.editor import *
video = VideoFileClip("video_ejemplo.mp4").fx(vfx.speedx, 2)
video.write_videofile("rapido.mp4")
```

## Cortar vídeo

Otra funcionalidad muy útil es cortar el vídeo, haciendo uso de subclip(). Acepta dos parámetros, el inicio y final en segundos. Por lo tanto (1, 2) nos devolverá un vídeo que dura un segundo desde el segundo uno.

```python
from moviepy.editor import *
video = VideoFileClip("video_ejemplo.mp4")
cortado = video.subclip(1, 2)
cortado.write_videofile("cortado.mp4")
```

## Cambiar formato

Se pueden realizar ciertos cambios de formato. Por ejemplo, si tenemos el vídeo en mp4, podemos pasarlo a webm simplemente guardándolo y cambiando la extensión.

```python
from moviepy.editor import *
video = VideoFileClip("video_ejemplo.mp4")
video.write_videofile("otro_formato.webm")
```

## Unir vídeos

Una de las herramientas más potentes de moviepy, es que se pueden unir diferentes vídeos, y guardar su resultado en un nuevo vídeo. Si tenemos 3 vídeos, simplemente tenemos que leerlos y luego unirlos con concatenate_videoclips.

```python
from moviepy.editor import *
clip1 = VideoFileClip("video1.mp4")
clip2 = VideoFileClip("video2.mp4").subclip(5,20)
clip3 = VideoFileClip("video3.mp4")
final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("resultado.mp4")
```

Además de unir diferentes vídeos, también podemos aplicar las transformaciones que queramos sobre cada vídeo, como crear un subclip(), cambiar la velocidad o lo que se nos ocurra.

## Redimensionar

Tal vez tengamos un vídeo con una resolución muy grande y queramos generar una versión más pequeña. En una línea de código se puede realizar el redimensionado, en este caso para un ancho de 480.

```python
from moviepy.editor import *
video = VideoFileClip("video_ejemplo.mp4")
reducido = video.resize(width=480).write_videofile("reducido.mp4")
reducido.write_videofile("resultado.mp4")
```

## Extraer audio

También podemos extraer el audio de un vídeo, y almacenarlo en mp3 u otro formato que queramos.

```python
from moviepy.editor import *
video = VideoFileClip("video_ejemplo.mp4")
audio = video.audio
audio.write_audiofile("audio.mp3")
```

Y para que veas toda la potencia que tiene moviepy, te dejamos con el clásico texto de apertura de Start Wars, hecho con este paquete. Para más información consulta la documentación oficial.