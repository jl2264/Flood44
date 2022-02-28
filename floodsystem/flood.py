
from pytest import skip
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    list = []
    for i in stations:
        if i.relative_water_level() == None:
            skip
        elif i.relative_water_level() > tol:
            list.append((i.name, i.relative_water_level()))
    return sorted_by_key(list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    list = []
    for i in stations:
        if i.relative_water_level() == None:
            skip
        else:
             list.append((i.name, i.relative_water_level()))
    return sorted_by_key(list, 1, reverse=True)[:N]

#calculate relative water level for each station, return list of names and level sorted alphabetically
def stations_highest_rel_level_2G(stations):
    list = []
    for i in stations:
        if i.relative_water_level() == None:
            skip
        else:
             list.append((i.name, i.relative_water_level()))
    return sorted_by_key(list, 0)
