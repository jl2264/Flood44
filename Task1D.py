from attr import define
from numpy import append
from pytest import Item
from sympy import N
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()

    rivers_full = rivers_with_station(stations)
    rivers_full.sort()

    dict_stations_1D = stations_by_river(stations)

    print('Numbers of rivers monitored : ', len(rivers_full), '\n First 10 - ', rivers_full[:10], '\n\n')
    
    print('River Aire : ', dict_stations_1D['River Aire'], '\n\n', 'River Cam : ', dict_stations_1D['River Cam'],'\n\n', 'River Thames : ', dict_stations_1D['River Thames'])



if __name__ == "__main__":
    print("\n *** Task 1D: rivers with a station(s) *** \n")
    run()
