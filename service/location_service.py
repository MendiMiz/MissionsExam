# import requests
import math
# import json
#
# API_KEY = 'f4cd64d7d7b59b6a39edd5ae68daad1a'
# target_datetime = "2024-09-13 00:00:00"
#
#
# def get_city_coordinates(city_name):
#     url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             city_info = data[0]
#             lat = city_info.get('lat')
#             lon = city_info.get('lon')
#             return {"lat": lat, "lon": lon}
#         else:
#             return "City not found"
#     else:
#         return f"Error {response.status_code}: {response.text}"


def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0
    # Radius of the Earth in kilometers #
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance
















