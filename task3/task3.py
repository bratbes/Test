import json
import pprint
import sys
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

print(sys.argv)

vdata = read_json(sys.argv[1])
tdata = read_json(sys.argv[2])
vdict = {}

def fill_data(data):
    if isinstance(data,dict):
        for key, value in data.items():
            if key == 'id':
                for i in range(len(vdata['values'])):
                    if value == vdata['values'][i]['id']:
                        vdict[vdata['values'][i]['id']] = vdata['values'][i]['value']
                        data['value'] = vdict[vdata['values'][i]['id']]
            elif isinstance(value, dict):
                data['value'] = vdata[value]
            elif isinstance(value, list):
                for item in value:
                    fill_data(item)
    elif isinstance(data, list):
        for item in data:
            fill_data(item)

fill_data(tdata)

with open('report.json', 'w') as file:
    data = json.dump(tdata, file, indent = 4)