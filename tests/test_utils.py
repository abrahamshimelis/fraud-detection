import unittest
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from src.utils import check_missing_data, check_duplicates, check_data_types, check_numeric_anomalies, get_numeric_columns, get_total_missing_percentage

class TestDataChecks(unittest.TestCase):

    def test_check_missing_data(self):
        df = pd.DataFrame({
            'A': [1, 2, np.nan],
            'B': [4, np.nan, np.nan],
            'C': [7, 8, 9]
        })
        result = check_missing_data(df)
        self.assertEqual(result['Column Name'].tolist(), ['A', 'B'])
        self.assertEqual(result['Missing Values'].tolist(), [1, 2])

    def test_get_total_missing_percentage(self):
        # Create a sample DataFrame with missing values
        data = {'A': [1, None, 3], 'B': [4.5, 5.6, None], 'C': ['x', 'y', 'z']}
        df = pd.DataFrame(data)

        # Calculate total percentage of missing values
        missing_data_percentage = get_total_missing_percentage(df)

        # Expected total percentage of missing values
        expected_percentage = 2 / (3 * 3) * 100  # Number of missing values / Total cells * 100

        # Check if the calculated percentage matches the expected percentage
        self.assertAlmostEqual(missing_data_percentage, expected_percentage, places=2)

    def test_check_duplicates(self):
        df = pd.DataFrame({
            'A': [1, 2, 2],
            'B': [4, 5, 5],
            'C': [7, 8, 8]
        })
        result = check_duplicates(df)
        self.assertEqual(result['A'].tolist(), [2])
        self.assertEqual(result['Number of Duplicates'].tolist(), [1])

    def test_check_data_types(self):
        df = pd.DataFrame({
            'A': [1, '2', 3],
            'B': [4.0, '5.0', 6.0],
            'C': ['7', '8', '9']
        })
        result = check_data_types(df)
        if isinstance(result, str):
            self.assertEqual(result, "Success: Data types per column are uniform.")
        else:
            self.assertEqual(result['Column Name'].tolist(), ['A', 'B'])
            self.assertEqual(result['Number of Different Data Types'].tolist(), [2, 2])


    def test_get_numeric_columns(self):
        # Create a sample DataFrame with different data types
        data = {'A': [1, 2, 3], 'B': [4.5, 5.6, 6.7], 'C': ['x', 'y', 'z']}
        df = pd.DataFrame(data)

        # Test if the function correctly identifies numeric columns
        numeric_columns = get_numeric_columns(df)
        expected_columns = ['A', 'B']  # Columns A and B have numeric data types
        self.assertEqual(numeric_columns, expected_columns)

    def test_check_numeric_anomalies(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 500, 6],
            'C': [7, 8, 9]
        })
        result = check_numeric_anomalies(df, 'B', 0, 100)
        self.assertEqual(result['Column Name'].tolist(), ['B'])

if __name__ == '__main__':
    unittest.main()