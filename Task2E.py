
from dataclasses import replace
import datetime
from os import remove
import matplotlib.pyplot as plt
from pytest import skip
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    dt = 10
    
    stations_N = (stations_highest_rel_level (stations, N))
    list = []

    for i in stations_N:
        list.append(i[0])

    list_1 = []
    for station in stations:
        if station.name in list:
            list_1.append(station)
    
    for station in list_1:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0:
            print(station.name,'data error')
        else:
            plot_water_levels(station,dates,levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
