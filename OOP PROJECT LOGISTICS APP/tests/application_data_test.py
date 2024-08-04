import unittest
from core.application_data import ApplicationData
from models.locations import Locations
from models.packages import Packages
from models.route import Route
from models.vehicles import Actros, Man, Scania
from models.customer import Customer

class ApplicationData_Should(unittest.TestCase):

    def test_if_application_data_has_correct_collections(self):

        app_data = ApplicationData()

        self.assertIsInstance(app_data.customers, tuple)
        self.assertIsInstance(app_data._routes, list)

    
    def test_if_create_customer_works(self):

        app_data = ApplicationData()

        app_data.create_customer('borislav','bonev','bobi@abv.bg')

        self.assertEqual(1, len(app_data._customers))

    def test_if_get_specific_customer_by_email_works(self):

        app_data = ApplicationData()
        customer = Customer('borislav','bonev','bobi@abv.bg')

        app_data.create_customer('borislav','bonev','bobi@abv.bg')
        test = app_data.get_specific_customer_by_email('bobi@abv.bg')

        self.assertEqual('bobi@abv.bg', test.contact_email)

    def test_if_get_specific_customer_by_email_doesnt_works(self):

        with self.assertRaises(ValueError):
            app_data = ApplicationData()

            app_data.create_customer('borislav','bonev','bobi@abv.bg')
            test = app_data.get_specific_customer_by_email('bobi')

    def test_if_create_route_works(self):

        app_data = ApplicationData()
        route = Route()

        app_data.create_route(route)

        self.assertIn(route, app_data._routes)
        self.assertEqual(1, len(app_data._routes))

    
    def test_if_get_specific_route_by_locations_work(self):

        app_data = ApplicationData()
        route = Route()
        locations_in_route = Locations('Sydney', 'Melbourne')
        app_data.create_route(route)
        route.add_locations(locations_in_route)
        
        self.assertEqual(route, app_data.get_specific_route_by_locations('Sydney', 'Melbourne'))

    def test_if_get_specific_route_by_locations_doesnt_work(self):
        with self.assertRaises(ValueError):
            app_data = ApplicationData()
            route = Route()
            locations_in_route = Locations('Sydney', 'Melbourne')
            
            route.add_locations(locations_in_route)

            test = app_data.get_specific_route_by_locations('Sydney', 'Melbourne')
    

    def test_if_get_specific_route_by_id_works(self):

        app_data = ApplicationData()
        route = Route()

        app_data.create_route(route)

        self.assertEqual(route, app_data.get_specific_route_by_id(1))

    def test_if_get_specific_route_by_id_doesnt_works(self):

        with self.assertRaises(ValueError):
            app_data = ApplicationData()
            route = Route()

            app_data.create_route(route)

            test = app_data.get_specific_route_by_id(2)

    def test_if_get_specific_package_by_id_works(self):

        app_data = ApplicationData()
        
        package = Packages(45.5)

        app_data.create_customer('borislav', 'bonev', 'bobi@abv.bg')
        customer = app_data.get_specific_customer_by_email('bobi@abv.bg')

        customer.add_package_to_customer(package)

        self.assertEqual(package, app_data.get_specific_package_by_id(1))

    
    def test_if_get_specific_package_by_id_doesnt_works(self):

        with self.assertRaises(ValueError):
            app_data = ApplicationData()
        
            package = Packages(45.5)

            app_data.create_customer('borislav', 'bonev', 'bobi@abv.bg')
            customer = app_data.get_specific_customer_by_email('bobi@abv.bg')

            customer.add_package_to_customer(package)
            
            app_data.get_specific_package_by_id(2)


    def test_if_get_specific_customer_by_package_id_works(self):

        app_data = ApplicationData()
        package = Packages(45.5)
        app_data.create_customer('borislav', 'bonev', 'bobi@abv.bg')

        customer = app_data.get_specific_customer_by_email('bobi@abv.bg')

        customer.add_package_to_customer(package)

        self.assertEqual(customer, app_data.get_specific_customer_by_package_by_id(1))

    def test_if_get_specific_customer_by_package_id_doesnt_works(self):

        with self.assertRaises(ValueError):
            app_data = ApplicationData()
        
            package = Packages(45.5)

            app_data.create_customer('borislav', 'bonev', 'bobi@abv.bg')
            customer = app_data.get_specific_customer_by_email('bobi@abv.bg')

            customer.add_package_to_customer(package)
            
            app_data.get_specific_customer_by_package_by_id(2)