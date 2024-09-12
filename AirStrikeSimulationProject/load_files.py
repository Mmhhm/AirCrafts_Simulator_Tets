import json
import csv

def csv_read_lst(file_path):
    with open(file_path, mode ='r') as file:
      csvFile = list(csv.reader(file))
      # for lines in csvFile:
    return csvFile

def csv_read_dict(file_path):
    with open(file_path, mode='r') as file:
        csvFile = list(csv.DictReader(file))
        # for lines in csvFile:
    return csvFile

# Open and read the JSON
def load_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

# File paths
pilots_path = 'pilots.json'
aircrafts_path = 'aircrafts.json'
city_targets_path = 'air_strike_targets.csv'

# Save to dict
pilots_dict = load_json(pilots_path)
aircrafts_dict = load_json(aircrafts_path)
city_targets_dict =  csv_read_dict(city_targets_path)
print(pilots_dict)
print(aircrafts_dict)
print(city_targets_dict)




