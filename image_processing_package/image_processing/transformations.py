# image_processing/transformations.py
from PIL import Image

def rotate_image(image: Image.Image, angle: float) -> Image.Image:
    """Rotaciona a imagem pelo ângulo fornecido."""
    return image.rotate(angle)

def resize_image(image: Image.Image, size: tuple) -> Image.Image:
    """Redimensiona a imagem para o tamanho fornecido (largura, altura)."""
    return image.resize(size)
