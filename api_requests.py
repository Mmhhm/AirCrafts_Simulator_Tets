# import requests
# # TODO shorten the for loop
# def get_city_lat_lon(cities: dict):
#     all_cities_coordinates = {}
#     latitude = "lat"
#     longitude = "lon"
#     dict_in_lst = 0
#     for city in cities.values():
#         city_name = city
#         request = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&APPID=67426bc9e51f120382ea5da6ca877eef').json()
#         all_cities_coordinates[city_name] = {latitude : request[dict_in_lst][latitude], longitude : request[dict_in_lst][longitude]}
#     return all_cities_coordinates
#
# # x = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=Jerusalem&APPID=67426bc9e51f120382ea5da6ca877eef').json()
# #
# # print(x[0]["lat"])
#
# print(get_city_lat_lon(csv_read_dict('air_strike_targets.csv')))