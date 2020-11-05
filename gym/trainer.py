class Trainer:
    id_counter = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.id_counter
        Trainer.id_counter += 1

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'

    @staticmethod
    def get_next_id():
        if Trainer.id_counter == 1:
            return 1
        return Trainer.id_counter
