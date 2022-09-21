from classes.greetings import Greetings
from classes.wine import Wine
from classes.pair import Pair
from classes.recipe import Recipe
from simple_term_menu import TerminalMenu
import clearing
import cowsay

# cowsay.cheese('Cheese goes well with any wine!')
# cowsay.pig('Pinot and Pork are best friends')
# cowsay.cow('You cant go wrong with Beef and Cabernet')
# cowsay.turkey('Poultry and Rose')

pairing = [
    {'type':'Cabernet Sauvignon', 'protein':'Roast beef', 'cheese':'Gouda cheese', 'fruit':'Plums'},
    {'type':'Pinot Noir', 'protein':'Salmon', 'cheese':'Gruyere cheese', 'fruit':'Apples'},
    {'type':'Shiraz', 'protein':'Duck', 'cheese':'Pecorino cheese', 'fruit':'Apricot'},
    {'type':'Merlot', 'protein':'Pork', 'cheese':'Camembert cheese', 'fruit':'Figs'},
    {'type':'Sangiovese', 'protein':'Spaghetti Bolognese', 'cheese':'Mozzarella cheese', 'fruit':'Strawberry'},
    {'type':'Chianti', 'protein':'Pizza', 'cheese':'Parmesan cheese', 'fruit':'Apples'},
    {'type':'Bordeaux', 'protein':'Lamb', 'cheese':'Brie cheese', 'fruit':'Pears'},
    {'type':'Tempranillo', 'protein':'Lasagna', 'cheese':'Manchego cheese', 'fruit':'Cherries'},
    {'type':'Carmenere', 'protein':'BBQ', 'cheese':'Cheddar cheese', 'fruit':'Plums'},
    {'type':'Rose', 'protein':'Seafood', 'cheese':'Feta cheese', 'fruit':'Watermelon'}
]

recipe = [
    {'name':'Roast beef','protein':'ROAST BEEF: \n 500g of beef \n 100g of butter \n Salt and Pepper to taste \n \n METHOD: \n Put the beef on a tray, rub butter salt and pepper all over, \n put it in the oven at 180° for 1hour.\n', 'cheese':'Gouda cheese', 'fruit':'Plums'},
    {'name':'Salmon','protein':'SALMON: \n 2 Slices of Salmon \n 100g of Butter \n Salt and pepper to taste \n Italian herbs \n \n METHOD: \n Season the fish with salt, pepper and herbs, \n add butter to a frying pan, cook both sides of \n the fish untill preferred level of doneness.\n', 'cheese':'Gruyere cheese', 'fruit':'Apples'},
    {'name':'Duck','protein':'DUCK: \n 200g Duck Breasts \n 2tb of Olive Oil \n 1 Clove of garlic \n Lemon Pepper, Salt, to taste \n \n METHOD: \n Preheat oven to 180°, season the breasts with salt, \n Pepper and garlic, add Olive Oil to a frying pan, \n cook both sides untill brown, finish cooking for another 20min in the oven.\n', 'cheese':'Pecorino cheese', 'fruit':'Apricot'},
    {'name':'Pork','protein':'PORK: \n 1 Pork Leg \n Salt Pepper \n Aluminium Foil \n Oil \n \n METHOD: \n Get a Tray, add the pork leg, rub salt and pepper, \nadd oil for the crackling, roll aluminium foil around \n the tray, bake at 180° for 2 hours.\n', 'cheese':'Camembert cheese', 'fruit':'Figs'},
    {'name':'Spaghetti Bolognese','protein':'SPAGHETTI BOLOGNESE: \n 500g minced meat \n 1 can tomato sauce \n 500g Spaghetti \n Parmesan cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Cook spaghetti pasta in salty boiling water, \n fry oil with onion and garlic, add seasoned minced meat, \n when meat is done add tomato sauce, cook for 20 minutes, \n add water if needed, mix it with the pasta, add some parmesan, enjoy.\n', 'cheese':'Mozzarella cheese', 'fruit':'Strawberry'},
    {'name':'Pizza','protein':'PIZZA: \n 1 Sliced Pepperoni sausage \n mozzarella cheese \n tomato sauce \n pizza base \n oregano \n \n METHOD: \n preheat oven to 180, get a tray, put the pizza base, \n spread tomato sauce, add cheese, add sliced pepperoni, \n add oregano, bake for 10 to 20 minutes.\n', 'cheese':'Parmesan cheese', 'fruit':'Apples'},
    {'name':'Lamb','protein':'LAMB: \n 1 leg of lamb \n rosemary \n thyme \n olive oil \n salt and pepper \n 7spices \n \n METHOD: \n Preheat oven to 180, put the leg of lamb on a tray, add the 7 spices, \n salt and pepper, olive oil and rub, bake for 2 hours.\n', 'cheese':'Brie cheese', 'fruit':'Pears'},
    {'name':'Lasagna','protein':'LASAGNA: \n 500g minced meat \n 1can tomato sauce \n 500g Lasagna sheets \n Mozzarella cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Fry oil with onion and garlic, add seasoned minced meat, when meat \n is done add tomato sauce, cook for 20 minutes, add water if \n needed, get a tray, add a layer of sauce, cheese and lasagna sheets, \n repeat untill you reach the top of the tray, bake for 40min at 180°.\n', 'cheese':'Manchego cheese', 'fruit':'Cherries'},
    {'name':'BBQ','protein':'BBQ: \n Beef \n sausages \n Charcoal \n Salt and pepper \n \n METHOD: \n light up the charcoal, season the beef with salt and pepper, \n grill the meat and sausages.\n', 'cheese':'Cheddar cheese', 'fruit':'Plums'},
    {'name':'Seafood','protein':'SEAFOOD: \n 500g of mixed seafood \n 1 lemon or lime \n 100g butter \n salt and pepper \n 2 cloves of garlic \n \n METHOD: \n Add butter and garlic to a frying pan, season seafood \n with salt and pepper, fry for 6 minutes.\n', 'cheese':'Feta cheese', 'fruit':'Watermelon'}
]




# Wine.welcome()
# clearing.clear()

# def app_options():
#     options = ["I want to try another wine (Use Arrow Keys ↑ ↓)", "I want to exit the app (Use Arrow Keys ↑ ↓)"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     if options[menu_entry_index] == options[0]:
#         clearing.clear()
#         print(wine_questions())
#     else:
#         print(bottle)





# def wine_questions():
#     input_message = input("What type of red wine do you have in mind (Please enter full item name)? ")
#     wine_input = input_message
#     wine_validation = Wine.is_valid_wine(wine_input)
#     if wine_validation:
#         clearing.clear()
#         print(f"{wine_input} goes well with the foods bellow, choose one for Recipe! (Use Arrow Keys ↑ ↓)")
#         for pair in pairing:
#             if wine_input == pair['type']:
#                     food_options = [pair['protein'], pair['cheese'], pair['fruit']]
#                     terminal_menu = TerminalMenu(food_options)
#                     menu_entry_index = terminal_menu.show()
#                     for item in recipe:
#                         if food_options[menu_entry_index] == pair['protein']:
#                             clearing.clear()
#                             if pair['protein'] == item['name']:
#                                 print(item['protein'])
#                                 app_options()
#                         elif food_options[menu_entry_index] == pair['cheese']:
#                             clearing.clear()
#                             if pair['cheese'] == item['cheese']:
#                                 print(item['cheese'])
#                                 app_options()
#                         else:
#                             clearing.clear()
#                             print(item['fruit'])
#                             app_options()
#     else:
#         print(f"{wine_input} it is not a valid wine!")
#         print(app_options())

# wine_questions()

#REFACTOR
#________________________________________________________________________________

# PSEUDOCODE:
# 0.The app has 3 lists: 
# __available__wines with 10 available wine types.
# pairing with 4 items, type, protein, cheese, fruit.
# recipe with 4 items, name, protein, cheese, fruit 
# 1. Welcome function welcomes the user and prompts the user to press enter to start.
# 2.wine_questions function asks for a user input with the name of the wine:
# 3.the class method is_valid_wine checks to see if the user input is available in 
# the list of __available__wines, returning a True or False Boolean.
# 4.if the is_valid_wine is True the app returns a list with options of foods that pair with that wine from the pairing list of items.
# 5.if the is_valid_wine is False the app returns app_options function with a list with 2 options asking if the user wants to try
# a different wine or exit the app.
# 6.Once the user picks a food option from the list, the app then checks if the item protein from the pairing list matches the item 
# protein from the recipe list and it returns a recipe for that item from the recipe list.
# 7.Then the function app_options presents a list with 2 options asking if the user wants to try a different wine or exit the app.
# 8.When the user chooses to try another wine the wine_questions function is run again.
# 9.When the user chooses to exit the app an ASCII file with a bottle of wine and glasses is shown on the Screen with a thank you and a
# do not drink and drive message.

# LIST OF FUNCTIONS FIRST:
# welcome()
# wine_questions()
# is_valid_wine()
# app_options()

# LIST OF FUNCTIONS NOW:
# welcome()
# wine_validation()
# pairing()
# recipe()
# is_valid_wine()
# app_options()
Wine.welcome()
clearing.clear()

input_message = input("What type of red wine do you have in mind (Please enter full item name)? ")
wine_input = input_message
wine_validation = Wine.is_valid_wine(wine_input)

def wine_validation():
    if wine_validation:
        clearing.clear()
        print(f"{wine_input} goes well with the foods bellow, choose one for Recipe! (Use Arrow Keys ↑ ↓)")
        return wine_input
    else:
        print(f"{wine_input} it is not a valid wine!")
        print(app_options())

def app_options():
    options = ["I want to try another wine (Use Arrow Keys ↑ ↓)", "I want to exit the app (Use Arrow Keys ↑ ↓)"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == options[0]:
        clearing.clear()
        print(wine_validation())
    else:
        print(bottle)

def pair_list_iteration():
    for pair in pairing:
        if wine_input == pair['type']:
            food_options = [pair['protein'], pair['cheese'], pair['fruit']]
            terminal_menu = TerminalMenu(food_options)
            menu_entry_index = terminal_menu.show()
            print(food_options[menu_entry_index])
        


def recipe_list_iteration():
    for item in recipe:
        if pair_list_iteration() == pair['protein']:
            clearing.clear()
            if pair['protein'] == item['name']:
                print(item['protein'])
                app_options()
        elif pair_list_iteration() == pair['cheese']:
            clearing.clear()
            if pair['cheese'] == item['cheese']:
                print(item['cheese'])
                app_options()
        else:
            clearing.clear()
            print(item['fruit'])
            app_options()

wine_validation()
# pairing()
recipe_list_iteration()













