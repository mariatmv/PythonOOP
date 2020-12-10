from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        hp = HeavyHardware(name, capacity, memory)
        System._hardware.append(hp)

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        try:
            s = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(s)
            System._software.append(s)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption:int, memory_consumption:int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        try:
            s = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(s)
            System._software.append(s)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        software = [x for x in System._software if x.name == software_name]
        if not software or not hardware:
            return "Some of the components do not exist"

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        used_memory = int(sum([x.memory_consumption for x in System._software]))
        total_memory = int(sum([x.total_memory for x in System._hardware]))
        used_capacity = int(sum([x.capacity_consumption for x in System._software]))
        total_capacity = int(sum([x.total_capacity for x in System._hardware]))
        output = f'System Analysis\nHardware Components: {len(System._hardware)}\n' \
                 f'Software Components: {len(System._software)}\n' \
                 f'Total Operational Memory: {used_memory} / {total_memory}\n' \
                 f'Total Capacity Taken: {used_capacity} / {total_capacity}'
        return output

    @staticmethod
    def system_split():
        output = f""
        for hardware in System._hardware:
            express_softwares = [x for x in hardware.software_components if x.type == "Express"]
            light_softwares = [x for x in hardware.software_components if x.type == "Light"]
            used_memory = sum([x.memory_consumption for x in hardware.software_components])
            used_capacity = sum([x.capacity_consumption for x in hardware.software_components])
            output += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {len(express_softwares)}\n" \
                      f"Light Software Components: {len(light_softwares)}\n" \
                      f"Memory Usage: {int(used_memory)} / {hardware.total_memory}\n" \
                      f"Capacity Usage: {int(used_capacity)} / {hardware.total_capacity}\n" \
                      f"Type: {hardware.type}\n"
            output += f"Software Components: {', '.join([x.name for x in hardware.software_components]) or 'None'}"

        return output
