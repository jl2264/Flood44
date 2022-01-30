from attr import define
from numpy import append
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():

    stations = build_station_list()
    # Build list of stations
    
    p = (52.2053, 0.1218)
    # Coordinate of Cambridge

    list_cam = stations_by_distance(stations, p)

    print('10 closest stations from  the Cambridge city centre : ', list_cam[:10], '\n\n')
    print('10 furthest stations from the Cambridge city centre : ', list_cam[-10:])

if __name__ == "__main__":
    print("\n *** Task 1B: sort stations by distance *** \n")
    run()