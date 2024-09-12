from repository.json_repository import read_json
from api.weather_api import request_data
from service import weather_service as ws
from toolz import pipe, partial, curry, groupby
from model.pilot import Pilot


def convert_pilots_to_models(json_data):
    return [Pilot(a["name"], a["skill"]) for a in json_data]












