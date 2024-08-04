from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from commands.command_validators import location_validator
from models.route import Route
from models.locations import Locations

class CreateRoute(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        starting_location, ending_location = self.params

        current_r = Route()
        route_id = Route.increment_id
        
        start_location = location_validator(starting_location)
        end_location = location_validator(ending_location)

        if start_location == end_location:
            raise ValueError('The starting location cannot be the same as the ending location')

        add_current_locations = Locations(start_location, end_location)

        current_r.add_locations(add_current_locations) # purvo adva locationite

        self._app_data.create_route(current_r) # sled tva se createva

        return f'Route with [ID: {route_id}] | Start location: {start_location} | End location: {end_location} was created'