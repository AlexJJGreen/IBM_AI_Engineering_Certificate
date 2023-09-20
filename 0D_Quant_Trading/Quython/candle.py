class Candle:
     """
    Object mapping of a time series candle

    Attributes:
        timestamp (str): The timestamp of the candle.
        open_price (float): The opening price of the candle.
        high_price (float): The highest price during the time period.
        low_price (float): The lowest price during the time period.
        close_price (float): The closing price of the candle.
    """
     
    def __init__(self, timestamp, open_price, high_price, low_price, close_price):
        """
        Initializes a new Candle object.

        Args:
            timestamp (str): The timestamp of the candle.
            open_price (float): The opening price of the candle.
            high_price (float): The highest price during the time period.
            low_price (float): The lowest price during the time period.
            close_price (float): The closing price of the candle.
        """
        self.timestamp = timestamp
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price

        def body_size(self):
            return abs(self.close_price - self.open_price)
        
        def wick_size(self):
            return self.high_price - max(self.open_price, self.close_price)
            
        def tail_size(self):
            return min(self.open_price, self.close_price) - self.low_price
        
        def __str__(self):
            return f"Candle at {self.timestamp}: Open={self.open_price}, High={self.high_price}, Low={self.low_price}, Close={self.close_price}"
        
        def __str__(self):
            return f"Candle at {self.timestamp}: Open={self.open_price}, High={self.high_price}, Low={self.low_price}, Close={self.close_price}"
        
