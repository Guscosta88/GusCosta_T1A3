from classes.bottle import bottle
from classes.logo import logo
import cowsay

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

    def welcome():
        enter = ""
        while True:
            if enter == "":
                enter = print(logo)
            elif enter != "":
                print(input("                             PRESS ENTER TO START! "))
                break




# class Food:

#     def __init__(self, name, recipe):
#         self.name = name
#         self.recipe = recipe
