import json
import os
# import sys

import yaml

# error_message = 'Please set an output format: yml json'

basedir = os.path.dirname(os.path.realpath(__file__))

output_format = 'json'  # hardsetting fornow
# try:
#     output_format = sys.argv[1] if len(sys.argv) > 2 else 'json'
#     list(['yml', 'json']).index(output_format)
#     if not output_format:
#         print(error_message)
#         raise
# except ValueError as e:
#     print(error_message)
#     raise(e)
# except IndexError as e:
#     print(error_message)
#     raise(e)

all_data = {'episodes': [], 'characters': []}

for datatype in all_data.keys():
    data_files = os.listdir(os.path.join(basedir, datatype))
    for f in data_files:
        content = yaml.load(
            open(os.path.join(basedir, datatype, f)))
        all_data[datatype] = all_data[datatype] + content[datatype]

# Individual sorting rules
all_data['episodes'].sort(key=lambda x: (x['season'], x['episode']))
all_data['characters'].sort(key=lambda x: (x['short_name']))

# Turn all 'maybe' good episodes to bad episodes
for index, ep in enumerate(all_data['episodes']):
    if all_data['episodes'][index]['good'] == 'maybe':
        all_data['episodes'][index]['good'] = False

if output_format == 'yml':
    raise ValueError('not yet, sorry. just json for now')
    # output = yaml.dump(all_data)
elif output_format == 'json':
    output = json.dumps(all_data, indent=4)
else:
    raise ValueError('????')


output_file = 'simpsons_data.{}'.format(output_format)
with open(os.path.join(basedir, output_file), 'w') as f:
    f.write(output)

print('Compilation complete in {}'.format(output_format))
