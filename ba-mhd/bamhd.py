import json
from math import radians, cos, sin, asin, sqrt


class BaMHD(object):
    def __init__(self, db_file='ba_mhd_db.json'):
        self.data = json.load(open(db_file, 'r'))

    def distance(self, stop1, stop2):
        """Return distance between two stops in km."""
        coords1 = self.data['bus_stops'][stop1]
        coords2 = self.data['bus_stops'][stop2]

        def haversine(lon1, lat1, lon2, lat2):
            """
            Calculate the great circle distance between two points
            on the earth (specified in decimal degrees)

            Courtesy of http://stackoverflow.com/a/15737218
            """
            # convert decimal degrees to radians
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            km = 6367 * c
            return km

        return haversine(coords1[0], coords1[1], coords2[0], coords2[1])

    def neighbors(self, stop):
        """Return neighbors for a given stop"""
        return self.data['neighbors'][stop]

    def stops(self):
        return self.data['bus_stops'].keys()


def find_shortest_path(bamhd, stopA, stopB):
    """Find a path between two MHD stops in Bratislava. Return a list of MHD
    stops."""
    return []

if __name__ == "__main__":
    bamhd = BaMHD()
    print 'Zoo' in bamhd.stops()
    print bamhd.distance('Avion - IKEA', 'Cvernovka')
    print find_shortest_path(bamhd, 'Zoo', 'Avion - IKEA')
