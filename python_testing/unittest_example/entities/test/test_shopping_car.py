import unittest
from entities.product import Product, ProductDiscountError
from entities.shopping_car import ShoppingCar

'''
Covertura de codigo con unittest

$ coverage run -m unittest ..path/file.py 
$ coverage report -> show the report in the console
$ coverage html -> creates a web report

# to wacht the web report you need to create a server
$ python3 -m http.server -> http://0.0.0.0:8000/

'''


def is_available_to_skip():
    return True


def is_connected():
    return False


class TestShoppingCar(unittest.TestCase):

    """Se utilizan para compartir informacion entre las pruebas unitarias
    Se puede crear una conexion a la base de datos y compartirla a las pruenas unitarias
    """
    @classmethod
    def setUpClass(cls):
        """Se ejecuta antes de todas las pruebas"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta despues de todas las pruebas"""
        pass

    """Definir lo necesario para llevar a cabo"""

    def setUp(self):
        """Inicializa objetos para las pruebas"""

        self.name = 'iPhone'
        self.price = 1000.00

        self.smartphone = Product(self.name, self.price)

        self.shopping_car_1 = ShoppingCar()
        self.shopping_car_2 = ShoppingCar()
        self.shopping_car_2.add_product(self.smartphone)

    def tearDown(self):
        """Restablece los objetos en dado caso hayan sido alterados en las pruebas"""
        pass

    def test_shopping_car_empty(self):
        self.assertTrue(self.shopping_car_1.empty(),
                        'El carrito de compras no esta vacio.')

    def test_shopping_car_has_product(self):
        self.assertTrue(self.shopping_car_2.has_products(),
                        'El carrito de compras no esta vacio.')
        self.assertFalse(self.shopping_car_2.empty())

    def test_product_in_shopping_car(self):
        product = Product('Nuevo producto', 10)
        self.shopping_car_2.add_product(product)

        self.assertIn(product, self.shopping_car_2.products)
        self.assertIn(self.smartphone, self.shopping_car_2.products)

    def test_product_not_in_shoppin_car(self):
        self.shopping_car_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_car_2.products)

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.00, discount=11.00)

    def test_total_shopping_car(self):
        self.shopping_car_1.add_product(Product('Libro', 15.00))
        self.shopping_car_1.add_product(Product('Camara', 700.00, 70.00))
        self.shopping_car_1.add_product(Product('PC', 1000.00, 0.00))

        self.assertGreater(self.shopping_car_1.total, 0)
        self.assertLess(self.shopping_car_1.total, 2000)
        self.assertEqual(self.shopping_car_1.total, 1645.00)

    def test_total_empty_shopping_car(self):
        self.assertEqual(self.shopping_car_1.total, 0.0)

    # Cuando el dev conoce la razón para no ser ejecutada
    @unittest.skip('La prueba no cumple los requerimientos necesarios.')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(is_available_to_skip(), 'No se encuentra con todos los requerimientos.')
    def test_skip_example_2(self):
        pass

    @unittest.skipUnless(is_connected(), 'No se encuentra con todos los requerimientos.')
    def test_skip_example_3(self):
        pass
    # skipIf -> evalua sobre verdadero
    # skipUnless -> Evalua sobre false

    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name)


if __name__ == '__main__':
    unittest.main()
