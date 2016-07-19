import json
import csv
import yaml
from pprint import pprint

#FILENAME_JSON = 'input.json'
FILENAME_CSV = 'input.csv'
FILENAME_YAML = 'input.yaml'

#with open(FILENAME_JSON, 'r') as json_file:
#    json_data = json.load(json_file)
#pprint(json_data)

with open(FILENAME_YAML, 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)

yaml_list_dicts = yaml_data['data']

with open(FILENAME_CSV, 'r') as csv_file:
    reader = csv.reader(csv_file)
    names = next(reader)
    lines = [l for l in reader]

csv_list_dicts = [
    {
        names[col_num]: col_val
        for col_num, col_val in enumerate(line)
    } for line in lines
]

combined_list_of_dicts = yaml_list_dicts + csv_list_dicts

# Output combined data into a csv file
with open('output.csv', 'w') as csv_out:
    header = ','.join(names)
    csv_out.write(header + '\n')
    for dict_val in combined_list_of_dicts:
        row_list = [str(dict_val[name]) for name in names]
        row_string = ','.join(row_list)
        csv_out.write(row_string + '\n')

# Output combined data into a JSON file
with open('output.json', 'w') as json_out:
    json.dump(combined_list_of_dicts, json_out)


