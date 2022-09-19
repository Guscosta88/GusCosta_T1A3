class Wine:
    __available__wines = [
        "Cabernet Sauvignon",
        "Pinot Noir",
        "Shiraz",
        "Merlot",
        "Sangiovese",
        "Chianti",
        "Bordeaux",
        "Tempranillo",
        "Carmenere",
        "Rose"
    ]
    def __init__(self, name):
        self.name = name

    @classmethod
    def is_valid_wine(cls, wine):
        return wine in cls.__available__wines

class Food:
    def __init__(self, name):
        