from project.spaceship.spaceship import Spaceship

import unittest


class TestSpaceship(unittest.TestCase):
    def test_initialization(self):
        test = Spaceship("ime", 300)
        self.assertEqual("ime", test.name)
        self.assertEqual(300, test.capacity)
        self.assertEqual([], test.astronauts)

        for attr in ['name', 'capacity', 'astronauts']:
            self.assertTrue(hasattr(test, attr))

    def test_add_should_raise_exception_when_not_enough_capacity(self):
        test = Spaceship("ime", 0)
        with self.assertRaises(ValueError) as context:
            test.add('nqkakvo ime')
            self.assertEqual("Spaceship is full", context)

    def test_add_should_raise_exception_when_astronaut_already_exist(self):
        test = Spaceship("ime", 2)
        test.astronauts.append('zdr')
        with self.assertRaises(ValueError) as context:
            test.add('zdr')
            self.assertEqual("Astronaut zdr Exists", context)

    def test_should_add_new_astronaut(self):
        test = Spaceship("ime", 2)
        test.add('zdr')
        self.assertEqual('zdr', test.astronauts[0])
        self.assertEqual("Added astronaut ime", test.add('ime'))

    def test_remove_should_raise_exception_if_astronaut_doesnt_exist(self):
        test = Spaceship("ime", 1)
        with self.assertRaises(ValueError) as context:
            test.remove('zdr')
            self.assertEqual(context, "Astronaut Not Found")

    def test_should_remove_astronaut(self):
        test = Spaceship("ime", 2)
        test.add('zdr')
        self.assertEqual('zdr', test.astronauts[0])
        test.remove('zdr')
        self.assertEqual([], test.astronauts)


if __name__ == '__main__':
    unittest.main()