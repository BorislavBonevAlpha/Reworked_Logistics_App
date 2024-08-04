from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from models.vehicles import Scania, Actros, Man

class AssingTruck(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        route_id, free_truck = self.params
        route_id = int(route_id)

        current_route = self._app_data.get_specific_route_by_id(route_id)

        if free_truck == 'Scania':
            scania = Scania('Scania', 42000, 8000)
            current_route.add_trucks(scania)
            return f'Truck # {scania._id}| Name: Scania | Capacity: 42000 | Max_range: 8000 was added to route [ID: {current_route._id}]'
        
        if free_truck == 'Man':
            man = Man('Man', 37000, 10000)
            current_route.add_trucks(man)
            return f'Truck # {man._id}| Name: Man | Capacity: 37000 | Max_range: 10000 was added to route [ID: {current_route._id}]'
       
        if free_truck == 'Actros':
            actros = Actros('Actros', 26000, 13000)
            current_route.add_trucks(actros)
            return f'Truck # {actros._id}| Name: Actros | Capacity: 26000 | Max_range: 13000 was added to route [ID: {current_route._id}]'