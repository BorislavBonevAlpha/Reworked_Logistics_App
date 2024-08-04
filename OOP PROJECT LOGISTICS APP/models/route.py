from models.locations import Locations
from models.packages import Packages
from models.vehicles import Actros, Man, Scania

class Route:
    increment_id = 0

    def __init__(self) -> None:
        
        Route.increment_id += 1
        self._id = Route.increment_id

        self._list_of_locations: list[Locations] = []
        self._list_of_packages: list[Packages] = []
        self._list_of_trucks: list[Actros, Man, Scania] = []

    
    def add_locations(self, location: Locations):

        self._list_of_locations.append(location)

    def add_package(self, package: Packages):
        
        if package in self._list_of_packages:
            raise ValueError('You already added this package to the route')

        self._list_of_packages.append(package)
        
    def add_trucks(self, truck):

        if isinstance(truck, Actros):
            self._list_of_trucks.append(truck)

        if isinstance(truck, Man):
            self._list_of_trucks.append(truck)

        if isinstance(truck, Scania):
            self._list_of_trucks.append(truck)

    def to_string(self):

        return f'----------------------------------------------------- \n Information about Route: # {self._id}'
    
    def info_package(self):

        return f'Assigned Packages: ({len(self._list_of_packages)})'
    
    def info_trucks(self):

        return f'Assigned Trucks: ({len(self._list_of_trucks)})'