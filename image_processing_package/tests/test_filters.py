# tests/test_filters.py
import unittest
from PIL import Image
from image_processing.filters import apply_grayscale, apply_sepia

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.image = Image.new('RGB', (100, 100), 'white')

    def test_grayscale(self):
        grayscale_image = apply_grayscale(self.image)
        self.assertEqual(grayscale_image.mode, 'L')

    def test_sepia(self):
        sepia_image = apply_sepia(self.image)
        self.assertEqual(sepia_image.mode, 'RGB')

if __name__ == '__main__':
    unittest.main()
