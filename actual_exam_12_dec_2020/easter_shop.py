from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        try:
            self.chocolate_factory.make_chocolate(recipe)
            self.storage[recipe] = self.chocolate_factory.products[recipe]
        except Exception as context:
            return str(context)

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.ingredients and color in self.paint_factory.ingredients:
            new_key = f'{color} {egg_type}'
            if new_key in self.storage.keys():
                self.storage[new_key] += 1
            else:
                self.storage[new_key] = 1
            for ing in self.paint_factory.ingredients:
                # self.paint_factory.ingredients[color] = 0
                self.paint_factory.remove_ingredient(ing, self.paint_factory.ingredients[ing])
            for ing in self.egg_factory.ingredients:
                # self.egg_factory.ingredients[egg_type] = 0
                self.egg_factory.remove_ingredient(ing, self.egg_factory.ingredients[ing])
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        output = [f'Shop name: {self.name}', f'Shop Storage:']
        for k, v in self.storage.items():
            output.append(f'{k}: {v}')


# egg_fc = EggFactory('eggs', 100)
# egg_fc.add_ingredient('quail egg', 2)
# paint_fc = PaintFactory('pp', 100)
# paint_fc.add_ingredient("yellow", 2)
# ch_fc = ChocolateFactory('ch', 100)
# shop = EasterShop('shop', ch_fc, egg_fc, paint_fc)
# shop.paint_egg("yellow", 'quail egg')