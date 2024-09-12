from objects import *


all_pilots_obj = creat_pilots('pilots.json')
all_aircrafts_obj = creat_aircrafts('aircrafts.json')

added_dis = add_distance('C:\\Users\\mkf\\Desktop\\IDF DATA Course\\Tests\\Test_12_9_24\\AirStrikeSimulationProject\\air_strike_targets.csv', 'C:\\Users\\mkf\\Desktop\\IDF DATA Course\\Tests\\Test_12_9_24\\AirStrikeSimulationProject\\cities_distances.json')
full_city_lst = add_weather(added_dis, 'C:\\Users\\mkf\\Desktop\\IDF DATA Course\\Tests\\Test_12_9_24\\AirStrikeSimulationProject\\cities_weather.json')
full_cities_obj_lst = creat_cities(full_city_lst)
print(f'city list: {full_city_lst}')
print(added_dis)


# Weather to number
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


# Find the max cloud in weather
def find_max_cloud(city_lst):
    max = 0
    for city in city_lst:
        if city.weather['clouds'] > max:
            max = city.weather['clouds']
    if max != 0:
        return max / 100
    return 0

print(find_max_cloud(full_cities_obj_lst))


# Calc cloud score
def cloud_weather_score(city_lst, clouds):
    max_clouds = find_max_cloud(city_lst)
    if clouds != 0:
        return 1 - (max_clouds / clouds)
    return 0


# Find the max wind in weather
def find_max_wind(city_lst):
    max = 0
    for city in city_lst:
        if city.weather['wind'] > max:
            max = city.weather['wind']
    if max != 0:
        return max / 100
    return 0


# Calc wind score
def calc_wind_score(city_lst, wind):
    max_winds = find_max_wind(city_lst)
    if wind != 0:
        return 1 - (max_winds / wind)
    return 0


# Calc full weather score
def calc_full_weather(city_list, weather):
    main_weather = main_weather_score(weather['weather'])
    cloud_weather = cloud_weather_score(city_list, weather['clouds'])
    wind_score = calc_wind_score(city_list, weather['wind'])
    third = 1 / 3
    return main_weather * third + cloud_weather * third + wind_score * third

# print(calc_full_weather(full_cities_obj_lst, full_cities_obj_lst[0].weather)) # remove


# Assign the weather to the city
def assign_weather_score(city_list):
    for city in city_list:
        city.weather_score = calc_full_weather(city_list, city.weather)
    return city_list

added_weather_score = assign_weather_score(full_cities_obj_lst)


# Assign priority scores to cities
def assign_priority_score(city_list):
    max_prt = 5
    for c in city_list:
        c.priority_score = int(c.priority) / max_prt
    return city_list

final_cities_lst = assign_priority_score(added_weather_score)


# Assign pilote scores to cities
def assign_pilote_score(pilots_list):
    max_skill = 10
    for p in pilots_list:
        p.pilote_score = p.skill_level / max_skill
    return pilots_list

final_pilote_obj = assign_pilote_score(all_pilots_obj)


# Calc fuel/distance per mission
def fuel_per_mission(fuel_capacity, distance):
    full_ability = 1
    calc_ability = full_ability - ((distance - fuel_capacity) / 1000)
    if fuel_capacity  > distance:
        return full_ability
    elif(calc_ability > 0):
        return calc_ability
    elif(calc_ability > 1):
        return 1
    return 0

print(fuel_per_mission(all_aircrafts_obj[0].fuel_capacity, final_cities_lst[3].distance))


# Create a mission list
all_missions = create_missions(final_cities_lst, all_aircrafts_obj, final_pilote_obj)


# Calc and assign mission score
def calc_mission_score(all_missions):
    score = 0
    pilote_and_priority = 1 / 5
    weather_and_fuel = 1 / 3
    for m in all_missions:
        score += m.city_target.weather_score * weather_and_fuel
        score += m.city_target.priority_score * pilote_and_priority
        score += m.pilote.skill_score * pilote_and_priority
        score += fuel_per_mission(m.aircraft.fuel_capacity, m.city_target.distance) * weather_and_fuel
        m.mission_score = score
        score = 0
    return all_missions


# List of full missions (including mission scores)
final_all_missions = (calc_mission_score(all_missions))

# sorted missions in descending order
sorted_missions = sorted(final_all_missions, key=lambda x: x.mission_score, reverse=True)
write_final_table_to_csv(sorted_missions)


