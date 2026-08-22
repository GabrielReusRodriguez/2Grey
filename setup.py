from pathlib import Path

from setuptools import setup


README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")


setup(
    name="two-grey",
    version="1.0.0",
    description="Convierte imágenes a escala de grises desde la línea de comandos.",
    long_description=README,
    long_description_content_type="text/markdown",
    scripts=["2Grey.py"],
    install_requires=["Pillow>=9.0.0"],
    python_requires=">=3.10",
)
