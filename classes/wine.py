# The Class Wine holds the string value of 10 wine names available for the user to interact with.

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

# Initializes the Wine Class.

    def __init__(self, name):
        self.name = name

# The is_valid_wine method is used to check if the wine is available in the available wines list, it returns a boolean value.

    def is_valid_wine(self):
        return self.name in self.__available__wines