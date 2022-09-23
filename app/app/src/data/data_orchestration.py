from src.data.data_transform import DataPrep, FilterData
import numpy as np


def data_prep(filename):
    ld = DataPrep()
    data = ld.load_data(filename)
    data = data.replace('', np.nan)
    data = ld.fill_nan_value(data)
    filled_data = data
    prep_data = ld.create_segments(filled_data)
    return prep_data


def data_filter(filename, country_code, segment):
    data = data_prep(filename)
    fd = FilterData(data)
    country_data = fd.filter_data_of_country(country_code)
    valid_values = fd.filter_valid_values(country_data)
    amount_by_segment = fd.filter_voucher_amount_by_segment(valid_values,
                                                            segment)
    return amount_by_segment
