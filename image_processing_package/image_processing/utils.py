# image_processing/utils.py
from PIL import Image
import os

def load_image(image_path: str) -> Image.Image:
    """Carrega uma imagem a partir de um caminho especificado."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")
    
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        raise ValueError(f"Não foi possível carregar a imagem: {e}")

def save_image(image: Image.Image, output_path: str) -> None:
    """Salva a imagem no caminho especificado."""
    try:
        image.save(output_path)
        print(f"Imagem salva com sucesso em {output_path}")
    except Exception as e:
        raise ValueError(f"Não foi possível salvar a imagem: {e}")

def validate_image_format(image: Image.Image, valid_formats=('JPEG', 'PNG')) -> bool:
    """Verifica se a imagem está em um formato válido."""
    if image.format not in valid_formats:
        raise ValueError(f"Formato inválido: {image.format}. Formatos aceitos: {valid_formats}")
    return True

def convert_image_mode(image: Image.Image, mode: str) -> Image.Image:
    """Converte a imagem para o modo especificado (por exemplo, 'RGB', 'L')."""
    if image.mode != mode:
        return image.convert(mode)
    return image
