import json
import csv

# Read csv file into list
def csv_read_lst(file_path):
    with open(file_path, mode ='r') as file:
      csvFile = list(csv.reader(file))
    return csvFile

# Read csv file into dict
def csv_read_dict(file_path):
    with open(file_path, mode='r') as file:
        csvFile = list(csv.DictReader(file))
    return csvFile

# Read JSON file into dict
def load_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def write_final_table_to_csv(all_missions):
    with open('mission_table.csv', 'w',) as file:
        writer = csv.writer(file)
        writer.writerow(['Target Name', 'Priority', 'Assigned Pilot, Assigned AirCraft',
                        'Distance', 'Weather Conditions', 'Pilot Skill', 'Aircraft Speed',
                         'Fuel Capacity', 'Mission Fit Score'])
        for m in all_missions:
            writer.writerow([m.city_target.city, m.city_target.priority, m.pilote.name,
                             m.aircraft.type, int(m.city_target.distance), m.city_target.weather['weather'],
                             m.pilote.skill_level, m.aircraft.speed, m.aircraft.fuel_capacity, round(m.mission_score, 2)])
    print("Yes, we did it!!!")


# File paths
pilots_path = 'pilots.json'
aircrafts_path = 'aircrafts.json'
city_targets_path = 'air_strike_targets.csv'

# Save to dict
pilots_dict = load_json(pilots_path)
aircrafts_dict = load_json(aircrafts_path)
city_targets_dict = csv_read_dict(city_targets_path)

# Print for testing
print(pilots_dict)
print(aircrafts_dict)
print(city_targets_dict)




