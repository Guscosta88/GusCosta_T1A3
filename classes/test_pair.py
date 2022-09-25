import pytest
from classes.pair import Pair

# The test_initial_pair_value test function makes sure that the pair list 
# items are run properly within the class through the correct attributes 
# to return the correct pair values.
 
def test_initial_pair_value():
    pair_testing = Pair("Cabernet sauvignon", "Roast beef", "Gouda cheese", "Plums")     
    assert pair_testing.wine == "Cabernet sauvignon"
    assert pair_testing.main_dish == "Roast beef"
    assert pair_testing.cheese == "Gouda cheese"
    assert pair_testing.fruit == "Plums"

# The test_no_pair_value test function raises an exception which means that the next block of code will be tested and if no exception
# is raised between pair and Pair() the test passes, otherwise it fails. 

def test_no_pair_value():
    with pytest.raises(Exception) as e_info:
        pair = Pair()   