import pytest
from code.data_extraction import extract_data

def test_extract_data_non_empty():
    data = extract_data("some_url_or_file")
    print("Checking if extracted data is not empty...")
    assert len(data) > 0

def test_extract_data_format():
    data = extract_data("some_url_or_file")
    print("Checking if data is in the expected format (e.g., a list or dict)...")
    assert isinstance(data, list)  # or dict depending on what is returned

# Run manually if needed
if __name__ == "__main__":
    test_extract_data_non_empty()
