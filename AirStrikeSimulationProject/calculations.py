import math, json
from api_requests import *
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0 # Radius of the Earth in kilometers
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

# Get JLM's coordinates
JLM_coordinates_url = "http://api.openweathermap.org/geo/1.0/direct?q=Jerusalem,israel&APPID=67426bc9e51f120382ea5da6ca877eef"
JLM_coordinates_req = (requet_to_json(JLM_coordinates_url))[0]
JLM_lat_lon = (JLM_coordinates_req['lat'], JLM_coordinates_req['lon'])


# calc all cities distance
def calc_all_cities_distance(jlm_lat, jlm_lon, cities_lat_lon):
    all_distances = {}
    for city in cities_lat_lon:
        all_distances[city] = haversine_distance(jlm_lat, jlm_lon, cities_lat_lon[city]["lat"], cities_lat_lon[city]["lon"])
    return all_distances


# find all cities distances
city_targets_path = 'air_strike_targets.csv'
all_cities_coordinates = get_city_lat_lon(load_files.csv_read_dict(city_targets_path))
all_distances_dict = calc_all_cities_distance(JLM_lat_lon[0], JLM_lat_lon[1], all_cities_coordinates)
print(all_distances_dict)

# dump the distances to json file, so that i won't have to use api requests
with open("cities_distances.json", "w") as outfile:
    json.dump(all_distances_dict, outfile)

