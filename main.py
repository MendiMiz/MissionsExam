from repository.json_repository import read_json
from api.weather_api import request_data
from service import weather_service as ws
from toolz import pipe, partial, curry, groupby
from operator import itemgetter
import flow

# if __name__ == '__main__':
#     print(flow.pilots_model[0])

