from src.data.data_transform import DataPrep, FilterData
import numpy as np


def data_prep(filename):
    """
    Function to orchestrate whole data prep.
    """
    ld = DataPrep()
    # Load data stored in parquet as dataframe
    data = ld.load_data(filename)

    # Replace NaN in empty string fields
    data = data.replace('', np.nan)

    # Fill NaN values
    data = ld.fill_nan_value(data)
    filled_data = data

    # Create frequency and recency segments
    prep_data = ld.create_segments(filled_data)
    return prep_data


def data_filter(filename, country_code, segment):
    """
    Function to filter only relevant data.
    """
    # Get data from data prep step
    data = data_prep(filename)
    fd = FilterData(data)

    # Filter data from country specified in API request
    country_data = fd.filter_data_of_country(country_code)

    # Filter valid values based os segment criteria
    valid_values = fd.filter_valid_values(country_data, segment)

    # Get most used voucher amount by segment
    amount_by_segment = fd.filter_voucher_amount_by_segment(valid_values,
                                                            segment)
    return amount_by_segment
