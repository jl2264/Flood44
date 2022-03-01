
from floodsystem.station import MonitoringStation
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels, relative_level_rising_rate
from dateutil.tz import tzutc
from dataclasses import replace
from os import remove
import matplotlib
import numpy as np


def test_relative_level_rising_rate():

    #create fake station s1 (has same typical range and latet level as Hayes Basin, but not necessary)
    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='Test Station',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(0.91,0.97),
    river='river',
    town='town')
    s1.latest_level = 1.536


    #create arbitrary dates
    dates_2G = [datetime.datetime(2022, 2, 28, 12, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 11, 45, tzinfo=tzutc()),
        datetime.datetime(2022, 2, 28, 11, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 11, 15, tzinfo=tzutc()),
        datetime.datetime(2022, 2, 28, 11, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 10, 45, tzinfo=tzutc()),
        datetime.datetime(2022, 2, 28, 10, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 10, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 10, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 9, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 9, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 9, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 9, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 8, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 8, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 8, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 8, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 7, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 7, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 7, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 7, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 6, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 6, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 6, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 6, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 5, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 5, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 5, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 5, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 4, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 4, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 4, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 4, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 3, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 3, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 3, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 3, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 2, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 2, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 2, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 2, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 1, 45, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 1, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 1, 15, tzinfo=tzutc()), 
        datetime.datetime(2022, 2, 28, 1, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 0, 45, tzinfo=tzutc())]

    #water level at station s1 do not change (have constant level = 1)
    levels_2G = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 
        1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 
        1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 
        1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 
        1.00, 1.00, 1.00, 1.00, 1.00, 1.00] 

    #rate of relative water level rise should be zero
    assert relative_level_rising_rate(s1, dates_2G, levels_2G) == 0

test_relative_level_rising_rate()