#!/usr/bin/env python

"""A quick and dirty script to log what episodes still need review."""

import os

import yaml

basedir = os.path.dirname(os.path.realpath(__file__))

all_data = {"episodes": []}

for datatype in all_data.keys():
    data_files = os.listdir(os.path.join(basedir, datatype))
    for f in data_files:
        content = yaml.safe_load(open(os.path.join(basedir, datatype, f)))
        all_data[datatype] = all_data[datatype] + content[datatype]

all_data["episodes"].sort(key=lambda x: (x["season"], x["episode"]))
all_keys = all_data['episodes'][0].keys()
for ep in all_data["episodes"]:
    s = f"{ep['season']}-{ep['episode']} - {ep['title']}"
    for k in all_keys:
        if ep[k] is None:
            print(f"{s} - MISSING {k}")
