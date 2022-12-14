import pytest
"""
Para que pytest funcione correctamente debemos usar el prefijo test_ en el nombre
del fichero y en los nombres de las funciones.
"""
# Lo recomendable es usar clases para que las pruebas compartan el mismo contexto.

# def test_example():
#     assert 10 == 10, 'La prueba no ha pasado'

# Para ejecutar una prueba -> pytest test_main.py:: TestExample:: test_resta_dos_numeros
# Para ejecutar una clase -> pytest test_main.py:: TestExample


class TestExample:

    @classmethod
    def setup_class(cls):
        print('>>> setup_class -> se ejecuta antes de todas las pruebas')

    @classmethod
    def teardown_class(cls):
        print('>>> tear_down -> se ejecuta despues de todas las pruebas')

    # Definimos acciones que se ejecutan antes o despues respectivamente de las pruebas

    def setup_method(self):
        # print('>>> Se ejecuta antes de cada prueba')
        self.x = 10
        self.y = 20

    def teardown_method(self):
        print('>>> Se ejecuta despues de cada prueba')

    def test_suma_dos_numeros(self):
        assert self.x + self.y == 30, 'La suma no es correcta.'

    def test_resta_dos_numeros(self):
        assert self.x - self.y == -10, 'La resta no es correcta.'


class TestExample2:

    def test_multiplicacion_dos_numeros(self):
        assert 2 * 10 == 20, 'La multiplicacion no es correcta.'
