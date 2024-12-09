import unittest
from prueba_python_library.math import calc_math_add_01, calc_math_multiply_01, calc_math_lcm_01

class TestMathFunctions(unittest.TestCase):
    
    def test_math_add_01(self):
        self.assertEqual(calc_math_add_01(1, 2, 3), 6)
        self.assertEqual(calc_math_add_01(10, -5, 5), 10)

    def test_math_multiply_01(self):
        self.assertEqual(calc_math_multiply_01(1, 2, 3), 6)
        self.assertEqual(calc_math_multiply_01(10, -2, 5), -100)

    def test_math_lcm_01(self):
        self.assertEqual(calc_math_lcm_01(4, 5), 20)
        self.assertEqual(calc_math_lcm_01(1, 2), 6)

if __name__ == '__main__':
    unittest.main()
