from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient (self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient (self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        if value <= self.capacity:
            return True
        return False
