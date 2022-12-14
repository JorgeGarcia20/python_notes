import unittest
from entities.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        """Inicializa objetos para las pruebas"""

        self.name = 'iPhone'
        self.price = 1000.00

        self.smartphone = Product(self.name, self.price)

    def test_product(self):
        self.assertEqual(1, 1)

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name, 'El nombre no es correcto')
        self.assertEqual(product.price, price, 'El precio no es correcto')

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)
