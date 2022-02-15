# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from audioop import reverse
from haversine import haversine
from pytest import skip
from sqlalchemy import true
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):

    list_stations_distance = []
    for i in stations:
        stations_distance = haversine (i.coord,  p)
        list_stations_distance.append((i.name, i.town, stations_distance))
    return sorted_by_key(list_stations_distance, 2)

def stations_within_radius(stations, centre, r):
    list_station_in_radius = []
    for i in stations:
        if haversine(i.coord, centre) < r:
            list_station_in_radius.append(i.name)
        else:
            skip
    list_station_in_radius.sort()
    return list_station_in_radius

def rivers_with_station(stations):
    list_rivers = []
    for i in stations:
        if i.river in list_rivers:
            skip
        else:
            list_rivers.append(i.river)
    
    return list_rivers

def stations_by_river(stations):
    dict_stations_by_river = {}
    for i in stations:
        if i.river in dict_stations_by_river:
           lista = dict_stations_by_river[i.river]
           lista.append(i.name)
           lista.sort()
           dict_stations_by_river[i.river] = lista
        else:
            dict_stations_by_river[i.river] = [i.name]
    
    return dict_stations_by_river

def rivers_by_station_number(stations, N):
    dict_rivers_station_no = {}
    for i in stations:
        if i.river in dict_rivers_station_no:
            dict_rivers_station_no[i.river] += 1
        else:
            dict_rivers_station_no[i.river] = 1
    list_rivers_station_no = list(dict_rivers_station_no.items())
    list_rivers_station_no =  sorted_by_key(list_rivers_station_no, 1, reverse=True)

    #list_rivers_station_no.reverse()
    #list_rivers_station_no = sorted(dict_rivers_station_no.items() , reverse=True, key=lambda x: x[1])
    '''print(list_rivers_station_no)'''
    if N == len(list_rivers_station_no):
        return list_rivers_station_no
    else:
        while (list_rivers_station_no[N-1])[1] == (list_rivers_station_no[N])[1]:
            N += 1
            if N == len(list_rivers_station_no):
                break
    list_N_rivers_station_no = list_rivers_station_no[:N]

    return list_N_rivers_station_no

     

