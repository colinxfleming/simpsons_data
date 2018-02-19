import json
import os
import sys

import yaml

error_message = 'Please set an output format: yml json'

basedir = os.path.dirname(os.path.realpath(__file__))

try:
    output_format = sys.argv[1] if len(sys.argv) > 2 else 'json'
    list(['yml', 'json']).index(output_format)
    if not output_format:
        print(error_message)
        raise
except ValueError as e:
    print(error_message)
    raise(e)
except IndexError as e:
    print(error_message)
    raise(e)

all_data = {'episodes': [], 'characters': []}

seasons = os.listdir(os.path.join(basedir, 'episodes'))
for season in seasons:
    content = yaml.load(
        open(os.path.join(basedir, 'episodes', season)))
    all_data['episodes'] = all_data['episodes'] + content['episodes']

all_data['episodes'].sort(key=lambda x: (x['season'], x['episode']))

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
