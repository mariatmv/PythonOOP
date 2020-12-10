from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.total_capacity = capacity
        self.memory = memory
        self.total_memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)
        self.memory -= software.memory_consumption
        self.capacity -= software.capacity_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)
