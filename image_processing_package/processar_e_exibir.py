from image_processing.utils import load_image, save_image
from image_processing.filters import apply_grayscale
import matplotlib.pyplot as plt

# Carregar uma imagem
image = load_image('minha_imagem.jpg')

# Aplicar filtro em escala de cinza
grayscale_image = apply_grayscale(image)

# Salvar a imagem processada
save_image(grayscale_image, 'imagem_em_escala_cinza.jpg')

# Exibir a imagem original e a imagem processada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagem em Escala de Cinza')
plt.imshow(grayscale_image, cmap='gray')
plt.axis('off')

plt.show()
