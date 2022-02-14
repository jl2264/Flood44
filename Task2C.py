
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    N = 10
    update_water_levels(stations)
    list_2C = stations_highest_rel_level (stations, N)
    
    print (N, 'highest water level stations: ', list_2C)
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
