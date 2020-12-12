from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        l = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
        if ingredient_type in l:
            if quantity <= self.capacity:
                if ingredient_type not in self.ingredients.keys():
                    self.ingredients[ingredient_type] = quantity
                    # self.capacity -= quantity
                else:
                    self.ingredients[ingredient_type] += quantity
                    # self.capacity -= quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients.keys():
            if quantity <= self.ingredients[ingredient_type]:
                # todo: check if quantity is 0 and then remove the whole ingredient
                self.ingredients[ingredient_type] -= quantity
                # self.capacity += quantity
            else:
                raise ValueError("Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name not in self.recipes.keys():
            self.recipes[recipe_name] = recipe
        else:
            self.recipes[recipe_name].update(recipe)
            # todo: not really sure it works

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes.keys():
            raise TypeError("No such recipe")

        if recipe_name not in self.products.keys():
            self.products[recipe_name] = 1
        else:
            self.products[recipe_name] += 1

        for ingredient in self.recipes[recipe_name]:
            self.ingredients[ingredient] -= self.recipes[recipe_name][ingredient]
            # todo: again not sure

