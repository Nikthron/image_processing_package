# image_processing/filters.py
from PIL import Image

def apply_grayscale(image: Image.Image) -> Image.Image:
    """Aplica filtro em escala de cinza à imagem."""
    return image.convert("L")

def apply_sepia(image: Image.Image) -> Image.Image:
    """Aplica filtro sépia à imagem."""
    width, height = image.size
    pixels = image.load()
    
    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            pixels[px, py] = (min(tr, 255), min(tg, 255), min(tb, 255))

    return image
