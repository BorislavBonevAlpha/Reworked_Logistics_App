
def location_validator(location):
    list_locations = ['Sydney','Melbourne', 'Adelaide', 'AliceSprings', 'Brisbane', 'Darwin', 'Perth']
    if location not in list_locations:
        raise ValueError('There is no such location')
    else:
        return location