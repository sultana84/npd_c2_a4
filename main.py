import json
import csv
import yaml
from pprint import pprint

FILENAME_JSON = 'input.json'
FILENME_CSV = 'input.csv'
FILENAME_YAML = 'input.yaml'

with open(FILENAME_JSON, 'r') as json_file:
    json_data = json.load(json_file)
pprint(json_data)

with open(FILENAME_YAML, 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)
pprint(yaml_data)

with open(FILENAME_CSV, 'r') as csv_file:
    reader = csv.reader(csv_file)
    names = next(reader)
    lines = [l for l in reader]

print(names)
print(lines)
