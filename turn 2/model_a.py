import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

class TestDataIntegration(unittest.TestCase):

	def test_structural_data_change(self):
		# Dummy data for actual and expected results
		actual_data = pd.DataFrame({
			"name": ["Alice", "Bob"],
			"age": [25, 30],
			"location": ["New York", "San Francisco"]
		})

		expected_data = pd.DataFrame({
			"name": ["Alice", "Bob"],
			"age": [25, 30],
			"location": ["New York", "San Jose"]  # Changed location to introduce discrepancy
		})

		try:
			assert_frame_equal(actual_data, expected_data, check_dtype=False)
			print("Test Passed: Structural data remains unchanged")
		except AssertionError as e:
			print(f"Test Failed: Structural data change detected.\n{e}")

if __name__ == "__main__":
	unittest.main()
