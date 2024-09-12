from repository.json_repository import read_json
from api.weather_api import request_data
from service import pilot_service as ps, target_service as ts, aircraft_service as airs, weather_service as ws
from model.pilot import Pilot
from operator import itemgetter

read_pilots = read_json("assets/pilots.json")
pilots_models = ps.convert_pilots_to_models(read_pilots)
read_targets = read_json("assets/targets_priority.json")
targets_models = ts.convert_targets_to_models(read_targets)
read_aircraft = read_json("assets/aircraft_type.json")
aircraft_models = airs.convert_aircraft_to_models(read_aircraft)
read_weather = read_json("assets/targets_weather.json")
weather_models = ws.convert_weather_to_models(read_weather)
read_locations = read_json("assets/cities_location.json")

print(read_locations)


def pilot_score(pilot: Pilot):
    # /5 to make this 20% of the total score
    return pilot.skill / 10 / 5


def wind_scr_calc(wind_speed):
    wind_speeds = list(map(lambda a: a.wind_speed, weather_models))
    max_speed = max(wind_speeds)
    return (max_speed - wind_speed) * (100 / max_speed) / 100


def weather_score(city):
    status_score_dict = {"Clean": 1, "Clouds": 0.7, "Rain": 0.4, "Stormy": 0.2}
    city_weather = next(x for x in weather_models if x.location == city)
    cloud_scr = status_score_dict[city_weather.clouds]
    cloud_status_scr = city_weather.clouds_status / 100
    wind_scr = wind_scr_calc(city_weather.wind_speed)
    # /5 to make this 20% of the total score
    return (cloud_scr + cloud_status_scr + wind_scr) / 3 / 5


def main():
    targets_combination = {}
    for target in targets_models:
        targets_combination[f"{target.target_city}"] = []
        for aircraft in aircraft_models:
            for pilot in pilots_models:
                combo = {"target": target, "aircraft": aircraft, "pilot": pilot, "city": target.target_city}
                targets_combination[f"{target.target_city}"].append(combo)

        for combination in targets_combination[f"{target.target_city}"]:
            pilot_scr = pilot_score(combination["pilot"])
            weather_scr = weather_score(combination["city"])
            
    return targets_combination


# print(main())



