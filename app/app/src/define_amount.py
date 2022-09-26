from src.data.user_data import UserFrequency, UserRecency
import src.data.data_orchestration as data_orchestration


class AmountRecency:
    def __init__(self, last_order_ts, first_order_ts) -> None:
        self.ur = UserRecency(last_order_ts, first_order_ts)
        pass

    def filter_amount_recency(self, data, segment_group):
        """
        Function that filters voucher amount by recency.
        """
        amount = data.query("recency_segment == @segment_group").loc[
            :, 'voucher_amount']
        return amount

    def get_amount_by_recency(self,
                              country_code,
                              segment):
        """
        Function that gets amount recommended for that user
        base on recency.
        """
        # Calculate recency based on order dates
        user_recency = self.ur.calculate_recency()

        # Get group of recency of user
        user_group_recency = \
            self.ur.define_segment_group_recency_user(user_recency)

        # Get data filtered by country code and segment
        filtered_data = \
            data_orchestration.data_filter(
                'src/data/content/data.parquet.gzip',
                country_code,
                segment)

        # Get voucher amount by segment of user
        amount = self.filter_amount_recency(filtered_data,
                                            user_group_recency)
        return list(amount.values)[0]


class AmountFrequency:
    def __init__(self, total_orders) -> None:
        self.uf = UserFrequency(total_orders)
        pass

    def filter_amount_frequency(self, data, segment_group):
        """
        Function that filters voucher amount by frequency.
        """
        amount = data.query("frequency_segment == @segment_group").loc[
            :, 'voucher_amount']
        return amount

    def get_amount_by_frequency(self,
                                country_code,
                                segment):
        """
        Function that gets amount recommended for that user
        base on frequency.
        """
        # Get group of frequency of user
        user_group_frequency = self.uf.define_segment_group_frequency_user()

        # Get data filtered by country code and segment
        filtered_data = \
            data_orchestration.data_filter(
                'src/data/content/data.parquet.gzip',
                country_code,
                segment)
        # Get voucher amount by segment of user
        amount = self.filter_amount_frequency(filtered_data,
                                              user_group_frequency)
        return list(amount.values)[0]
