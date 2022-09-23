class Wine:
    __available__wines = [
        "Cabernet sauvignon",
        "Pinot noir",
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


    def is_valid_wine(self):
        return self.name in self.__available__wines