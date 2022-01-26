from attr import define
from numpy import append
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import floodsystem.station


def stations_within_radius_cam():
    stations = build_station_list()
    r = 10
    centre = (52.2053, 0.1218)
    list_stations_within_radius_cam = stations_within_radius(stations, centre, r)
    print(list_stations_within_radius_cam)
    return list_stations_within_radius_cam


def run():
    stations_within_radius_cam()
    # Put code here that demonstrates functionality

if __name__ == "__main__":
    run()