import pytest
from code.dashboard import load_data_from_file, clean_column_names

def test_should_pass():
    print("\nAlways True!")
    assert True

def test_load_data_from_file():
    df = load_data_from_file("cache/cleaned_data.json")
    print("Checking if dataframe has rows...")
    assert len(df) > 0

def test_clean_column_names_lowercase():
    df = load_data_from_file("cache/cleaned_data.json")
    df = clean_column_names(df)
    print("Checking if all column names are lowercase...")
    assert all(col == col.lower() for col in df.columns)

def test_clean_column_names_no_spaces():
    df = load_data_from_file("cache/cleaned_data.json")
    df = clean_column_names(df)
    print("Checking if column names have no spaces...")
    assert all(" " not in col for col in df.columns)

def test_dashboard_visualizations():
    df = load_data_from_file("cache/cleaned_data.json")
    df = clean_column_names(df)
    # Assuming you have a function that generates charts in your dashboard code
    chart = generate_chart(df)  # Replace with actual chart generation function
    print("Checking if chart is generated...")
    assert chart is not None

# Run manually if needed
if __name__ == "__main__":
    test_should_pass()
