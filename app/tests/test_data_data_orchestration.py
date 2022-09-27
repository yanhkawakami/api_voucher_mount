import src.data.data_orchestration as do
import pandas as pd


def test_data_prep():
    r = do.data_prep('tests/test_content/test_data.parquet.gzip')
    assert isinstance(r, pd.DataFrame)


def test_data_filter():
    r = do.data_filter('tests/test_content/test_data.parquet.gzip',
                       'Peru', 'frequency_segment')
    assert isinstance(r, pd.DataFrame)
