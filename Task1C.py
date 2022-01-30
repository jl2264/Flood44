from attr import define
from numpy import append
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
   
def run():
   
    stations = build_station_list()
    r = 10
    centre = (52.2053, 0.1218)


    list_stations_within_radius_cam = stations_within_radius(stations, centre, r)
    print('Stations within 10 km of the Cambridge city centre : ', list_stations_within_radius_cam)


if __name__ == "__main__":
    print("\n *** Task 1C: stations within radius *** \n")
    run()