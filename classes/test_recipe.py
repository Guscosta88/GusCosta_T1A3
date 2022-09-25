import pytest
from classes.recipe import Recipe

# The test_initial_recipe_value test function makes sure that the recipe list 
# items are run properly within the class through the correct attributes to 
# return the correct recipe values.
 
def test_initial_recipe_value():
    recipe_testing = Recipe("Gouda cheese", '''
CHEESE BOARD: 
Gouda cheese 
Prosciutto 
Walnuts

''', "cheese")     
    assert recipe_testing.name == "Gouda cheese"
    assert recipe_testing.description == '''
CHEESE BOARD: 
Gouda cheese 
Prosciutto 
Walnuts

'''
    assert recipe_testing.recipe_type == "cheese"

# The test_no_recipe_value test function raises an exception which means that the next block of code will be tested and if no exception
# is raised between recipe and Recipe() the test passes, otherwise it fails. 

def test_no_recipe_value():
    with pytest.raises(Exception) as e_info:
        recipe = Recipe()  