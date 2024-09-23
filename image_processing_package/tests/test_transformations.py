# tests/test_transformations.py
import unittest
from PIL import Image
from image_processing.transformations import rotate_image, resize_image

class TestTransformations(unittest.TestCase):
    def setUp(self):
        self.image = Image.new('RGB', (100, 100), 'white')

    def test_rotate_image(self):
        rotated_image = rotate_image(self.image, 45)
        self.assertEqual(rotated_image.size, self.image.size)

    def test_resize_image(self):
        resized_image = resize_image(self.image, (50, 50))
        self.assertEqual(resized_image.size, (50, 50))

if __name__ == '__main__':
    unittest.main()
