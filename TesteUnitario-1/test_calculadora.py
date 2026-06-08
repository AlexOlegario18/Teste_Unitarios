import unittest
from calculadora import somar, subtrair, multiplicar, dividir, calcular_media

class TestCalculadora(unittest.TestCase):

    # --- Testes para somar(a, b) ---
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_somar_negativos(self):
        self.assertEqual(somar(-2, -3), -5)

    def test_somar_com_zero(self):
        self.assertEqual(somar(5, 0), 5)
        self.assertEqual(somar(0, 0), 0)

    # --- Testes para subtrair(a, b) ---
    def test_subtrair_positivos(self):
        self.assertEqual(subtrair(10, 5), 5)

    def test_subtrair_negativos(self):
        self.assertEqual(subtrair(-5, -2), -3)

    # --- Testes para multiplicar(a, b) ---
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(10, 0), 0)

    # --- Testes para dividir(a, b) ---
    def test_dividir_positivos(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    # --- Testes para calcular_media(lista) ---
    def test_calcular_media_inteiros(self):
        self.assertEqual(calcular_media([10, 8, 6]), 8)

    def test_calcular_media_decimais(self):
        self.assertEqual(calcular_media([2.5, 7.5]), 5.0)

    def test_calcular_media_um_elemento(self):
        self.assertEqual(calcular_media([10]), 10)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    # --- Exemplo de uso de subTest para múltiplos casos ---
    def test_somar_com_varios_casos(self):
        casos = [
            (2, 3, 5),
            (0, 0, 0),
            (-1, 1, 0),
            (10, -5, 5)
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b, esperado=esperado):
                self.assertEqual(somar(a, b), esperado)

if __name__ == '__main__':
    unittest.main()
