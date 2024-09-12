from api.weather_api import request_data
from model.weather import Weather
from toolz import pipe, partial, curry, groupby, get_in
from operator import itemgetter
from repository.json_repository import read_json, write_weather_list_to_json

targets = list(map(lambda a: a["Target City"], read_json("assets/targets_priority.json")))


def convert_weather_to_models(json_data):
    return [Weather(a["location"], a["clouds"], a["clouds_status"], a["wind_speed"]) for a in json_data]


def targets_midnight_weather_from_api():
    targets_weather = []
    for city in targets:
        data = request_data(
                        "https://api.openweathermap.org/data/2.5/forecast?q="
                        f"{city}"
                        "&appid=f4cd64d7d7b59b6a39edd5ae68daad1a")
        midnight_weather = filter_midnight(data)
        targets_weather.append(
            {
                "location": city,
                "weather": midnight_weather
            }
        )
    return targets_weather


def filter_midnight(city_data):
    return pipe(
            city_data["list"],
            partial(filter, lambda a: a if a["dt_txt"].endswith("00:00:00") else ""),
            next
        )


def convert_api_to_model(api_weather):
    print(get_in(["weather", "list", "weather"], api_weather))
    return Weather(
        location=api_weather["location"],
        clouds=get_in(["weather", "weather", 0, "main"], api_weather),
        clouds_status=get_in(["weather", "clouds", "all"], api_weather),
        wind_speed=get_in(["weather", "wind", "speed"], api_weather)
    )


def transform_weather_to_model(targets_weather_api):
    return pipe(
        targets_weather_api,
        partial(map, convert_api_to_model),
        list
    )


def write_weather_api_as_models():
    weather_from_api = targets_midnight_weather_from_api()
    weather_models = transform_weather_to_model(weather_from_api)
    write_weather_list_to_json(weather_models, "assets/targets_weather.json")



