from image_processing.utils import load_image, save_image
from image_processing.filters import apply_grayscale

# Carregar uma imagem
image = load_image('minha_imagem.jpg')

# Aplicar filtro em escala de cinza
grayscale_image = apply_grayscale(image)

# Salvar a imagem processada
save_image(grayscale_image, 'imagem_em_escala_cinza.jpg')
