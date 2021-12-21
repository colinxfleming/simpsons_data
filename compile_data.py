#!/usr/bin/env python

import json
import os

import yaml

basedir = os.path.dirname(os.path.realpath(__file__))

all_data = {'episodes': []}

for datatype in all_data.keys():
    data_files = os.listdir(os.path.join(basedir, datatype))
    for f in data_files:
        content = yaml.load(
            open(os.path.join(basedir, datatype, f)))
        all_data[datatype] = all_data[datatype] + content[datatype]

# Individual sorting rules
all_data['episodes'].sort(key=lambda x: (x['season'], x['episode']))

for index, ep in enumerate(all_data['episodes']):
    # Turn all 'maybe' good episodes to bad episodes
    if all_data['episodes'][index]['good'] == 'maybe':
        all_data['episodes'][index]['good'] = False

    # Turn all empty guest star arrays to [] from nil
    if all_data['episodes'][index]['guest_stars'] is None:
        all_data['episodes'][index]['guest_stars'] = []

output = json.dumps(all_data, indent=4)
output_file = 'simpsons_data.json'
with open(os.path.join(basedir, output_file), 'w') as f:
    f.write(output)

print('Compilation complete - simpsons_data.json')
