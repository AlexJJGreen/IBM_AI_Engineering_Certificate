import datetime


class TimeSeries:
    def __init__(self, interval):
        self.interval = interval
        self.items = []

    def __getitem__(self, index):
        return self.items[index]


class Candlestick:
    def __init__(
        self,
        open_price: int,
        close_price: int,
        high_price: int,
        low_price: int,
        date_time,
        interval,
    ):
        self.open_price = open_price
        self.close_price = close_price
        self.high_price = high_price
        self.low_price = low_price
        self.date_time = date_time
        self.interval = interval

    def __repr__(self):
        return f"Open: {self.open_price} Close: {self.close_price} High: {self.high_price} Low: {self.low_price}"
