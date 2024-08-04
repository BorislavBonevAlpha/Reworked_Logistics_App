from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData

class CreateCustomer(BaseCommand):
    
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        
        first_name, last_name, contact_email = self.params

        self.app_data.create_customer(first_name, last_name, contact_email)

        return f'Customer: {first_name.capitalize()} {last_name.capitalize()} | with Email: {contact_email} was created'