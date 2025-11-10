from src.data_handler import SolarDataProcessor
import pandas as pd

def test_clean_data():
    processor = SolarDataProcessor("data/benin_clean.csv", "Benin")
    df = processor.clean_data()
    assert isinstance(df, pd.DataFrame)
    assert "Country" in df.columns
    assert df["GHI"].notnull().all()
