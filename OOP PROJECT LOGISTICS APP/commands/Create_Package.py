from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from commands.command_validators import location_validator
from models.packages import Packages

class CreatePackage(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)


    def execute(self):
        
        start_location, end_location, weight_kg, customer_email = self.params

        start_location = location_validator(start_location)
        end_location = location_validator(end_location)

        specific_customer = self._app_data.get_specific_customer_by_email(customer_email)
        creating_package = Packages(float(weight_kg))

        package_id = Packages.increment_id

        specific_customer.add_package_to_customer(creating_package)

        return f'Package with [ID: {package_id}] was assigned to customer with email: {specific_customer.contact_email}'
        

