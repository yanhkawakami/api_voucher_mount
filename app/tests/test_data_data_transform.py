from src.data.data_transform import DataPrep, FilterData
import src.data.data_orchestration as do
import numpy as np
import pandas as pd


dp = DataPrep()
data = dp.load_data('tests/test_content/test_data.parquet.gzip')
data_filter = do.data_prep('tests/test_content/test_data.parquet.gzip')
fd = FilterData(data_filter)


def test_load_data():
    r = dp.load_data('tests/test_content/test_data.parquet.gzip')
    assert isinstance(r, pd.DataFrame)


def test_fill_nan_value():
    r = dp.fill_nan_value(data)
    assert isinstance(r, pd.DataFrame)


def test_support_frequency_segment():
    assert dp.support_frequency_segment(4) == "0-4"
    assert dp.support_frequency_segment(5) == "5-13"
    assert dp.support_frequency_segment(14) == "14-37"
    assert dp.support_frequency_segment(140) == "N/A"


def test_support_recency_segment():
    assert dp.support_recency_segment(pd.Timedelta(days=4)) == "N/A"
    assert dp.support_recency_segment(pd.Timedelta(days=30)) == "30-60"
    assert dp.support_recency_segment(pd.Timedelta(days=61)) == "61-90"
    assert dp.support_recency_segment(pd.Timedelta(days=91)) == "91-120"
    assert dp.support_recency_segment(pd.Timedelta(days=121)) == "121-180"
    assert dp.support_recency_segment(pd.Timedelta(days=200)) == "180+"


def test_create_segments():
    data_file = data.replace('', np.nan)
    data_file = dp.fill_nan_value(data_file)
    r = dp.create_segments(data_file)
    assert isinstance(r, pd.DataFrame)


def test_filter_data_of_country():
    r = fd.filter_data_of_country("Peru")
    assert r["country_code"].unique() == ["Peru"]


def test_filter_valid_values():
    r = fd.filter_valid_values(data_filter, 'frequent_segment')
    assert 'N/A' not in r["frequent_segment"].unique()


def test_filter_voucher_amount_by_segment():
    r = fd.filter_voucher_amount_by_segment(data_filter, 'recency_segment')
    assert r is not None
