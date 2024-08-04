import unittest
from unittest.mock import MagicMock, patch
from commands.Create_Package import CreatePackage

class TestCreatePackage(unittest.TestCase):

    @patch('core.application_data.ApplicationData')
    def test_create_package_success(self, MockApplicationData):
        # Arrange
        mock_app_data = MockApplicationData()
        mock_customer = MagicMock()
        
        mock_customer.contact_email = 'bobi@abv.bg'
        mock_app_data.get_specific_customer_by_email.return_value = mock_customer
    
        command = CreatePackage(['Sydney', 'Melbourne', 45.5, 'bobi@abv.bg'], mock_app_data)
        
        # Act
        result = command.execute()

        # Assert
        mock_app_data.get_specific_customer_by_email.assert_called_once_with('bobi@abv.bg')
        mock_customer.add_package_to_customer.assert_called_once()
        self.assertEqual(result, f'Package with [ID: 1] was assigned to customer with email: {mock_customer.contact_email}')


    @patch('core.application_data.ApplicationData')
    def test_create_package_error(self, MockApplicationData):
        
        with self.assertRaises(ValueError):
            mock_app_data = MockApplicationData()
            mock_customer = MagicMock()
            
            mock_customer.contact_email = 'bobi@abv.bg'
            mock_app_data.get_specific_customer_by_email.return_value = mock_customer
        
            command = CreatePackage(['Sydney', 'Melbourne', 'bobi@abv.bg'], mock_app_data)
            
            # Act
            result = command.execute()
