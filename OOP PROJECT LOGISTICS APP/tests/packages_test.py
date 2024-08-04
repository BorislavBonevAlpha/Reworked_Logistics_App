import unittest
from models.packages import Packages

class Packages_Should(unittest.TestCase):

    def test_set_correct_attributes(self):

        package = Packages(45.5)

        self.assertEqual(45.5, package.weight_kg)

    def test_check_correct_attributes(self):

        package = Packages(45.5)

        self.assertIsInstance(package.weight_kg, float)
    
    def test_set_incorrect_attributes(self):

        with self.assertRaises(ValueError):
            package = Packages(-1)
        with self.assertRaises(ValueError):
            package = Packages(101)

    def test_weight_setter_works(self):

        package = Packages(45.5)

        package.weight_kg = 60

        self.assertEqual(60, package.weight_kg)

    
    def test_weight_setter_works_with_incorrectinfo(self):

        with self.assertRaises(ValueError):
            package = Packages(45.5)

            package.weight_kg = -1

        with self.assertRaises(ValueError):
            package = Packages(45.5)

            package.weight_kg = 101

    def test_if_id_increments_correctly_packages(self):

        packages1 = Packages(50.5)

        self.assertEqual(1, packages1._id)

    def test_if_id_increments_incorrectly_packages(self):


        package = Packages(45.5)

        self.assertNotEqual(2, package._id)