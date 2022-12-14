# assert
import unittest


class TestExample(unittest.TestCase):

    def test_suma_numeros(self):
        x = 10
        y = 20
        resultado = x + y
        # 30

        self.assertEqual(resultado, 30)

    def test_restar_numeros(self):
        self.assertEqual(30 - 20, 10)


def sumar_numeros_positivos(x: int, y: int) -> int:
    """Funcion que suma dos números enteros positivos.

    Args:
            x (int): primer número
            y (int): segundo número

    Returns:
            int: x + y
    """

    assert x > 0 and y > 0, 'Solo se pueden sumar números enteros positivos'
    return x + y


if __name__ == '__main__':
    #resultado = sumar_numeros_positivos(-30, 10)
    # print(resultado)
    unittest.main()  # Ejecuta todos los metodos con el prefijo test_ de las clases que hereden de TestCase
