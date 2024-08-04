from models.customer import Customer
from models.locations import Locations
from models.route import Route

class ApplicationData:

    def __init__(self):
        self._customers: list[Customer] = []
        self._routes: list[Route] = []

    @property
    def customers(self):
        return tuple(self._customers)
    
    def create_customer(self, first_name: str, last_name: str, contact_email: str):
        
        self._customers.append(Customer(first_name, last_name, contact_email))

    def get_specific_customer_by_email(self, customer_email: str):

        for customer in self._customers:
            if customer.contact_email == customer_email:
                return customer
        
        raise ValueError('There is no such customer with this email')
    
    def create_route(self, current_route: Route):
        
        self._routes.append(current_route)

    
    def get_specific_route_by_locations(self, first_location: str, second_location: str):
        
        for route in self._routes:
            for location in route._list_of_locations:
                if location.starting_location == first_location and location.ending_location == second_location:
                    return route
            
        raise ValueError('There is no current route matching those locations')
    
    def get_specific_route_by_id(self, route_id: int):

        for route in self._routes:
            if route._id == route_id:
                return route
            
        raise ValueError('There is no route matching this id')
    
    def get_specific_package_by_id(self, package_id: int):

        for customer in self._customers:
            for package in customer._packages:
                if package._id == package_id:
                    return package

            raise ValueError('There is no package matching this id')
        

    def get_specific_customer_by_package_by_id(self, package_id: int):

        for customer in self._customers:
            for package in customer._packages:
                if package._id == package_id:
                    return customer

            raise ValueError('There is no package matching this id')