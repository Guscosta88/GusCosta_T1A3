from classes.wine import Wine, Food
from classes.images import Image



wine_input = input("What type of red wine do you have in mind (Please enter full item name)? ")

wine_validation = Wine.is_valid_wine(wine_input)

print(wine_validation)


cheese = Image.cheese
print(cheese)
