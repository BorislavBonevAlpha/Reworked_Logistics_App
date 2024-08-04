

class Packages:
    increment_id = 0

    def __init__(self, weight_kg: float) -> None:
 
        self.weight_kg = weight_kg

        Packages.increment_id += 1
        self._id = Packages.increment_id

    @property
    def weight_kg(self):
        return self._weight_kg
    
    @weight_kg.setter
    def weight_kg(self, value):

        if value < 0 or value > 100:
            raise ValueError('Invalid kilograms')
        
        self._weight_kg = value


    