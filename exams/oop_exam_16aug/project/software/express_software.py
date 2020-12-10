from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Express', capacity, memory * 2)