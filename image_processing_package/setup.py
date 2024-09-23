# setup.py
from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'numpy',
    ],
    author="Seu Nome",
    description="Um pacote básico para processamento de imagens",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)
