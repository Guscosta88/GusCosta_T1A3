from constants.logo import logo

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


    def is_valid_wine(cls):
        return cls.name in cls.__available__wines