import json

def findStations():
    city_cover = set(json.loads(input()))

    stations = {}

    for _ in range(int(input())):
        data = json.loads(input())
        stations[data["Name"]] = set(data["Cities"])

    selected_stations = []

    while city_cover:
        best_station = max(stations, key=lambda s: len(stations[s] & city_cover))

        covered = stations[best_station] & city_cover

        if not covered:
            break

        city_cover -= covered
        
        selected_stations.append(best_station)

    print(sorted(selected_stations))



findStations()