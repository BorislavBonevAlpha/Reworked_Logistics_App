
def check_if_ids_are_below_recommend(id: int):

    if id > 10:
        raise ValueError('No trucks from this model available')
    else:
        return id
    

def check_if_ids_are_below_recommend_actros_men(id: int):

    if id > 15:
        raise ValueError('No trucks from this model available')
    else:
        return id