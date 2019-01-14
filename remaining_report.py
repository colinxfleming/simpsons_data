#!/usr/bin/env python

"""A quick and dirty script to log what episodes still need review."""

import os

import yaml

basedir = os.path.dirname(os.path.realpath(__file__))

all_data = {'episodes': [], 'characters': []}

for datatype in all_data.keys():
    data_files = os.listdir(os.path.join(basedir, datatype))
    for f in data_files:
        content = yaml.load(
            open(os.path.join(basedir, datatype, f)))
        all_data[datatype] = all_data[datatype] + content[datatype]

all_data['episodes'].sort(key=lambda x: (x['season'], x['episode']))
all_data['characters'].sort(key=lambda x: (x['short_name']))

print('***EPISODE GOODNESS/BADNESS TO REVIEW***\n')
for ep in all_data['episodes']:
    if isinstance(ep['good'], str):
        print(f"{ep['season']}-{ep['episode']} - {ep['title']}")

print('\nEPISODES TO LOG CHARACTERS')
for ep in all_data['episodes']:
    if ep['characters'] is None:
        print(f"{ep['season']}-{ep['episode']} - {ep['title']}")
