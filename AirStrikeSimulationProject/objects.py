from load_files import *
# from AirStrikeSimulationProject import "cities_distance.json"
class Pilote:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_sevel = skill_level

class AirCraft:
    def __init__(self, type, speed, fuel_capacity):
        self.type = type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

    # def calc_ability(self):


class CityTarget:
    def __init__(self, city,  priority, distance, weather):
        self.city = city
        self.distance = distance
        self.weather = weather
        self.weather_score = 0
        self.priority = priority



class Mission:
    def __init__(self, city_target, aircraft, pilote):
        self.city_target = city_target
        self.aircraft = aircraft
        self.pilote = pilote


# TODO calc speed

def is_fuel_per_mission(fuel_capacity, distance):
    one_direction = fuel_capacity / 2
    if one_direction < distance:
        return 0
    return 1

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

# print(load_json('pilots.json'))




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




city_targets_dict =  csv_read_dict(city_targets_path)

def add_distance(cities_path, cities_distance_path):
    city_targets_dict = csv_read_dict(cities_path)
    distance_dict = load_json(cities_distance_path)
    for city in city_targets_dict:
        city['distance'] = distance_dict[city['City']]
    return city_targets_dict


def add_weather(added_dis, cities_weather_path):
    weather_dict = load_json(cities_weather_path)
    for city in added_dis:
        city['weather'] = weather_dict[city['City']]
    return added_dis

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

