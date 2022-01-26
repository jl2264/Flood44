from attr import define
from numpy import append
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import floodsystem.station

def stations_from_cam():
    stations = build_station_list()
    p = (52.2053, 0.1218)

    list_cam = stations_by_distance(stations, p)
    print(list_cam[:10])
    print(list_cam[-10:])
    return list_cam

def run():
    stations_from_cam()
    # Put code here that demonstrates functionality

if __name__ == "__main__":
    run()