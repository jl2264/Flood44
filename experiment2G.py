from floodsystem.stationdata import build_station_list
import datetime
import matplotlib
import matplotlib.pyplot as plt
from pytest import skip
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level_2G
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels, relative_level_rising_rate
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 1 #over past 2 days to give warnings for most recent data
    p=2

    stations_N = (stations_highest_rel_level_2G(stations)) #create list of stations and relative water levels

    #relative_water_level_list = []
    #for i in stations_N:
    #    relative_water_level_list.append(i[1]) #create list of relative water levels

    '''trial_station = stations[10]
    print(trial_station)
    dates2, levels2 = fetch_measure_levels(trial_station.measure_id, dt=datetime.timedelta(days=dt))
    if len(dates2) == 0:
        skip
    else:
        print(relative_level_rising_rate(trial_station, dates2, levels2))'''
    
    overall_rates_of_change_list = []
    
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if len(matplotlib.dates.date2num(dates)) == 0:
            skip
        elif station.relative_water_level == None:
            skip
        else:
            #print(relative_level_rising_rate(station, dates, levels))
            overall_rates_of_change_list.append(relative_level_rising_rate(station, dates, levels))
    print(overall_rates_of_change_list)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()