# создать и записать json
# sys.stdin

import json
import sys

OUT_FILE = 'test.json'

# cat - 5; parrot - 2; lemur - 11
# lion - 1; monkey - 2; snail - 1
# dog - 5; cabbage - -1; dolphin - 6
# python - 11

# {'c': {'cat': 5, 'cabbage': -1}, 'l': {'lemur': 11, 'lion': 1}, ...}

d = {}
likes = {'low': {}, 'middle': {}, 'high': {}}
for line in sys.stdin:
    for elem in line.rstrip('\n').split('; '):
        animal, number = elem.split(' - ')
        number = int(number)
        # if animal[0] not in d:
        #     d[animal[0]] = {}
        # d[animal[0]][animal] = number
        d.setdefault(animal[0], dict())[animal] = number
        if number < 2:
            likes['low'][animal] = number
        elif number > 7:
            likes['high'][animal] = number
        else:
            likes['middle'][animal] = number
# print({x: y for x, y in sorted(d.items())})
# print(dict(sorted(d.items())))
with open(OUT_FILE, 'w') as out_json:
    print(json.dumps(d))
    json.dump(likes, out_json)
