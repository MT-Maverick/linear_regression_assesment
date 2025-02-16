# validate_data.py
import pytest
import pandas as pd
import os


@pytest.fixture(scope="module",autouse=True)
def test_csv_existance():
    assert os.path.exists(path='sampled_field_df.csv')

def test_colums():
    df = pd.read_csv('sampled_field_df.csv')
    expected_colums = ['Field_ID', 'Elevation', 'Location', 'Slope','Rainfall', 'Ave_temps','Soil_fertility', 'Soil_type', 'pH', 'Pollution_level', 'Crop_type', 'Standard_yield']
    assert set(df.columns) == set(expected_colums)

def test_crop_types():
    df = pd.read_csv('sampled_field_df.csv')
    expected_values = ['cassava', 'tea', 'wheat', 'potato', 'banana', 'coffee', 'rice','maize']
    assert set(df['Crop_type'].unique()).issubset(set(expected_values))

def test_no_missing_values():
    df = pd.read_csv('sampled_field_df.csv')
    assert df.isnull().sum().sum() == 0
