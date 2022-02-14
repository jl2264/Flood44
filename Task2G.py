from floodsystem.stationdata import build_station_list
import datetime
import matplotlib.pyplot as plt
from pytest import skip
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
import numpy as np



def risk_river(river,stations):
    
    dt = 5
    p = 5

    for station in stations:
        if station.river == river:
            print (station.river)
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, p)