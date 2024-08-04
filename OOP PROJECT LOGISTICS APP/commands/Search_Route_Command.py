from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from commands.command_validators import location_validator

class SearchRoute(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        first_location, second_location = self._params

        first_location = location_validator(first_location)
        second_location = location_validator(second_location)

        get_current_route = self._app_data.get_specific_route_by_locations(first_location, second_location)

        return f'Current route that matches your package: [ID: {get_current_route._id}] '