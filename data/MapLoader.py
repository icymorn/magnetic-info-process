import json
from algorithm.PassFilter import low_filter, high_filter

def loadRouteFromMap(mapName, routeName, direction = 1):
    mapData = json.load(open(mapName, 'rb'))
    for route in mapData['graphEdge']:
        if route['name'] == routeName:
            routes = route['fingerdata']
            for n in range(len(routes)):
                routes[n] = high_filter(low_filter(routes[n]))
            return route
    return None

def main():
    mapDirectory = '/home/moe/PycharmProjects/dingge/app/map/'
    print loadRouteFromMap(mapDirectory + 'map_1.json', 'A-B')

if __name__ == '__main__':
    main()
