from attr import define
from numpy import append
from pytest import Item
from sympy import N
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
import floodsystem.station


def rivers_monitored():
    stations = build_station_list()
    rivers_full = rivers_with_station(stations)
    rivers_full.sort()
    print(len(rivers_full),'First 10 - ', rivers_full[:10], '\n\n\n\n')
    return rivers_full


def stations_by_River_1D():
    stations = build_station_list()
    dict_stations_1D = stations_by_river(stations)
    print ('River Aire - ', dict_stations_1D['River Aire'], '\n\n', 'River Cam - ', dict_stations_1D['River Cam'],'\n\n', 'River Thames - ', dict_stations_1D['River Thames'])
    return dict_stations_1D



def run():
    rivers_monitored()
    # Put code here that demonstrates functionality

if __name__ == "__main__":
    run()

def run():
    stations_by_River_1D()
    # Put code here that demonstrates functionality

if __name__ == "__main__":
    run()
