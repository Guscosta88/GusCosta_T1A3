from classes.wine import Wine, Food
from classes.bottle import bottle
from classes.logo import logo
import cowsay

# cowsay.cheese('Cheese goes well with any wine!')
# cowsay.pig('Pinot and Pork are best friends')
# cowsay.cow('You cant go wrong with Beef and Cabernet')
# cowsay.turkey('Poultry and Rose')
# print(bottle)


# print(logo)





# if invalid_wine_input == "Y":
#     print(wine_input)
# else:
#     print(bottle)

Wine.welcome()


def wine_questions():
    input_message = input("What type of red wine do you have in mind (Please enter full item name)? ")
    wine_input = input_message
    wine_validation = Wine.is_valid_wine(wine_input)
    if wine_validation:
        print(f"{wine_input} goes well with the foods bellow, choose one for Recipe!")
    else:
        print(input("Not a valid wine, Do you want to try another wine?(Y/N) "))

wine_questions()





# input_message = input("What type of red wine do you have in mind (Please enter full item name)? ")
# invalid_wine_input = input("Not a valid wine, Do you want to try another wine?(Y/N) ")
# wine_validation = Wine.is_valid_wine(wine_input)
# if wine_validation:
#     print(f"{wine_input} goes well with the foods bellow, choose one for Recipe!")
# else:
#     print(invalid_wine_input)

# if invalid_wine_input == "Y":
#     print(wine_input)
# else:
#     print(bottle)





