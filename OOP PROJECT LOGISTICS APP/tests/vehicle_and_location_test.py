import unittest
from models.locations import Locations
from models.vehicles import Actros

class Locations_Should(unittest.TestCase):

    def test_if_locations_set_correct_attributes(self):

        location = Locations('Sydney', 'Melbourne')

        self.assertEqual('Sydney', location.starting_location)
        self.assertEqual('Melbourne', location.ending_location)

    def test_if_locations_have_correct_attributes(self):

        location = Locations('Sydney', 'Melbourne')

        self.assertIsInstance(location.starting_location, str)
        self.assertIsInstance(location.ending_location, str)

    def test_if_vehicle_sets_correct_attributes(self):

        vehicle = Actros('Actros', 300, 5000)

        self.assertEqual('Actros', vehicle.name)
        self.assertEqual(300, vehicle.capacity_kg)
        self.assertEqual(5000, vehicle.max_range)

    def test_if_vehicle_has_correct_id(self):

        vehicle = Actros('Actros', 300, 5000)

        self.assertEqual(1, vehicle._id)

    def test_if_vehicle_has_correct_attributes(self):

        vehicle = Actros('Actros', 300.50, 5000.0)

        self.assertIsInstance(vehicle.name, str)
        self.assertIsInstance(vehicle.capacity_kg, float)
        self.assertIsInstance(vehicle.max_range, float)