import pytest
from code.data_transformation import clean_data, transform_data

def test_clean_data_no_empty_values():
    data = clean_data(["data", "", "valid", None, "another"])
    print("Checking if there are no empty values in cleaned data...")
    assert "" not in data
    assert None not in data

def test_transform_data_format():
    data = ["raw_data_1", "raw_data_2"]
    transformed_data = transform_data(data)
    print("Checking if transformed data is in the expected format (e.g., a pandas DataFrame)...")
    assert isinstance(transformed_data, list)  # or pandas DataFrame

def test_transform_data_at_least_1_item():
    data = ["raw_data_1", "raw_data_2"]
    transformed_data = transform_data(data)
    print("Checking if transformed data has at least 1 item...")
    assert len(transformed_data) >= 1

# Run manually if needed
if __name__ == "__main__":
    test_clean_data_no_empty_values()
