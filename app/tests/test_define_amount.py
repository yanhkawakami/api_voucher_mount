from src.define_amount import AmountRecency, AmountFrequency
import src.data.data_orchestration as do
import pandas as pd


ar = AmountRecency("2019-05-03 00:00:00", "2018-05-03 00:00:00")
af = AmountFrequency(10)
data = do.data_prep('tests/test_content/test_data.parquet.gzip')


def test_filter_amount_recency():
    r = ar.filter_amount_recency(data, '30-60')
    assert isinstance(r, pd.Series)


def test_get_amount_by_recency():
    r = ar.get_amount_by_recency("Peru", 'recency_segment')
    assert r == 2640.0


def test_filter_amount_frequency():
    r = af.filter_amount_frequency(data, '5-13')
    assert isinstance(r, pd.Series)


def test_get_amount_by_frequency():
    r = af.get_amount_by_frequency("Peru", 'frequent_segment')
    assert r == 2640.0
