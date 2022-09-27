from src.data.user_data import UserRecency, UserFrequency
import pandas as pd


ur = UserRecency("2019-05-03 00:00:00", "2018-05-03 00:00:00")
uf = UserFrequency(10)


def test_calculate_recency():
    r = ur.calculate_recency()
    assert isinstance(r, pd.Timedelta)


def test_define_segment_group_recency_user():
    r = ur.define_segment_group_recency_user(pd.Timedelta(days=1))
    assert r == 'N/A'


def test_define_segment_group_frequency_user():
    r = uf.define_segment_group_frequency_user()
    assert r == "5-13"
