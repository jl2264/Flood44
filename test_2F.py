from floodsystem.station import MonitoringStation

import matplotlib
from dateutil.tz import tzutc
from dataclasses import replace
import datetime
from os import remove
import matplotlib.pyplot as plt
from pytest import skip
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
import numpy as np


def test_plot_water_level_with_fit():

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

    #create fake station s2 (has different typical range and latest level than s2)
    s2 = MonitoringStation(
    station_id=2,
    measure_id=2,
    label='Test Station 2',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(1.91,1.97),
    river='river',
    town='town')
    s1.latest_level = 0.536

    #create arbitrary dates (in this case taken from Hayes Basin on 28th February)
    dates = [datetime.datetime(2022, 2, 28, 12, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 11, 45, tzinfo=tzutc()),
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
    
    #create arbitrary levels (in this case taken from Hayes Basin on 28th February)
    levels = [1.536, 1.54, 1.541, 1.549, 1.558, 1.561, 1.567, 1.569, 1.574, 1.58, 1.587, 
        1.593, 1.598, 1.603, 1.609, 1.613, 1.619, 1.623, 1.627, 1.633, 1.638, 1.642, 1.646, 
        1.65, 1.654, 1.66, 1.665, 1.668, 1.673, 1.678, 1.682, 1.687, 1.691, 1.695, 1.7, 1.703, 
        1.707, 1.711, 1.716, 1.719, 1.723, 1.727, 1.731, 1.736, 1.74, 1.77]

    levels2 = [1.00, 1.00, 1.00, 1.00, 2.00, 2.00, 2.00, 2.00, 1.00, 1.00, 
        1.00, 1.00, 2.00, 2.00, 2.00, 2.00, 1.00, 1.00, 1.00, 1.00, 
        2.00, 2.00, 2.00, 2.00, 1.00, 1.00, 1.00, 1.00, 2.00, 2.00, 
        2.00, 2.00, 1.00, 1.00, 1.00, 1.00, 2.00, 2.00, 2.00, 2.00, 
        1.00, 1.00, 1.00, 1.00, 2.00, 2.00]

    #plot first test graph, p = 4
    test_graph_1 = plot_water_level_with_fit(s1, dates, levels, 4)
    #plot second test graph, has very spiky data, p = 4
    test_graph_2 = plot_water_level_with_fit(s2, dates, levels2, 4)
    #can see that when p (degree of polynomial) increased, best-fit polynomial matches data more closely
    test_graph_2 = plot_water_level_with_fit(s2, dates, levels2, 20)

    #convert dates to floats so they can be worked with as function arguments
    dates_converted = matplotlib.dates.date2num(dates)  

    #calculate gradient and round to avoid any potential floating point error
    gradient_1 = round((levels[45] - levels[0])/(dates_converted[45]-dates_converted[0]), 8)
    gradient_2 = round((levels2[45] - levels2[0])/(dates_converted[45]-dates_converted[0]))
    assert gradient_1 == -0.4992 #graph 1 has knwon calculated gradient of -0.4992, check this is consistent
    assert gradient_2 == -2 #graph 2 has knwon calculated gradient of -2, check this is consistent

test_plot_water_level_with_fit()