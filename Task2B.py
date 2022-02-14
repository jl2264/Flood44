
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    tol = 0.8
    update_water_levels(stations)
    list_2B = stations_level_over_threshold (stations, tol)
    
    print ('Stations relative water level >', tol, ': ', list_2B)
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
