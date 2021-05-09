import unittest
from calculo_inicial import Calculo

class TestCalculoInicial(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculo()
        
    def test_sum(self):
        self.assertEqual(self.calc.add(2, 30), 32)

if __name__ == '__main__':
    unittest.main()
