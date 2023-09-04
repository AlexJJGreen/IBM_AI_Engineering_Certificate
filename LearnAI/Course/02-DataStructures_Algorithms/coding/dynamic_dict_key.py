class DynamicDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, val):
        self.data[f"data_{val}"] = val
