from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity and len(self.workers) < self.__workers_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__budget < price and len(self.animals) < self.__animal_capacity and len(self.workers) < self.__workers_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker):
        found = list(filter(lambda x: x.name == worker, self.workers))
        if not found:
            return f"There is no {worker} in the zoo"
        self.workers.remove(found[0])
        return f"{worker} fired successfully"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_needs = 0
        for animal in self.animals:
            total_needs += animal.get_needs()
        if total_needs > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = f'You have {len(self.animals)} animals' + '\n'
        lions = list(filter(lambda x: type(x).__name__ == "Lion", self.animals))
        tigers = list(filter(lambda x: type(x).__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda x: type(x).__name__ == "Cheetah", self.animals))
        output += f'----- {len(lions)} Lions:'
        for l in lions:
            output += '\n' + l.__repr__()
        output += f'\n----- {len(tigers)} Tigers:'
        for t in tigers:
            output += '\n' + t.__repr__()
        output += f'\n----- {len(cheetahs)} Cheetahs:'
        for ch in cheetahs:
            output += '\n' + ch.__repr__()

        return output

    def workers_status(self):
        output = f'You have {len(self.workers)} workers' + '\n'
        keepers = list(filter(lambda x: type(x).__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda x: type(x).__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda x: type(x).__name__ == "Vet", self.workers))
        output += f'----- {len(keepers)} Keepers:'
        for k in keepers:
            output += '\n' + k.__repr__()
        output += f'\n----- {len(caretakers)} Caretakers:'
        for c in caretakers:
            output += '\n' + c.__repr__()
        output += f'\n----- {len(vets)} Vets:'
        for v in vets:
            output += '\n' + v.__repr__()
        return output


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300),
           Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
