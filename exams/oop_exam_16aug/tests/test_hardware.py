from project.hardware.hardware import Hardware

import unittest

from project.software.software import Software


class TestHardware(unittest.TestCase):
    # def setUp(self):
    #     self.heavy_hd = Hardware("tejuk", "Heavy", 100, 100)
    #     self.power_hd = Hardware("silen", "Power", 300, 300)
    #     self.software = Software('Sf', 'Light', 200, 200)
    #
    # def test_attributes(self):
    #     for attr in ['name', 'type', 'capacity', 'memory']:
    #         self.assertTrue(hasattr(self.heavy_hd, attr))
    #
    # def test_initialization(self):
    #     self.assertEqual('tejuk', self.heavy_hd.name)
    #     self.assertEqual('Heavy', self.heavy_hd.type)
    #     self.assertEqual(100, self.heavy_hd.capacity)
    #     self.assertEqual(100, self.heavy_hd.memory)
    #     self.assertEqual([], self.heavy_hd.software_components)
    #
    #     self.assertEqual('silen', self.power_hd.name)
    #     self.assertEqual('Power', self.power_hd.type)
    #     self.assertEqual(300, self.power_hd.capacity)
    #     self.assertEqual(300, self.power_hd.memory)
    #     self.assertEqual([], self.power_hd.software_components)
    #
    # # def test_installation_should_be_successful(self):
    # #     self.power_hd.install(self.software)
    # #     self.assertEqual(1, len(self.power_hd.software_components))
    #
    # def test_installation_should_raise_exception(self):
    #     with self.assertRaises(Exception) as exc:
    #         self.heavy_hd.install(self.software)
    #         self.assertEqual("Software cannot be installed", exc)
    #
    # def test_uninstalling_software(self):
    #     self.power_hd.install(self.software)
    #     self.assertEqual(1, len(self.power_hd.software_components))
    #     self.power_hd.uninstall(self.software)
    #     self.assertEqual(0, len(self.power_hd.software_components))

    def setUp(self):
        self.hw = Hardware('Test hw', 'Power', 100, 50)
        self.sw = Software('Test sw', 'Light', 20, 10)

    def test_init_when_valid_arguments_should_implement(self):
        self.assertEqual(self.hw.name, 'Test hw')
        self.assertEqual(self.hw.type, 'Power')
        self.assertEqual(self.hw.capacity, 100)
        self.assertEqual(self.hw.memory, 50)
        self.assertEqual(self.hw.software_components, [])

    def test_install_when_not_enough_memory_or_capacity_should_raise_exception(self):
        self.sw = Software('Test sw', 'Light', 101, 51)
        with self.assertRaises(Exception) as ex:
            self.hw.install(self.sw)
        self.assertEqual(str(ex.exception), 'Software cannot be installed')

    def test_uninstall_when_software_in_components_should_remove_it(self):
        self.hw.software_components.append(self.sw)
        self.hw.uninstall(self.sw)
        self.assertEqual(self.hw.software_components, [])


if __name__ == '__main__':
    unittest.main()