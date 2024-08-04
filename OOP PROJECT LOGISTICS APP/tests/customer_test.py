import unittest
from models.customer import Customer
from models.packages import Packages

class Customer_Should(unittest.TestCase):

    def test_set_correct_attributes(self):

        customer = Customer('Bobi','Bonev','bobi@abv.bg')

        self.assertEqual('Bobi', customer.first_name)
        self.assertEqual('Bonev', customer.last_name)
        self.assertEqual('bobi@abv.bg', customer.contact_email)

    def test_check_correct_attributes(self):

        customer = Customer('Bobi','Bonev','bobi@abv.bg')

        self.assertIsInstance(customer.first_name, str)
        self.assertIsInstance(customer.last_name, str)
        self.assertIsInstance(customer.contact_email, str)

    def test_set_incorrect_attributes(self):

        with self.assertRaises(ValueError):
            customer = Customer('Bobi','Bonev','bobabv.bg')

    def test_list_of_packages(self):

        customer = Customer('Bobi','Bonev','bobi@abv.bg')

        self.assertIsInstance(customer.packages, tuple)

    def test_if_contact_email_setter_works(self):

        customer = Customer('Bobi','Bonev','bobi@abv.bg')

        customer.contact_email = 'proba@abv.bg'

        self.assertEqual('proba@abv.bg', customer.contact_email)

    def test_if_contact_email_setter_works_with_incorrectinfo(self):

        with self.assertRaises(ValueError):
            customer = Customer('Bobi','Bonev','bobi@abv.bg')
            customer.contact_email = 'probaabv.bg'
        with self.assertRaises(ValueError):
            customer = Customer('Bobi','Bonev','bobi@abv.bg')
            customer.contact_email = 'pr@'
        with self.assertRaises(ValueError):
            customer = Customer('Bobi','Bonev','bobi@abv.bg')
            customer.contact_email = 'proasdasdasdkljaldsdfkjsfldkjsfdkljsdflkjsldfkjslfdkjsfdkljsdfkljsfdlkjfsdlkj@'

    def test_if_add_package_to_customer_method_works(self):

        customer = Customer('Bobi','Bonev','bobi@abv.bg')
        package = Packages(45.2)

        customer.add_package_to_customer(package)

        self.assertIn(package, customer.packages)

    def test_if_add_package_to_customer_method_works_2(self):

        with self.assertRaises(ValueError):
            customer = Customer('Bobi','Bonev','bobi@abv.bg')
            package = Packages(45.2)

            customer.add_package_to_customer(package)
            customer.add_package_to_customer(package)