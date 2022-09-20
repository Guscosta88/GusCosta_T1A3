from classes.wine import Wine, Food
from classes.bottle import bottle
from classes.logo import logo
from simple_term_menu import TerminalMenu
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

pairing = [
    {'type':'Cabernet Sauvignon', 'protein':'Roast beef', 'cheese':'Gouda cheese', 'fruit':'Plums'},
    {'type':'Pinot Noir', 'protein':'Salmon', 'cheese':'Gruyere cheese', 'fruit':'Apples'},
    {'type':'Shiraz', 'protein':'Duck', 'cheese':'Pecorino cheese', 'fruit':'Apricot'},
    {'type':'Merlot', 'protein':'Pork', 'cheese':'Camembert cheese', 'fruit':'Figs'},
    {'type':'Sangiovese', 'protein':'Spaghetti and meatballs', 'cheese':'Mozzarella cheese', 'fruit':'Strawberry'},
    {'type':'Chianti', 'protein':'Pizza', 'cheese':'Parmesan cheese', 'fruit':'Apples'},
    {'type':'Bordeaux', 'protein':'Lamb', 'cheese':'Brie cheese', 'fruit':'Pears'},
    {'type':'Tempranillo', 'protein':'Lasagna', 'cheese':'Manchego cheese', 'fruit':'Cherries'},
    {'type':'Carmenere', 'protein':'BBQ', 'cheese':'Cheddar cheese', 'fruit':'Plums'},
    {'type':'Rose', 'protein':'Seafood', 'cheese':'Feta cheese', 'fruit':'Watermelon'}
]

recipe = [
    {'name':'Roast beef','protein':'ROAST BEEF: \n 500g of beef \n 100g of butter \n Salt and Pepper to taste \n \n METHOD: \n Put the beef on a tray, rub butter salt and pepper all over, \n put it in the oven at 180° for 1hour.', 'cheese':'Gouda cheese', 'fruit':'Plums'},
    {'name':'Salmon','protein':'Salmon', 'cheese':'Gruyere cheese', 'fruit':'Apples'},
    {'name':'Duck','protein':'Duck', 'cheese':'Pecorino cheese', 'fruit':'Apricot'},
    {'name':'Pork','protein':'Pork', 'cheese':'Camembert cheese', 'fruit':'Figs'},
    {'name':'Spaghetti and meatballs','protein':'Spaghetti and meatballs', 'cheese':'Mozzarella cheese', 'fruit':'Strawberry'},
    {'name':'Pizza','protein':'Pizza', 'cheese':'Parmesan cheese', 'fruit':'Apples'},
    {'name':'Lamb','protein':'Lamb', 'cheese':'Brie cheese', 'fruit':'Pears'},
    {'name':'Lasagna','protein':'Lasagna', 'cheese':'Manchego cheese', 'fruit':'Cherries'},
    {'name':'BBQ','protein':'BBQ', 'cheese':'Cheddar cheese', 'fruit':'Plums'},
    {'name':'Seafood','protein':'Seafood', 'cheese':'Feta cheese', 'fruit':'Watermelon'}
]




Wine.welcome()

def not_valid_wine():
    options = ["I want to try another wine", "I want to exit the app"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "I want to try another wine":
        print(wine_questions())
    else:
        print(bottle)
    # print(f"You have selected {options[menu_entry_index]}!")




def wine_questions():
    input_message = input("What type of red wine do you have in mind (Please enter full item name)? ")
    wine_input = input_message
    wine_validation = Wine.is_valid_wine(wine_input)
    if wine_validation:
        print(f"{wine_input} goes well with the foods bellow, choose one for Recipe!")
        for pair in pairing:
            if wine_input == pair['type']:
                    food_options = [pair['protein'], pair['cheese'], pair['fruit']]
                    terminal_menu = TerminalMenu(food_options)
                    menu_entry_index = terminal_menu.show()
                    for item in recipe:
                        if food_options[menu_entry_index] == pair['protein']:
                            if pair['protein'] == item['name']:
                                print(item['protein'])
                                not_valid_wine()
                        elif food_options[menu_entry_index] == pair['cheese']:
                            if pair['cheese'] == item['cheese']:
                                print(item['cheese'])
                                not_valid_wine()
                        else:
                            print(item['fruit'])
                            not_valid_wine()
    else:
        print(f"{wine_input} it is not a valid wine!")
        print(not_valid_wine())

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





