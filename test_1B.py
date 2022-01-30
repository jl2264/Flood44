
from re import X
from attr import define
from numpy import append
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import numpy as np

def test_stations_by_distance():

    stations = build_station_list()
    p = np.random.rand(2)
    list_test_1B = stations_by_distance(stations, p)

    assert len(list_test_1B) > 0
    
    for x in range(len(list_test_1B)-1):
        assert (list_test_1B[x])[2] <= (list_test_1B[x+1])[2]

