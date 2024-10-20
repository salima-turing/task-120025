import pandas as pd
import pytest
from pytest_regressions import data_regression

@pytest.fixture
def dummy_data():
	"""
    Generate dummy data for testing
    """
	data = {
		"name": ["Alice", "Bob", "Charlie"],
		"age": [25, 30, 22],
		"email": ["alice@example.com", "bob@example.com", "charlie@example.com"],
	}
	return pd.DataFrame(data)

@pytest.fixture
def expected_data():
	"""
    Baseline data for comparison
    """
	data = {
		"name": ["Alice", "Bob", "Charlie"],
		"age": [25, 30, 22],
		"email": ["alice@example.com", "bob@example.com", "charlie@example.com"],
		"city": ["New York", "San Francisco", "Los Angeles"],  # added a new column for structural change
	}
	return pd.DataFrame(data)

def test_data_structure_change(dummy_data, expected_data, data_regression):
	"""
    Test to check if the data structure has changed
    """
	# Processing the data (e.g., applying transformations, etc.)
	processed_data = dummy_data

	# Check for structural changes
	data_regression.check(processed_data, baseline_name="expected_data")
