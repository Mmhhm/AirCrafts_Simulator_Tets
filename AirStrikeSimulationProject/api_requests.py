import requests, json, load_files
# TODO shorten the for loop

# simple api request
def requet_to_json(url):
    request = requests.get(url).json()
    return request

# get all target cities coordinates
def get_city_lat_lon(cities: dict):
    all_cities_coordinates = {}
    latitude = "lat"
    longitude = "lon"
    dict_in_lst = 0
    for city in cities:
        city_name = city["City"]
        request = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&APPID=67426bc9e51f120382ea5da6ca877eef').json()
        all_cities_coordinates[city_name] = {latitude : request[dict_in_lst][latitude], longitude : request[dict_in_lst][longitude]}
    return all_cities_coordinates

# x = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=Jerusalem&APPID=67426bc9e51f120382ea5da6ca877eef').json()
#
# print(x[0]["lat"])


## reqest all cities coordinates
# all_cities_coordinates = get_city_lat_lon(objects.csv_read_dict('air_strike_targets.csv'))
# print(all_cities_coordinates)


# filter the specified time, out of json request
def filter_weather_time(all_weather):
    specified_time = "2024-09-13 00:00:00"
    filtered_time = list(filter(lambda x: x["dt_txt"] == specified_time, all_weather["list"]))
    return filtered_time

# get all cities weather
def get_cities_weather(cities: dict):
    all_cities_weather = {}
    dict_in_lst = 0
    for city in cities:
        city_name = city["City"]
        request = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&APPID=67426bc9e51f120382ea5da6ca877eef').json()
        specified_time = filter_weather_time(request)
        all_cities_weather[city_name] = {"weather" : specified_time[dict_in_lst]['weather'][0]['main'], "clouds" : specified_time[dict_in_lst]['clouds']['all'], "wind" : specified_time[dict_in_lst]['wind']['speed']}
    return all_cities_weather

# all_cities_weather = (get_cities_weather(objects.csv_read_dict('air_strike_targets.csv')))
#
#
# # # dump the distances to json file, so that I won't have to use api requests
# with open("cities_weather.json", "w") as outfile:
#     json.dump(all_cities_weather, outfile)