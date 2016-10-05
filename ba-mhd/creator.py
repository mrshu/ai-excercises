import json
import requests
import re

bus_stops = {}
data = (json.load(open('export.geojson')))
for x in data['features']:
    name = x['properties']['name']
    coords = x['geometry']['coordinates']
    if name not in bus_stops:
        bus_stops[name] = coords

interesting_lines = [20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 37,
                     39, 41, 43, 44, 50, 51, 52, 53, 54, 56, 57, 58, 59, 61,
                     63, 65, 66, 67, 68, 69, 70, 74, 75, 77, 78, 79, 80, 83,
                     84, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 123, 130,
                     133, 139, 147, 151, 153, 184, 191, 192, 196, 1, 2,
                     3, 4, 5, 6, 7, 8, 9, 33, 64, 201, 202, 203, 204, 205, 207,
                     208, 209, 210, 211, 212]
neighbors = {}


def add_neighbor(neighbors, current, next):
    if current in neighbors:
        if next not in neighbors[current]:
            neighbors[current].append(next)
    else:
        neighbors[current] = [next]
    return neighbors

for line in interesting_lines:
    url = 'http://imhd.sk/ba/cestovny-poriadok/linka/{}'.format(line)
    r = requests.get(url)
    m = re.search(r'class="theader1"(.*)<td width="5">&nbsp;</td>', r.text)
    print url
    text = m.group(0)
    stops = re.findall(r'<a href="/ba/cestovny-poriadok/[^>]*>(.*?)</a>', text)
    for i in range(1, len(stops)):
        current = stops[i-1]
        next = stops[i]
        if current in bus_stops and next in bus_stops:
            neighbors = add_neighbor(neighbors, current, next)
            neighbors = add_neighbor(neighbors, next, current)

ba_mhd_db = {'neighbors': neighbors, 'bus_stops': bus_stops}
json.dump(ba_mhd_db, open('ba_mhd_db.json', 'w'))
