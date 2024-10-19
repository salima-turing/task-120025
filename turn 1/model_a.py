import unittest
import json

def transform_data(data):
	# Dummy data transformation function
	result = []
	for entry in data:
		transformed_entry = {
			"name": entry["name"].upper(),
			"age": entry["age"] * 2
		}
		result.append(transformed_entry)
	return result

class TestDataTransformation(unittest.TestCase):

	def test_transformation_with_differential_regression(self):
		# Dummy input data
		input_data = [
			{"name": "alice", "age": 25},
			{"name": "bob", "age": 30},
		]

		# Expected output data (based on current transformation logic)
		expected_output_data = [
			{"name": "ALICE", "age": 50},
			{"name": "BOB", "age": 60},
		]

		# Actual output data from the transformation function
		actual_output_data = transform_data(input_data)

		# Perform differential regression
		self.maxDiff = None
		self.assertEqual(json.dumps(actual_output_data, sort_keys=True), json.dumps(expected_output_data, sort_keys=True))

if __name__ == '__main__':
	unittest.main()
