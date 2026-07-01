# 2Grey

Convertidor de imágenes a escala de grises desde la línea de comandos, escrito en Python.

## Requisitos

- Python 3.10+
- [Pillow](https://pillow.readthedocs.io/)

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd 2Grey

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Uso básico — genera <nombre>_grey.<ext> junto al archivo original
python 2Grey.py imagen.png

# Especificar nombre de salida
python 2Grey.py imagen.png -o resultado.png
```

### Argumentos

| Argumento | Descripción |
|-----------|-------------|
| `input` | Ruta de la imagen de entrada (obligatorio) |
| `-o, --output` | Ruta de la imagen de salida (opcional) |

### Ejemplo

```bash
$ python 2Grey.py foto.jpg
Imagen guardada en: foto_grey.jpg
```

## Formatos soportados

Cualquier formato que soporte Pillow: PNG, JPEG, GIF, BMP, TIFF, WebP, entre otros.

