import unittest
from calculador import Calculador

class TestBasoic(unittest.TestCase):

    def setUp(self):
        self.cal = Calculador()

    def test_una_calculadora_nueva_inicia_en_cero(self): 
        self.assertEqual(0, self.cal.valor())

    def test_la_suma_de_5_mas_3_deber_dar_8(self):
        self.cal.suma(5,3)
        self.assertEqual(8, self.cal.valor())
    def test_la_suma_de_9_mas_3_deber_dar_12(self):
        self.cal.suma(9,3)
        self.assertEqual(12, self.cal.valor())