from models.packages import Packages

class Customer:

    def __init__(self, first_name: str, last_name: str, contact_email: str) -> None:
        
        self._first_name = first_name
        self._last_name = last_name
        self.contact_email = contact_email
        self._packages: list[Packages] = []

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def contact_email(self):
        return  self._contact_email
    
    @contact_email.setter
    def contact_email(self, value):

        if len(value) < 4 or len(value) > 50:
            raise ValueError('This email is invalid')
        if not '@' in value:
            raise ValueError('The email should contain the symbol "@"')
        
        self._contact_email = value

    def add_package_to_customer(self, package: Packages):
        if package in self.packages:
            raise ValueError('There is already such package')
        self._packages.append(package)
