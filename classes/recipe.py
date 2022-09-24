# Class Recipe iterates the values entered and it organizes it within 3 attributes, name, description, recipe_type.
# this class is imported in the main.py file.

class Recipe:
    def __init__(self, name, description, recipe_type):
        self.name = name
        self.description = description
        self.recipe_type = recipe_type