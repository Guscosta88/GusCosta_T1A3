# arts imported from constants folder
from constants.logo import logo
from constants.bottle import bottle

# packages py imported
import colorterminal
import clearing

# The Class Greetings holds two methods: 
# The welcome method that displays the ASCII logo imported from the constant logo.py file and prompts the user to press enter to start.
# The end method that clears any remaining data with the help of the clearing py package, displays the ASCII bottle art imported from 
# the constant bottle.py file with a thank you and a Do not drink and drive message to be displayed when the user is done using the app.


class Greetings:

    @classmethod
    def welcome(self):
        enter = ""
        while True:
            if enter == "":
                enter = print(colorterminal.ColorText.PURPLE + logo)
            elif enter != "":
                print(input("\t\t\tPRESS ENTER TO START! "))
                break
    @classmethod
    def end(self):
        clearing.clear()
        print(bottle)
        exit()





# print(colorterminal.ColorText.RED + 'Hello' + colorterminal.ColorText.PURPLE + ' World')