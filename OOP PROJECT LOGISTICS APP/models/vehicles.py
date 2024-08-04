
from models.constaints import check_if_ids_are_below_recommend, check_if_ids_are_below_recommend_actros_men

class Scania:
    increment_id = 0

    def __init__(self, name: str, capacity_kg: float, max_range: float) -> None:
        
        self.name = name
        self.capacity_kg = capacity_kg
        self.max_range = max_range

        Scania.increment_id += 1
        self._id = Scania.increment_id
        check_if_ids_are_below_recommend(self._id)


class Man:
    increment_id = 0

    def __init__(self, name: str, capacity_kg: float, max_range: float) -> None:
        
        self.name = name
        self.capacity_kg = capacity_kg
        self.max_range = max_range

        Man.increment_id += 1
        self._id = Man.increment_id
        check_if_ids_are_below_recommend_actros_men(self._id)



class Actros:
    increment_id = 0

    def __init__(self, name: str, capacity_kg: float, max_range: float) -> None:
        
        self.name = name
        self.capacity_kg = capacity_kg
        self.max_range = max_range

        Actros.increment_id += 1
        self._id = Actros.increment_id
        check_if_ids_are_below_recommend_actros_men(self._id)
