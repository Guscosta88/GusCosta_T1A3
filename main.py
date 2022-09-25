# classes where imported from the classes folder:
from classes.greetings import Greetings
from classes.wine import Wine
from classes.pair import Pair
from classes.recipe import Recipe

# packages py imported:
from simple_term_menu import TerminalMenu
import clearing
import cowsay

# Wine_list items:
# Every item of the wine_list is contained within the Pair class, which includes the self, wine, main, cheese and fruit attributes.
# The wine item inside of the Pair class is handled within the Wine class which includes self, name.
# Every Recipe item inside of the Pair class is handled within the Recipe class which includes self, name, description and recipe_type.
# Every class needed is imported within the main.py file.
# Each variable name contains all of this data and makes it easy to be accessed.

cabernet_sauvignon = Pair(
Wine('Cabernet sauvignon'),
Recipe(
'Roast beef',
'''
ROAST BEEF:
500g of beef 
100g of butter
Salt and Pepper to taste

METHOD: 
Put the beef on a tray, rub butter salt and pepper all over, 
put it in the oven at 180° for 1hour.

''',
'main'
),
Recipe(
'Gouda cheese',
'''
CHEESE BOARD: 
Gouda cheese 
Prosciutto 
Walnuts

''',
'cheese'
),
Recipe(
'Plums',
'''
DESSERT:
Plums
Honey
Cream

''',
'fruit'
)
)

pinot_noir = Pair(
Wine('Pinot noir'),
Recipe(
'Salmon', 
 '''
 SALMON:
 2 Slices of Salmon
 100g of Butter 
 Salt and pepper to taste
 Italian herbs
 
 METHOD:
 Season the fish with salt, pepper and herbs, 
 add butter to a frying pan, cook both sides of the
 fish untill preferred level of doneness.
 
 ''',
 'main'
),
Recipe(
'Gruyere cheese', 
 '''
 CHEESE BOARD:
 Gruyere cheese
 Bacon
 Almonds
 
 ''',
 'cheese'
 ),
 Recipe(
'Apples',
'''
DESSERT:
Apples
Brown Sugar
Cinammon

''',
'fruit'
)
)

shiraz = Pair(
Wine('Shiraz'),
Recipe(
'Duck', 
'''
DUCK:
200g Duck Breasts
2tb of Olive Oil
1 Clove of garlic
Lemon Pepper, Salt, to taste

METHOD:
Preheat oven to 180°, season the breasts with salt, 
Pepper and garlic, add Olive Oil to a frying pan,
cook both sides untill brown, finish cooking for 
another 20min in the oven.

''',
'main'
),
Recipe(
'Pecorino cheese', 
'''
CHEESE BOARD:
Pecorino cheese
Ricotta
Ham

''',
'cheese'
),
Recipe(
'Apricot',
'''
DESSERT:
Apricot
Tahini
Attar
Pistachios

''',
'fruit'
)
)

merlot = Pair(
Wine('Merlot'), 
Recipe(
'Pork', 
'''
PORK:
1 Pork Leg
Salt Pepper
Aluminium Foil
Oil

METHOD:
Get a Tray, add the pork leg, rub salt and pepper, 
add oil for the crackling, roll aluminium foil around
the tray, bake at 180° for 2 hours.

''',
'main'
),
Recipe(
'Camembert cheese', 
'''
CHEESE BOARD:
Camembert cheese
Cashew Nuts
Olive Oil

''',
'cheese'
),
Recipe(
'Figs',
'''
DESSERT:
Figs
Brown Sugar
Lemon Juice
Zest
Cream or Icecream

''',
'fruit'
)
)

sangiovese = Pair(
Wine('Sangiovese'), 
Recipe(
'Spaghetti Bolognese', 
'''
SPAGHETTI BOLOGNESE:
500g minced meat
1 can tomato sauce
500g Spaghetti
Parmesan cheese
oil
1 onion
1 clove of Garlic
salt pepper

METHOD:
Cook spaghetti pasta in salty boiling water,
fry oil with onion and garlic, add seasoned minced meat,
when meat is done add tomato sauce, cook for 20 minutes, 
add water if needed, mix it with the pasta, add some parmesan, enjoy.

''',
'main'
),
Recipe(
'Mozzarella cheese',
'''
CHEESE BOARD:
Mozzarella cheese
Jam
Brazil Nuts

''',
'cheese'
),
Recipe(
'Strawberry', 
'''
DESSERT:
Strawberry
Condensed Milk

''',
'fruit'
)
)


chianti = Pair(
Wine('Chianti'), 
Recipe(
'Pizza', 
'''
PIZZA:
1 Sliced Pepperoni sausage
mozzarella cheese
tomato sauce
pizza base 
oregano

METHOD:
preheat oven to 180, get a tray, put the pizza base,
spread tomato sauce, add cheese, add sliced pepperoni,
add oregano, bake for 10 to 20 minutes.

''',
'main'
),
Recipe(
'Parmesan cheese',
'''
CHEESE BOARD:
Parmesan cheese
Pepperoni
Brown Sugar

''',
'cheese'
),
Recipe(
'Apples',
'''
DESSERT:
Apples
Brown Sugar
Cinammon

''',
'fruit'
)
)

bordeaux = Pair(
Wine('Bordeaux'), 
Recipe(
'Lamb',             
'''
LAMB:
1 leg of lamb
rosemary
thyme
olive oil
salt and pepper
7spices

METHOD:
Preheat oven to 180, put the leg of lamb on a tray, add the 7 spices,
salt and pepper, olive oil and rub, bake for 2 hours.

''',
'main'
),
Recipe(
'Brie cheese',
'''
CHEESE BOARD:
Brie cheese
Truffles
Peanuts

''',
'cheese'
),
Recipe(
'Pears',  
'''
DESSERT:
Pears
Maple Syrup
Macadamia Nuts

''',
'fruit'
)
)

tempranillo = Pair(
Wine('Tempranillo'), 
Recipe(
'Lasagna', 
''' 
LASAGNA:
500g minced meat
1can tomato sauce
500g Lasagna sheets
Mozzarella cheese
oil
1 onion
1 clove of Garlic
salt pepper

METHOD:
Fry oil with onion and garlic, add seasoned minced meat, when meat
is done add tomato sauce, cook for 20 minutes, add water if
needed, get a tray, add a layer of sauce, cheese and lasagna sheets,
repeat untill you reach the top of the tray, bake for 40min at 180°.

''',
'main'
),
Recipe(
'Manchego cheese',
'''
CHEESE BOARD:
Manchego cheese
Jamon
Toasted Sunflower Seeds

''',
'cheese'
),
Recipe(
'Cherries',
'''
DESSERT:
Cherries
Cream
Honey

''',
'fruit'
)
)

carmenere = Pair(
Wine('Carmenere'), 
Recipe(
'BBQ', 
'''
BBQ:
Beef
sausages
Charcoal
Salt and pepper

METHOD:
light up the charcoal, season the beef with salt and pepper,
grill the meat and sausages.

''',
'main'
),
Recipe(
'Cheddar cheese',
'''
CHEESE BOARD:
Cheddar cheese
Smoked Almonds
Barbecue Sauce

''',
'cheese'
),
Recipe(
'Plums',
'''
DESSERT:
Plums
Maple Syrup

''',
'fruit'
)
)

rose = Pair(
Wine('Rose'), 
Recipe(
'Seafood', 
'''
SEAFOOD:
500g of mixed seafood
1 lemon or lime
100g butter
salt and pepper
2 cloves of garlic

METHOD:
Add butter and garlic to a frying pan, season seafood
with salt and pepper, fry for 6 minutes.

''',
'main'
),
Recipe(
'Feta cheese',
'''
CHEESE BOARD:
Feta cheese
Anchovies
Tzatziki Sauce

''',
'cheese'
),
Recipe(
'Watermelon',
'''
DESSERT:
Watermelon
does not need anything else

''',
'fruit'
)
)

# The wine_list is a list with the set variables that handles the data of each item within the classes.

wine_list = [
    cabernet_sauvignon,
    pinot_noir,
    shiraz,
    merlot,
    sangiovese,
    chianti,
    bordeaux,
    tempranillo,
    carmenere,
    rose
]


# The welcome method is a method of the Greetings class that displays the app Logo, 
# designed with ASCII, and prompts the user to press Enter to start the app.
# it is the first method to be called.

Greetings.welcome()

# The wine_qty_error_handling function receives a qty_message parameter with the result of the answer to the 
# question "how many wines do you want to check?", and if the answer it is not an integer it keeps 
# asking untill the user inputs an integer.

def wine_qty_error_handling(qty_message):
    clearing.clear()
    input_number = None
    while True:
        try:
            input_number = int(input(qty_message))
            break
        except:
            clearing.clear()
            print('must be an integer')
            
# The init function displays an input question for the user asking for a wine name.
# It forces the first letter to be capitalized with the capitalize function.
# Once the user enters an input, it is saved in the input_message variable and checked in the list
# of available wines within the Wine class, a Boolean value is returned and stored in the is_wine_valid variable 
# the function sends it to the wine_validation function alongside the input_message variable.

def init():
    clearing.clear()
    input_message = input("What type of red wine do you have in mind (Please enter full item name)? ").capitalize()
    user_wine = Wine(input_message)
    is_wine_valid = user_wine.is_valid_wine()
    wine_validation(is_wine_valid, input_message)

    
# The build_menu function uses the py package simple_term_menu to create an interactive terminal menu 
# and it holds two parameters, an options parameters that receives a variable from a chosen option, 
# and the return_string parameter that is set as True by default.
# if a string is returned the return_string parameter is set as True and a list of menu options coming from another function is shown, 
# if it is false it returns one item from the menu.

def build_menu(options, return_string = True):
    menu = TerminalMenu(options)
    menu_entry_index = menu.show()
    if return_string:
        return options[menu_entry_index]
    else:
        return menu_entry_index

# The wine_validation function receives the is_wine_valid, input_message parameters and if the Boolean of the is_wine_valid equals to 
# True it returns a message with the wine name alongside the pair_list_iteration showing three options of food that pair with that wine 
# to be chosen.
# if the Boolean of the is_wine_valid equals to False, it returns the input_message and an it is not a valid wine message, alongside the 
# app_options function that prompts the user to choose between 2 options, to either try another wine or leave the app.


def wine_validation(is_wine_valid, input_message):
    if is_wine_valid:
        clearing.clear()
        print(f"{input_message} goes well with the foods bellow, choose one for Recipe! (Use Arrow Keys ↑ ↓)")
        pair_list_iteration(input_message)
    else:
        clearing.clear()
        print(f"{input_message} it is not a valid wine!")
        app_options()


# The app_options function has a variable called options that holds two strings with questions, prompting the user to choose
# betweeen leaving the app or chosing a different wine, an index variable calls the build_menu function and sends an options parameter
# and a boolean False returning the two options as prompts to e selected, if he chooses the option to try another wine the init function 
# is called again, if he chooses to leave the app the end method is called prompting a goodbye message.

def app_options():
    options = ["I want to try another wine (Use Arrow Keys ↑ ↓)", "I want to exit the app (Use Arrow Keys ↑ ↓)"]
    index = build_menu(options, False)
    if index == 0:
        init()
    else:
        Greetings.end()

# The cowsay_items function holds a parameter called cowsay_check that receives the chosen recipe name from the pair_list_iteration 
# and it returns a cowsay item from the cowsay py package.
# If the item chosen was Pork it returns the pig cowsay, if it was the Roast beef it returns the cow, 
# if it was the Duck it returns the turkey, and if it was none it returns the T-rex.

def cowsay_items(cowsay_check):
    if cowsay_check == 'Pork':
        cowsay.pig('Merlot and Pork are best friends!')
    elif cowsay_check == 'Roast beef':
        cowsay.cow('You cant go wrong with Roast Beef and Cabernet!')
    elif cowsay_check == 'Duck':
        cowsay.turkey('Shiraz goes with any Poultry!')
    else:
        cowsay.trex('No wine is old enough to Pair with a T-Rex!')


# The pair_list_iteration function is the main logic of the app and it is where the input 
# from the user is checked against the wine_list items and values from the wine_list are returned.
# A for loop iterates in the wine_list, and if the input_message variable that carries the input from the user matches the 
# wine name from the Wine class within the Pair class in the wine_list item and also if the item from the wine_list also matches 
# the wine attribute within the Pair class it returns a list with 3 options, one option for main dish, one option for cheese, 
# and one option for fruit, these options are stored in a list called menu_options, this list is then send to the build_menu function 
# and displayed to the user to choose from, once the user chooses one of the three, the selection than goes to another set of conditionals
# where it is checked against the pair class attributes and if the main dish name equals to the main dish selected it returns the 
# recipe description the same happens for cheese and fruit.
# this result is also checked against the cowsay_items function to return the cowsay message.
# The goal of the app is to show food options that pair with the wine that the user chose, so this concludes the app's purpose.
# after that the user can choose to remain in the app and try another wine or leave the app and receive a thank you, do 
# not drink and drive message.


def pair_list_iteration(input_message):
    for pair in wine_list:
        if input_message == pair.wine.name if pair and pair.wine else None:
            menu_options = [
                pair.main_dish.name if pair and pair.main_dish else None,
                pair.cheese.name if pair and pair.cheese else None,
                pair.fruit.name if pair and pair.fruit else None
            ]
            menu_selected = build_menu(menu_options)

            if pair.main_dish.name == menu_selected:
                clearing.clear()
                print(pair.main_dish.description)
                cowsay_check = pair.main_dish.name
                cowsay_items(cowsay_check)
            elif pair.cheese.name == menu_selected:
                clearing.clear()
                print(pair.cheese.description)
                cowsay.cheese('Cheese goes well with any wine!')
            else:
                clearing.clear()
                print(pair.fruit.description)

            app_options()

wine_qty_error_handling("How many wines do you want to check? ")
init()














