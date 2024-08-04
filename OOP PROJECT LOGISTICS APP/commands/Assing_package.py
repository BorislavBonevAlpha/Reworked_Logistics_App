from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData

class AssingPackage(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)


    def execute(self):
        
        route_id, package_id = self._params
        route_id = int(route_id)
        package_id = int(package_id)

        current_route = self._app_data.get_specific_route_by_id(route_id)

        current_package = self._app_data.get_specific_package_by_id(package_id)

        current_route.add_package(current_package)

        return f'Package with [ID: {current_package._id}] was added to Route with [ID: {current_route._id}]'