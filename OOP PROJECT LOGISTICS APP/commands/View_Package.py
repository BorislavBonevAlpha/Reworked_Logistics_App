from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData

class ViewPackage(BaseCommand):

    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        package_id = int(self.params[0])

        current_customer = self.app_data.get_specific_customer_by_package_by_id(package_id)
        current_package = self.app_data.get_specific_package_by_id(package_id)
        
        return f'Package with ( ID: {current_package._id} and Weight: {current_package.weight_kg}kg ) is assigned to ( Customer: [ {current_customer.first_name} | {current_customer.last_name} ] | contact email: {current_customer.contact_email} )'