from classes.greetings import Greetings
from classes.wine import Wine
from classes.pair import Pair
from classes.recipe import Recipe
from simple_term_menu import TerminalMenu
import clearing
import cowsay


cabernet_sauvignon_pair = Pair('Cabernet Sauvignon', 'Roast beef', 'Gouda cheese', 'Plums')
pinot_noir_pair = Pair('Pinot Noir', 'Salmon', 'Gruyere cheese', 'Apples')
shiraz_pair = Pair('Shiraz', 'Duck', 'Pecorino cheese', 'Apricot')
merlot_pair = Pair('Merlot', 'Pork', 'Camembert cheese', 'Figs')
sangiovese_pair = Pair('Sangiovese', 'Spaghetti Bolognese', 'Mozzarella cheese', 'Strawberry')
chianti_pair = Pair('Chianti', 'Pizza', 'Parmesan cheese', 'Apples')
bordeaux_pair = Pair('Bordeaux', 'Lamb', 'Brie cheese', 'Pears')
tempranillo_pair = Pair('Tempranillo', 'Lasagna', 'Manchego cheese', 'Cherries')
carmenere_pair = Pair('Carmenere', 'BBQ', 'Cheddar cheese', 'Plums')
rose_pair = Pair('Rose', 'Seafood', 'Feta cheese', 'Watermelon')

pair_list = [
    cabernet_sauvignon_pair,
    pinot_noir_pair,
    shiraz_pair,
    merlot_pair,
    sangiovese_pair,
    chianti_pair,
    bordeaux_pair,
    tempranillo_pair,
    carmenere_pair,
    rose_pair
]





# print(pinot_noir_pair.wine)
# print(pinot_noir_pair.main_dish)
# print(pinot_noir_pair.cheese)
# print(pinot_noir_pair.fruit)



cabernet_sauvignon_recipe = Recipe('Cabernet Sauvignon', '\n ROAST BEEF: \n 500g of beef \n 100g of butter \n Salt and Pepper to taste \n \n METHOD: \n Put the beef on a tray, rub butter salt and pepper all over, \n put it in the oven at 180° for 1hour.\n', '\n CHEESE BOARD: \n Gouda cheese \n Prosciutto \n Walnuts \n ', '\n DESSERT: \n Plums \n Honey \n Cream \n')
pinot_noir_recipe = Recipe('Pinot Noir', '\n SALMON: \n 2 Slices of Salmon \n 100g of Butter \n Salt and pepper to taste \n Italian herbs \n \n METHOD: \n Season the fish with salt, pepper and herbs, \n add butter to a frying pan, cook both sides of \n the fish untill preferred level of doneness.\n', '\n CHEESE BOARD: \n Gruyere cheese \n Bacon \n Almonds \n', '\n DESSERT: \n Apples \n Brown Sugar \n Cinammon \n')
shiraz_recipe = Recipe('Shiraz', '\n DUCK: \n 200g Duck Breasts \n 2tb of Olive Oil \n 1 Clove of garlic \n Lemon Pepper, Salt, to taste \n \n METHOD: \n Preheat oven to 180°, season the breasts with salt, \n Pepper and garlic, add Olive Oil to a frying pan, \n cook both sides untill brown, finish cooking for another 20min in the oven.\n', '\n CHEESE BOARD: \n Pecorino cheese \n Ricotta \n Ham \n', '\n DESSERT: \n Apricot \n Tahini \n Attar \n Pistachios \n')
merlot_recipe = Recipe('Merlot', '\n PORK: \n 1 Pork Leg \n Salt Pepper \n Aluminium Foil \n Oil \n \n METHOD: \n Get a Tray, add the pork leg, rub salt and pepper, \nadd oil for the crackling, roll aluminium foil around \n the tray, bake at 180° for 2 hours.\n', '\n CHEESE BOARD: \n Camembert cheese \n Cashew Nuts \n Olive Oil \n', '\n DESSERT: \n Figs \n Brown Sugar \n Lemon Juice \n Zest \n Cream or Icecream \n')
sangiovese_recipe = Recipe('Sangiovese', '\n SPAGHETTI BOLOGNESE: \n 500g minced meat \n 1 can tomato sauce \n 500g Spaghetti \n Parmesan cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Cook spaghetti pasta in salty boiling water, \n fry oil with onion and garlic, add seasoned minced meat, \n when meat is done add tomato sauce, cook for 20 minutes, \n add water if needed, mix it with the pasta, add some parmesan, enjoy.\n', '\n CHEESE BOARD: \n Mozzarella cheese \n Jam \n Brazil Nuts \n', '\n DESSERT: \n Strawberry \n Condensed Milk \n')
chianti_recipe = Recipe('Chianti', '\n PIZZA: \n 1 Sliced Pepperoni sausage \n mozzarella cheese \n tomato sauce \n pizza base \n oregano \n \n METHOD: \n preheat oven to 180, get a tray, put the pizza base, \n spread tomato sauce, add cheese, add sliced pepperoni, \n add oregano, bake for 10 to 20 minutes.\n', '\n CHEESE BOARD: \n Parmesan cheese \n Pepperoni \n Brown Sugar \n', '\n DESSERT: \n Apples \n Brown Sugar \n Cinammon \n')
bordeaux_recipe = Recipe('Bordeaux', '\n LAMB: \n 1 leg of lamb \n rosemary \n thyme \n olive oil \n salt and pepper \n 7spices \n \n METHOD: \n Preheat oven to 180, put the leg of lamb on a tray, add the 7 spices, \n salt and pepper, olive oil and rub, bake for 2 hours.\n', '\n CHEESE BOARD: \n Brie cheese \n Truffles \n Peanuts \n', '\n DESSERT: \n Pears \n Maple Syrup \n Macadamia Nuts \n')
tempranillo_recipe = Recipe('Tempranillo', '\n LASAGNA: \n 500g minced meat \n 1can tomato sauce \n 500g Lasagna sheets \n Mozzarella cheese \n oil \n 1 onion \n 1 clove of Garlic \n salt pepper \n \n METHOD: \n Fry oil with onion and garlic, add seasoned minced meat, when meat \n is done add tomato sauce, cook for 20 minutes, add water if \n needed, get a tray, add a layer of sauce, cheese and lasagna sheets, \n repeat untill you reach the top of the tray, bake for 40min at 180°.\n', '\n CHEESE BOARD: \n Manchego cheese \n Jamon \n Toasted Sunflower Seeds \n', '\n DESSERT: \n Cherries \n Cream \n Honey \n')
carmenere_recipe = Recipe('Carmenere', '\n BBQ: \n Beef \n sausages \n Charcoal \n Salt and pepper \n \n METHOD: \n light up the charcoal, season the beef with salt and pepper, \n grill the meat and sausages.\n', '\n CHEESE BOARD: \n Cheddar cheese \n Smoked Almonds \n Barbecue Sauce \n', '\n DESSERT: \n Plums \n Maple Syrup \n')
rose_recipe = Recipe('Rose', '\n SEAFOOD: \n 500g of mixed seafood \n 1 lemon or lime \n 100g butter \n salt and pepper \n 2 cloves of garlic \n \n METHOD: \n Add butter and garlic to a frying pan, season seafood \n with salt and pepper, fry for 6 minutes.\n', '\n CHEESE BOARD: \n Feta cheese \n Anchovies \n Tzatziki Sauce \n', '\n DESSERT: \n Watermelon \n does not need anything else \n')

recipe_list = [
    cabernet_sauvignon_recipe,
    pinot_noir_recipe,
    shiraz_recipe,
    merlot_recipe,
    sangiovese_recipe,
    chianti_recipe,
    bordeaux_recipe,
    tempranillo_recipe,
    carmenere_recipe,
    rose_recipe
]

# print(recipe_list[1].main_dish)
# exit()

# print(pinot_noir_recipe.wine)
# print(pinot_noir_recipe.main_dish)
# print(pinot_noir_recipe.cheese_board)
# print(pinot_noir_recipe.dessert)


Greetings.welcome()
clearing.clear()

input_message = input("What type of red wine do you have in mind (Please enter full item name)? ")
user_wine = Wine(input_message)
is_wine_valid = user_wine.is_valid_wine()

def reset_state():
    input_message = None
    is_wine_valid = None

def wine_validation():
    if is_wine_valid:
        clearing.clear()
        print(f"{input_message} goes well with the foods bellow, choose one for Recipe! (Use Arrow Keys ↑ ↓)")
        return input_message
    else:
        print(f"{input_message} it is not a valid wine!")
        print(app_options())

def app_options():
    options = ["I want to try another wine (Use Arrow Keys ↑ ↓)", "I want to exit the app (Use Arrow Keys ↑ ↓)"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == options[0]:
        clearing.clear()
        reset_state()
    else:
        Greetings.end()

def pair_list_iteration():
    for i in range(len(pair_list)):
        if input_message == pair_list[i].wine:
            food_options = [pair_list[i].main_dish, pair_list[i].cheese, pair_list[i].fruit]
            terminal_menu = TerminalMenu(food_options)
            menu_entry_index = terminal_menu.show()
            for item in range(len(recipe_list)):
                if food_options[menu_entry_index] == pair_list[i].main_dish:
                    clearing.clear()
                    if pair_list[i].wine == recipe_list[item].wine:
                        print(recipe_list[item].main_dish)
                        app_options()
                elif food_options[menu_entry_index] == pair_list[i].cheese:
                    clearing.clear()
                    if pair_list[i].wine == recipe_list[item].wine:
                        print(recipe_list[item].cheese_board)
                        app_options()
                elif food_options[menu_entry_index] == pair_list[i].fruit:
                    clearing.clear()
                    if pair_list[i].wine == recipe_list[item].wine:
                        print(recipe_list[item].dessert)
                        app_options()

wine_validation()
pair_list_iteration()

# for i in range(len(pair_list)):
#     print(pair_list[i].wine)
# exit()












