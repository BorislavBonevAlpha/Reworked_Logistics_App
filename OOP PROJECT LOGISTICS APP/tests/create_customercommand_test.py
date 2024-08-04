import unittest
from unittest.mock import MagicMock, patch
from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from commands.Create_Customer import CreateCustomer

class TestCreateCustomer(unittest.TestCase):

    @patch('core.application_data.ApplicationData')
    def test_execute_success(self, MockApplicationData):
        # Arrange
        mock_app_data = MockApplicationData()
        command = CreateCustomer(['John', 'Doe', 'john.doe@example.com'], mock_app_data)
        
        # Act
        result = command.execute()

        # Assert
        mock_app_data.create_customer.assert_called_once_with('John', 'Doe', 'john.doe@example.com') # edin vid toq red ni trqbva za da sme sigurni 
        #che pravilno se izvikva komandata s pravilnite parametri
        self.assertEqual(result, 'Customer: John Doe | with Email: john.doe@example.com was created')
        

    @patch('core.application_data.ApplicationData')
    def test_execute_incorrect(self, MockApplicationData):

        with self.assertRaises(ValueError):

            mock_app_data = MockApplicationData()

            command = CreateCustomer(['John', 'john.doe@example.com'], mock_app_data)

            result = command.execute()
