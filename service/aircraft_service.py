from model.aircraft import Aircraft


def convert_aircraft_to_models(json_data):
    return [Aircraft(a["type"], a["speed"], a["fuel_capacity"]) for a in json_data]


