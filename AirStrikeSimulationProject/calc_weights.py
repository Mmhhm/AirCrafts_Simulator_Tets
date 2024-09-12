from objects import *

all_pilots_obj = creat_pilots('pilots.json')

all_aircrafts_obj = creat_aircrafts('aircrafts.json')

added_dis = add_distance('C:\\Users\\mkf\\Desktop\\IDF DATA Course\\Tests\\Test_12_9_24\\AirStrikeSimulationProject\\air_strike_targets.csv', 'C:\\Users\\mkf\\Desktop\\IDF DATA Course\\Tests\\Test_12_9_24\\AirStrikeSimulationProject\\cities_distances.json')
full_city_lst = add_weather(added_dis, 'C:\\Users\\mkf\\Desktop\\IDF DATA Course\\Tests\\Test_12_9_24\\AirStrikeSimulationProject\\cities_weather.json')
full_cities_obj_lst = creat_cities(full_city_lst)
print(full_city_lst)
print(added_dis)



def main_weather_score(weather):
    if weather == "Clear":
        return 1.0
    elif weather == "Clouds":
        return 0.7
    elif weather == "Rain":
        return 0.4
    elif weather == "Stormy":
        return 0.2
    else:
        return 0



def find_max_cloud(city_lst):
    max = 0
    for city in city_lst:
        if city.weather['clouds'] > max:
            max = city.weather['clouds']
    if max != 0:
        return max / 100
    return 0

print(find_max_cloud(full_cities_obj_lst))

def cloud_weather_score(city_lst, clouds):
    max_clouds = find_max_cloud(city_lst)
    if clouds != 0:
        return 1 - (max_clouds / clouds)
    return 0


def find_max_wind(city_lst):
    max = 0
    for city in city_lst:
        if city.weather['wind'] > max:
            max = city.weather['wind']
    if max != 0:
        return max / 100
    return 0

def calc_wind_score(city_lst, wind):
    max_winds = find_max_wind(city_lst)
    if wind != 0:
        return 1 - (max_winds / wind)
    return 0


def calc_full_weather(city_list, weather):
    main_weather = main_weather_score(weather['weather'])
    cloud_weather = cloud_weather_score(city_list, weather['clouds'])
    wind_score = calc_wind_score(city_list, weather['wind'])
    third = 1 / 3
    return main_weather * third + cloud_weather * third + wind_score * third

# print(calc_full_weather(full_cities_obj_lst, full_cities_obj_lst[0].weather)) # remove

def assign_weather_score(city_list):
    for city in city_list:
        city.weather_score = calc_full_weather(city_list, city.weather)
    return city_list

print(assign_weather_score(full_cities_obj_lst)[9].weather_score)










