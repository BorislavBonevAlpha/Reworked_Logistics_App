
class Locations:

    Sydney = 'Sydney'
    Melbourne = 'Melborune'
    Adelaide = 'Adelaide'
    AliceSprings = 'AliceSprings'
    Brisbane = 'Brisbane'
    Darwin = 'Darwin'
    Perth = 'Perth'

    def __init__(self, starting_location: str, ending_location: str) -> None:
        
        self.starting_location = starting_location
        self.ending_location = ending_location

        