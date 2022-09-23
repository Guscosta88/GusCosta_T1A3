from constants.logo import logo
from constants.bottle import bottle
import clearing

class Greetings:

    @classmethod
    def welcome(self):
        enter = ""
        while True:
            if enter == "":
                enter = print(logo)
            elif enter != "":
                print(input("\t\t\tPRESS ENTER TO START! "))
                break
    @classmethod
    def end(self):
        clearing.clear()
        print(bottle)
        exit()
