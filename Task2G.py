from floodsystem.stationdata import build_station_list
import datetime
import matplotlib
import matplotlib.pyplot as plt
from pytest import skip
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level_2G, stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels, relative_level_rising_rate
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2 #over past 2 days to give warnings for most recent data

    N = 40 #only include 40 highest, rule out other stations for highest risk at this point
    p=2
    #use stations_highest_rel_level to shortlist 40 stations to be tested (prevents unnecessary calculations)
    stations_N = (stations_highest_rel_level(stations, N)) #create list of stations and relative water levels

    relative_water_level_list = []
    not_ruled_out = []
    for i in stations_N:
        not_ruled_out.append(i[0]) #create list of names of shortlisted stations
    list_1 = [] #create list of shortlisted stations
    for station in stations:
        if station.name in not_ruled_out:
            list_1.append(station)

    overall_list = []
    updated_relative_level_list = []
    for station in list_1:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        #skip any stations with unavailable data
        if len(matplotlib.dates.date2num(dates)) == 0:
            skip
        elif station.relative_water_level == None:
            skip
        #create list containing (station name, rate of rising water level, relative water level) for shortlisted stations
        else:
            overall_list.append([station.name, station.relative_water_level(), relative_level_rising_rate(station, dates, levels)])
    #calculate risk index (relative water level + 15*relative rising rate of water level)
    risk_index_list = []
    for i in overall_list:
        risk_factor = i[1]+15*i[2]
        if risk_factor <= -5:
            risk_index_list.append([i[0], risk_factor, 'Low'])
        elif risk_factor <= 0:
            risk_index_list.append([i[0], risk_factor, 'Moderate'])
        elif risk_factor <= 4.2:
            risk_index_list.append([i[0], risk_factor, 'High'])
        elif risk_factor > 4.2:
            risk_index_list.append([i[0], risk_factor, 'Severe'])
    print('The towns listed have been assessed to be at highest risk of flooding. ' + 
    '\n The format of the list is: station name, flood risk index, risk rating (low/moderate/high/severe).' +
    '\n Risk index = relative water level + 15 * rate of change of relative water level for 20 most recent water level readings.')
    print(risk_index_list)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()