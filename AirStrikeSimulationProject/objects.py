from load_files import *

# Pilote object
class Pilote:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level
        self.skill_score = 0

# AirCraft object
class AirCraft:
    def __init__(self, type, speed, fuel_capacity):
        self.type = type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

# Targeted cities object
class CityTarget:
    def __init__(self, city,  priority, distance, weather):
        self.city = city
        self.distance = distance
        self.weather = weather
        self.weather_score = 0
        self.priority = priority
        self.priority_score = 0

# Mission's object. Contains city, aircraft and pilote objects.
class Mission:
    def __init__(self, city_target=None, aircraft=None, pilote=None):
        self.city_target = city_target
        self.aircraft = aircraft
        self.pilote = pilote
        self.mission_score = 0



# city_targets_dict =  csv_read_dict(city_targets_path)

# Add distance to cities dict
def add_distance(cities_path, cities_distance_path):
    city_targets_dict = csv_read_dict(cities_path)
    distance_dict = load_json(cities_distance_path)
    for city in city_targets_dict:
        city['distance'] = distance_dict[city['City']]
    return city_targets_dict


# Add weather to cities dict
def add_weather(added_dis, cities_weather_path):
    weather_dict = load_json(cities_weather_path)
    for city in added_dis:
        city['weather'] = weather_dict[city['City']]
    return added_dis


# Read from file and create pilots list
def creat_pilots(file_path):
    pilots_obj_list = []
    pilots_dict = load_json(file_path)
    for pilote in pilots_dict:
        pilote_obj = Pilote(
            pilote['name'],
            pilote['skill_level']
        )
        pilots_obj_list.append(pilote_obj)
    return pilots_obj_list


# Read from file and create aircrafts list
def creat_aircrafts(file_path):
    aircrafts_obj_list = []
    aircrafts_dict = load_json(file_path)
    for ac in aircrafts_dict:
        aircraft_obj = AirCraft(
            ac['type'],
            ac['speed'],
            ac["fuel_capacity"]
        )
        aircrafts_obj_list.append(aircraft_obj)
    return aircrafts_obj_list


# Create cities list reading from cities dict
def creat_cities(cities_dict):
    cities_obj_list = []
    for c in cities_dict:
        city_obj = CityTarget(
            c['City'],
            c["Priority"],
            c['distance'],
            c["weather"],
        )
        cities_obj_list.append(city_obj)
    return cities_obj_list


# Read from file and create missions list
def create_missions(cities, aircrafts, pilots):
    mission_list = []
    for c in cities:
        for p in pilots:
            for a in aircrafts:
                mission = Mission(
                    c,
                    a,
                    p,
                )
                mission_list.append(mission)
    return mission_list



