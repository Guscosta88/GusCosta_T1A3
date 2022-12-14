# **GusCosta_T1A3**

# T1A3 - Terminal Application

Click [here](https://www.pythonanywhere.com/shared_console/428b4346-f536-42ef-b44f-295213d890d1) To open App on Python anywhere host.

Click [here](https://github.com/Guscosta88/GusCosta_T1A3) To open Github Repo.

Click [here](https://youtu.be/KRXxx8xaYpE) Part 01 - Slide Deck presentation.

Click [here](https://youtu.be/Cj6-mNZGvfw) Part 02 - Slide Deck presentation - App Running.

Click [here](https://youtu.be/dUEsWa-8rNI) Part 03 - Slide Deck presentation - Code Explained.

------

# **Purpose:**

#### **What does the app do?**

- It takes an user input with the name of a type of wine and it returns food options and recipes that pair with it.

#### **What problem does it solve?**

- It allows the user to acquire knowledge about the different types of wine and the foods that goes with it.

#### **what is the main goal?**

- To show that anyone, after using the app, can buy a bottle of wine, cook food that pairs with it and enjoy the little things in life.

#### **Identify any code style guide or styling conventions that the application will adhere to.**

- The Python convention chosen to be applied in this application is the PEP 8 – Style Guide for Python Code, as it implies conventions, standards and good practices that contribute to a reliable, clear and inclusive code, which helps to avoid any confusion that might happen when someone other than the code's creator reads it.

Click [here](https://peps.python.org/pep-0008/) To open the link to PEP 8 – Style Guide for Python Code.



# **Functionality / features:**


#### **Wine_list, Wine class, Pair class, Recipe class:**

- The wine_list is a list with set variables that handles the data of each item within the classes.
  Every item of the wine_list is contained within the Pair class, which includes the self, wine, main, cheese and fruit attributes.
  The wine item inside of the Pair class is handled within the Wine class which includes self, name.
  Every Recipe item inside of the Pair class is handled within the Recipe class which includes self, name, description and recipe_type.
  Every class needed is imported within the main.py file.
  Each variable name contains all of this data and makes it easy to be accessed.

#### **Greetings class, welcome method, end method:**

- The Class Greetings holds two methods: 
  The welcome method that displays the ASCII file with the app's logo imported from the constant logo.py file and prompts the user to press enter to start.
  The end method that clears any remaining data with the help of the clearing py package, displays the ASCII bottle art imported from 
  the constant bottle.py file with a thank you and a Do not drink and drive message to be displayed when the user is done using the app.

#### **Init Function:**

- The init function displays an input question for the user asking for a wine name.
  It forces the first letter to be capitalized with the capitalize function.
  Once the user enters an input, it is saved in the input_message variable and checked in the list
  of available wines within the Wine class, a Boolean value is returned and stored in the is_wine_valid variable 
  the function sends it to the wine_validation function alongside the input_message variable.

#### **build_menu function:**

- The build_menu function uses the py package simple_term_menu to create an interactive terminal menu 
  and it holds two parameters, an options parameters that receives a variable from a chosen option, 
  and the return_string parameter that is set as True by default.
  if a string is returned the return_string parameter is set as True and a list of menu options coming from another function is shown, 
  if it is false it returns one item from the menu.

#### **pair_list_iteration function:**

- The pair_list_iteration function is the main logic behind the app and it is where the input 
  from the user is checked against the wine_list items, after passing through all of the other functions and the values from the wine_list are returned.
  A for loop iterates within the wine_list, and if the input_message variable that carries the input from the user matches the 
  wine name from the Wine class within the Pair class in the wine_list item and also if the item from the wine_list also matches 
  the wine attribute within the Pair class, it returns a list with 3 options, one option for main dish, one option for cheese, 
  and one option for fruit, these options are stored in a list called menu_options, this list is then send to the build_menu function 
  and displayed to the user to choose from, once the user chooses one of the three, the selection than goes to another set of conditionals
  where it is checked against the pair class attributes and if the main dish name equals to the main dish selected it returns the 
  recipe description, the same happens for cheese and fruit.
  this result is also checked against the cowsay_items function to return the cowsay message.
  The goal of the app is to show food options that pair with the wine that the user chose, so this concludes the app's purpose.
  after that the user can choose to remain in the app and try another wine or leave the app and receive a thank you, do 
  not drink and drive message.

#### **cowsay_items function:**

- The cowsay_items function holds a parameter called cowsay_check that receives the chosen recipe name from the pair_list_iteration 
  and it returns a cowsay item from the cowsay py package.
  If the item chosen was Pork it returns the pig cowsay, if it was the Roast beef it returns the cow, 
  if it was the Duck it returns the turkey, and if it was none it returns the T-rex.

------

# **Error Handling Functions:**

#### **wine_qty_error_handling**
- The wine_qty_error_handling function receives a qty_message parameter with the user input that answers the question "how many wines do you want to check?", it also uses a while loop and try/except statements, if the answer it is not an integer it keeps asking untill the user inputs an integer.

#### **wine_validation function(Error handling, it handles an input different then the available in the list of wines):**

- The wine_validation function receives the is_wine_valid, input_message parameters and if the Boolean of the is_wine_valid equals to 
  True it returns a message with the wine name alongside the pair_list_iteration showing three options of food that pair with that wine 
  to be chosen.
  if the Boolean of the is_wine_valid equals to False, it returns the input_message and an it is not a valid wine message, alongside the 
  app_options function that prompts the user to choose between 2 options, to either try another wine or leave the app.

#### **app_options function(Error Handling, it gives the user options if the input was invalid):**

- The app_options function has a variable called options that holds two strings with questions, prompting the user to choose
  betweeen leaving the app or chosing a different wine, an index variable calls the build_menu function and sends an options parameter
  and a boolean False returning the two options as prompts to be selected, if he chooses the option to try another wine the init function 
  is called again, if he chooses to leave the app, the end method is called prompting a goodbye message.

------

# **Testing - Automated unit testing with pytest**

#### **test_initial_pair_value**
- The test_initial_pair_value test function makes sure that the pair list 
  items are run properly within the class through the correct attributes 
  to return the correct pair values.
  pytest package was installed, the Pair class was imported.
  This test was run with the command: 
  pytest classes/test_pair.py
  
![test_initial_pair_value](./images/test_initial_pair_value.jpg)

#### **test_no_pair_value**
- The test_no_pair_value test function raises an exception which means that 
  the next block of code will be tested and if no exception is raised between 
  pair and Pair() the test passes, otherwise it fails.
  pytest package was installed, the Pair class was imported.
  This test was run with the command: 
  pytest classes/test_pair.py 

![test_no_pair_value](./images/test_no_pair_value.jpg)

#### **test_pair**
- The test_pair program functions run together.
  pytest package was installed, the Pair class was imported.
  This test was run with the command: 
  pytest classes/test_pair.py

![test_pair](./images/test_pair.jpg)

#### **test_initial_recipe_value**
- The test_initial_recipe_value test function makes sure that the recipe list 
  items are run properly within the class through the correct attributes to 
  return the correct recipe values.
  pytest package was installed, the Recipe class was imported.
  This test was run with the command: 
  pytest classes/test_recipe.py 

![test_initial_recipe_value](./images/test_initial_recipe_value.jpg)

#### **test_no_recipe_value**
- The test_no_recipe_value test function raises an exception which means that the next block of code will be tested and if no exception
  is raised between recipe and Recipe() the test passes, otherwise it fails.
  pytest package was installed, the Recipe class was imported.
  This test was run with the command: 
  pytest classes/test_recipe.py 

![test_no_recipe_value](./images/test_no_recipe_value.jpg)

#### **test_recipe**
- The test_recipe program functions run together.
  pytest package was installed, the Recipe class was imported.
  This test was run with the command: 
  pytest classes/test_recipe.py

![test_recipe](./images/test_recipe.jpg)

------

# **A General break down of the app's functionalities:**

### **1. Welcome method welcomes the user and prompts the user to press enter to start.**

![Welcome](./images/welcome.jpg)

### **2. wine_qty_error_handling function asks for a number input with the quantity of wines to be searched:**

![wine_qty_error_handling](./images/wine_qty_error_handling.jpg)

### **3. init function asks for a user input with the name of the wine:**

![What_type_of_wine](./images/what_type_of_wine.jpg)

### **4. The class method is_valid_wine checks to see if the user input is available in the list of __available__wines, returning a True or False Boolean.**
### **5. If the is_valid_wine is True the app returns a list with options of foods that pair with that wine.**

![Foods](./images/foods.jpg)


### **6. If the is_valid_wine is False the app returns app_options function with a list with 2 options asking if the user wants to try a different wine or exit the app.**

![Not_valid](./images/not_valid.jpg)

### **7. Once the user picks a food option from the list, the app then checks if the item name matches the selected item and it returns a recipe for that item.**
### **8. Then the function app_options presents a list with 2 options asking if the user wants to try a different wine or exit the app.**

![recipe_cowsay](./images/recipe_cowsay.jpg)


### **9. When the user chooses to try another wine the init function runs again.**
### **10. When the user chooses to exit the app an ASCII file with a bottle of wine and glasses is shown on the Screen with a thank you and a do not drink and drive message.**

![End](./images/end.jpg)

### **11. The Python packages used in this application are:**

- Simple_term_menu:
    It creates an interactive menu in the terminal with the option to use arrow keys as selectors.
    
- Clearing
    It clears the terminal from past entries and outputs.

- Cowsay
    it returns different drawings of characters or animals with a message.

- Colorterminal
    it adds collor to the terminal items.

- Pytest
    Used for testing.

# **Flow Chart**

![Flowchart](./images/T1A3_flowchart.svg)


# **Implementation Plan**

## **Day One:**

- My first idea was to make a drawing app, but due to the GUI package constraints the educators decided that would be best to change, this is when I came up with the idea of building a wine and food pairing app where I could iterate 2 lists and match them for the outcome.
- The first day I spent creating a Trello board and refining my idea trying to decide which way to go to implement it and which features to include:

![Day One](./images/trello_board_day_one.jpg)

## **Day Two:**

- Day two I spent mostly organizing the lists of wine, and recipes trying to think what features to build and the best way to organize it to be easy to interact with it.

![Day Two](./images/trello_board_day_two.jpg)

## **Day Three:**

- As I was implementing little bits of the code and testing what would work I started to have a clearer idea of the features. I was able to write a rough logic that was already working from start to finish, but not DRY and with a lot of room for improvement.

![Day Three](./images/trello_board_day_three.jpg)

## **Day Four:**

- I started creating the classes to iterate with the lists and also to split my rough code into functions following the PEP-8 standards and OOP.

![Day Four](./images/trello_board_day_four.jpg)

## **Day Five:**

- I started implementing some error handling and validations.

![Day Five](./images/trello_board_day_five.jpg)

## **Day Six:**

- Created an ASCII logo and finish message.

![Day Six](./images/trello_board_day_six.jpg)



Click [here](https://trello.com/invite/b/r3h2nupf/f9aec563ed1bb1216b8cef26ded72817/agile-board) To open Trello board.


# **Help Documentation**

## **Installation guide:**
### **Follow the steps bellow to run the app:**
- Click [here](https://www.pythonanywhere.com/shared_console/428b4346-f536-42ef-b44f-295213d890d1) To open App on Python anywhere host.
- Alternatively if you want to run the app in your terminal follow the steps bellow.
- Make sure you are on a WSL2 Ubuntu Environment, [Click Here](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview) To install it.
- Clone the [Repository](https://github.com/Guscosta88/GusCosta_T1A3) and cd into it.
- Run the 3 following commands in sequence in your wsl2 terminal.
- ./my_wrapper.sh
- source .venv/bin/activate
- python3 main.py

- The ./my_wrapper.sh command will install all the python packages needed to run this app as well as a .venv virtual environment. The source .venv/bin/activate will allow you to access the .venv virtual environment.The python3 main.py is the command to start the application.

### **In case you get an error:**
- If for any reason the ./my_wrapper.sh command doesn't work you can install the packages manually one by one with the following commands:
1. sudo python3 -m pip install --upgrade pip
2. sudo apt update && sudo apt install python3.10-venv
3. sudo apt install python3-venv
4. python3 -m venv .venv
5. source .venv/bin/activate
6. pip install simple-term-menu
7. pip install clearing
8. pip install cowsay
9. pip install color-terminal
10. pip install pytest
