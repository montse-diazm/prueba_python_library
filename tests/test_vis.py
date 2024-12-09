import unittest
import pandas as pd
from prueba_python_library.vis import plot_viz_barchart_01

class TestVisualizationFunctions(unittest.TestCase):
    
    def test_viz_barchart_01(self):
        df = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [10, 20, 30]})
        try:
            plot_viz_barchart_01(df, 'Category', 'Values')
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
