from project.people.child import Child
from project.rooms.room import Room

import unittest


class TestRoom(unittest.TestCase):
    def test_attributes(self):
        room_one = Room('Ivanovi', 1500, 2)
        for attr in ['family_name', 'budget', 'members_count', 'children', 'expenses']:
            self.assertTrue(hasattr(room_one, attr))

    def test_initialization(self):
        room_one = Room('Ivanovi', 1500, 2)
        self.assertEqual(room_one.family_name, 'Ivanovi')
        self.assertEqual(room_one.budget, 1500)
        self.assertEqual(room_one.members_count, 2)
        self.assertEqual(room_one.children, [])
        self.assertEqual(room_one.expenses, 0)

    def test_expenses_propery_should_raise_value_error(self):
        room_one = Room('Ivanovi', 1500, 2)
        with self.assertRaises(ValueError) as exc:
            room_one.expenses = -10

    def test_calculate_expenses(self):
        child = Child(20)
        room_one = Room('Ivanovi', 1500, 2)
        room_one.calculate_expenses(child)
        self.assertEqual(room_one.expenses, 600)



if __name__ == '__main__':
    unittest.main()