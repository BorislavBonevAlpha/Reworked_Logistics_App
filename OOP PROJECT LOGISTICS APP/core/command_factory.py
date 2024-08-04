from core.application_data import ApplicationData
from commands.Create_Customer import CreateCustomer
from commands.Create_Package import CreatePackage
from commands.Create_Route import CreateRoute
from commands.Search_Route_Command import SearchRoute
from commands.Assing_package import AssingPackage
from commands.Assign_truck import AssingTruck
from commands.View_Route import ViewRoute
from commands.View_Package import ViewPackage

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):

        cmd, *params = input_line.split()

        if cmd.lower() == 'createcustomer':
            return CreateCustomer(params, self._app_data)
        if cmd.lower() == 'createpackage':
            return CreatePackage(params, self._app_data)
        if cmd.lower() == 'createroute':
            return CreateRoute(params, self._app_data)
        if cmd.lower() == 'searchroute':
            return SearchRoute(params, self._app_data)
        if cmd.lower() == 'assignpackage':
            return AssingPackage(params, self._app_data)
        if cmd.lower() == 'assigntruck':
            return AssingTruck(params, self._app_data)
        if cmd.lower() == 'viewroute':
            return ViewRoute(params, self._app_data)
        if cmd.lower() == 'viewpackage':
            return ViewPackage(params, self._app_data)
        else:
            raise ValueError('There is no such command')