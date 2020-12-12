from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    @property
    def products(self):
        return self.ingredients

    def add_ingredient(self, ingredient_type: str, quantity: int):
        l = ["white", "yellow", "blue", "green", "red"]
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