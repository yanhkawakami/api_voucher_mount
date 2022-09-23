import pandas as pd


class DataPrep:
    def __init__(self) -> None:
        pass

    def load_data(self, path_file):
        """
        Function that loads data from parquet.
        """
        data = pd.read_parquet(path_file)
        return data

    def fill_nan_value(self, data):
        """
        Function to fill NaN values of Dataframe.
        """
        data = data.fillna(0)
        return data

    def support_frequency_segment(self, total_orders):
        """
        Function that supports the creating of
        frequency segment column.
        """
        # Convert String to float to make comparison
        total_orders = float(total_orders)

        # Rules of orders
        if total_orders >= 0 and total_orders < 5:
            return "0-4"
        elif total_orders >= 5 and total_orders < 14:
            return "5-13"
        elif total_orders >= 14 and total_orders < 38:
            return "14-37"
        else:
            return 'N/A'

    def support_recency_segment(self, difference_days):
        """
        Function that supports the creating of
        recency segment column.
        """
        # Convert Timedelta to int to make comparison
        difference_days = int(difference_days.days)

        # Rules of days
        if difference_days >= 30 and difference_days < 61:
            return "30-60"
        elif difference_days >= 61 and difference_days < 91:
            return "61-90"
        elif difference_days >= 91 and difference_days < 121:
            return "91-120"
        elif difference_days >= 121 and difference_days < 181:
            return "91-120"
        else:
            return '180+'

    def create_segments(self, data):
        """
        Function that creates segments on dataframe.
        """
        # Create the frequency segment based on orders
        data["frequency_segment"] = data["total_orders"].\
            apply(self.support_frequency_segment)

        # Create difference of days
        data["difference_days"] = \
            pd.to_datetime(data["last_order_ts"]) - data["first_order_ts"]

        # Create the recency segment based on difference of days
        data["recency_segment"] = data["difference_days"].\
            apply(self.support_recency_segment)

        # Drop column that is not necessary anymore
        data = data.drop(["difference_days"], axis=1)
        return data


class FilterData:
    def __init__(self, data) -> None:
        self.data = data
        pass

    def filter_data_of_country(self, country_code):
        """
        Function that filters data from country based on
        country_code passed by parameter
        """
        # Filter data by country_code
        filtered_data = self.data.query("country_code == @country_code")
        return filtered_data

    def filter_valid_values(self, filtered_data):
        """
        Function that filters only valid values
        """
        # Removing frequency segment not valid
        filtered_data = filtered_data[filtered_data.frequency_segment != 'N/A']
        return filtered_data

    def filter_voucher_amount_by_segment(self, filtered_data, segment):
        """
        Function that counts amount by segment and
        filter only most used voucher amount
        """
        # Uses filetered data to count by segment
        filtered_amount = filtered_data.groupby([segment, 'voucher_amount']) \
            .size() \
            .reset_index(name='count') \
            .sort_values([segment, 'count'], ascending=False) \
            .loc[:, [segment, 'voucher_amount', 'count']] \
            .drop_duplicates(subset=[segment])
        return filtered_amount
