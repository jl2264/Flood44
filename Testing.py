
import datetime
from inflection import camelize
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from Task2G import risk_river

def run():
    stations = build_station_list
    river = 'Cam'
    risk_river(river,stations)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
