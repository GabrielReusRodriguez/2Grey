#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convierte una imagen a escala de grises."
    )
    parser.add_argument(
        "input",
        help="Ruta de la imagen de entrada",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Ruta de la imagen de salida (por defecto: <nombre>_grey.<ext>)",
    )
    return parser.parse_args()


def validate_input(path: Path) -> None:
    if not path.exists():
        print(f"Error: el archivo '{path}' no existe.", file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f"Error: '{path}' no es un archivo.", file=sys.stderr)
        sys.exit(1)


def build_output_path(input_path: Path, output_arg: str | None) -> Path:
    if output_arg:
        return Path(output_arg)
    stem = input_path.stem
    suffix = input_path.suffix or ".png"
    return input_path.parent / f"{stem}_grey{suffix}"


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)

    validate_input(input_path)

    output_path = build_output_path(input_path, args.output)

    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}", file=sys.stderr)
        sys.exit(1)

    grey = img.convert("L")
    grey.save(output_path)
    print(f"Imagen guardada en: {output_path}")


if __name__ == "__main__":
    main()
