import unittest
from prueba_python_library.statistics import calc_stats_find_mean_01, calc_stats_find_median_01, calc_stats_find_mode_01

class TestStatisticsFunctions(unittest.TestCase):
    
    def test_stats_find_median_01(self):
        self.assertEqual(calc_stats_find_median_01([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calc_stats_find_median_01([1, 2, 3, 4]), 2.5)

    def test_stats_find_mode_01(self):
        self.assertEqual(calc_stats_find_mode_01([1, 2, 2, 3]), 2)
        self.assertEqual(calc_stats_find_mode_01([1, 1, 1, 2, 2]), 1)

    def test_stats_find_mean_01(self):
        self.assertEqual(calc_stats_find_mean_01([1, 2, 3, 4]), 1.6666666666666667)

if __name__ == '__main__':
    unittest.main()
