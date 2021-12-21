def point2json(coord):
    return {
        "position": [coord[0], coord[1], coord[2]]
    }

import json
import numpy as np

points = []
f = open('data.txt', 'r')
point = f.readline()
while point:
    coord = np.array(point.split(), dtype=float)
    points.append(point2json(coord))
    point = f.readline()

f.close()

with open('data.json', 'w') as outf:
    outf.write(json.dumps(points, indent=4, separators=(',', ': ')))

outf.close()

