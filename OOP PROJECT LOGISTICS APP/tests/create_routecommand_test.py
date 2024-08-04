import unittest
from unittest.mock import MagicMock, patch
from commands.Base_Command import BaseCommand
from core.application_data import ApplicationData
from commands.Create_Package import CreatePackage
from commands.Create_Route import CreateRoute

class TestCreateRoute(unittest.TestCase):

    @patch('core.application_data.ApplicationData')
    @patch('models.route.Route')
    @patch('models.locations.Locations')
    def test_create_route_success(self, MockLocations, MockRoute, MockApplicationData):
        # Arrange
        mock_app_data = MockApplicationData()
        mock_route = MockRoute()
        mock_locations = MockLocations()

        # Create the command instance
        command = CreateRoute(['Sydney', 'Melbourne'], mock_app_data)
        
        # Act
        result = command.execute()

        # Assert
        mock_route.add_locations.assert_called_once_with(mock_locations)
        mock_app_data.create_route.assert_called_once_with(mock_route)
        self.assertEqual(result, 'Route with [ID: 1] | Start location: Sydney | End location: Melbourne was created')

    @patch('core.application_data.ApplicationData')
    def test_create_route_success(self, MockApplicationData):
        with self.assertRaises(ValueError):
            mock_app_data = MockApplicationData()
            mock_location = MagicMock()
            mock_route = MagicMock()

            command = CreateRoute(['Sydney',], mock_app_data)

            result = command.execute()
