from src.data.data_transform import DataPrep
from datetime import datetime


class UserRecency:
    def __init__(self, last_order_ts, first_order_ts) -> None:
        self.last_order_ts = last_order_ts
        self.first_order_ts = first_order_ts
        self.dp = DataPrep()

    def calculate_recency(self):
        format = '%Y-%m-%d %H:%M:%S'
        last_order_ts_dt = datetime.strptime((self.last_order_ts), format)
        first_order_ts_dt = datetime.strptime((self.first_order_ts), format)
        recency = last_order_ts_dt - first_order_ts_dt
        return recency

    def define_segment_group_recency_user(self, recency):
        segment_group = self.dp.support_recency_segment(recency)
        return segment_group


class UserFrequency:
    def __init__(self, total_orders) -> None:
        self.total_orders = total_orders
        self.dp = DataPrep()

    def define_segment_group_frequency_user(self):
        segment_group = self.dp.support_frequency_segment(self.total_orders)
        return segment_group
