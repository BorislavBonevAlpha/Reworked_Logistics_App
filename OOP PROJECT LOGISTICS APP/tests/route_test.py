import unittest
from models.route import Route
from models.locations import Locations
from models.packages import Packages
from models.vehicles import Actros, Man, Scania
from models.constaints import check_if_ids_are_below_recommend,check_if_ids_are_below_recommend_actros_men

class Routes_Should(unittest.TestCase):

    def test_if_id_increments(self):

        route = Route()

        self.assertEqual(1, route._id)

    def test_if_isinstance_correct_tuples(self):

        route = Route()

        self.assertIsInstance(route._list_of_locations, list)
        self.assertIsInstance(route._list_of_packages, list)
        self.assertIsInstance(route._list_of_trucks, list)

    def test_if_method_add_locations_works(self):

        route = Route()
        current_loc = Locations('Sydney', 'Melbourne')

        route.add_locations(current_loc)

        self.assertIn(current_loc, route._list_of_locations)

    def test_if_method_add_packages_works(self):

        current_package = Packages(45.5)
        route = Route()

        route.add_package(current_package)

        self.assertIn(current_package, route._list_of_packages)

    def test_if_method_incorrect_add_packages_works(self):
        
        with self.assertRaises(ValueError):
            current_package = Packages(45.5)
            route = Route()
            route.add_package(current_package)
            route.add_package(current_package)

    def test_if_method_add_trucks_works(self):

        route = Route()
        trucks = Actros('Actros', 59.9, 2000)

        route.add_trucks(trucks)

        self.assertIn(trucks, route._list_of_trucks)

    def test_to_string_method_works(self):

        route = Route()

        self.assertEqual('----------------------------------------------------- \n Information about Route: # 1', route.to_string())

    def test_info_package_method_works(self):

        route = Route()

        self.assertEqual('Assigned Packages: (0)', route.info_package())

    def test_info_truck_method_works(self):

        route = Route()

        self.assertEqual('Assigned Trucks: (0)', route.info_trucks())

    def test_if_constants_work(self):

        id = 5
        checker = check_if_ids_are_below_recommend(id)
        checker2 = check_if_ids_are_below_recommend_actros_men(id)
        self.assertEqual(5, checker)
        self.assertEqual(5, checker2)

    def test_if_constants_attribute_int(self):

        id = 5
        checker = check_if_ids_are_below_recommend(id)
        checker2 = check_if_ids_are_below_recommend_actros_men(id)

        self.assertIsInstance(checker, int)
        self.assertIsInstance(checker2, int)
        
    def test_if_constant_dont_work(self):

        with self.assertRaises(ValueError):
            id1 = 11
            id2 = 16
            checker = check_if_ids_are_below_recommend(id1)
            checker2 = check_if_ids_are_below_recommend_actros_men(id2)