from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from models.vehicles import Actros, Man, Scania

class ViewRoute(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        route_id = int(self.params[0])

        current_route = self.app_data.get_specific_route_by_id(route_id)

        info_route = current_route.to_string()
        
        list_package_info = []
        list_truck_info = []

        for package in current_route._list_of_packages:
            description = f'Package ID Number: {package._id} | Package Weight: {package.weight_kg}'
            list_package_info.append(description)

        for truck in current_route._list_of_trucks:
            if isinstance(truck, Actros):
                description_truck = f'Actros: Truck ID Number: {truck._id} | Capacity Kg: {truck.capacity_kg} | Max Range: {truck.max_range}'
            if isinstance(truck, Man):
                description_truck = f'Man: Truck ID Number: {truck._id} | Capacity Kg: {truck.capacity_kg} | Max Range: {truck.max_range}'
            if isinstance(truck, Scania):
                description_truck = f'Scania: Truck ID Number: {truck._id} | Capacity Kg: {truck.capacity_kg} | Max Range: {truck.max_range}'
            list_truck_info.append(description_truck)
            
        info_package = f'{current_route.info_package()} \n | {'\n | '.join(map(str, list_package_info))}'
        info_truck = f'{current_route.info_trucks()} \n | {'\n | '.join(map(str, list_truck_info))}'
        return f'{info_route}' + f'\n{info_package}' + f'\n{info_truck}'