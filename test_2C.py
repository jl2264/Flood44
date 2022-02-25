
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():

    stations = []

    #make 6 similar stations 
    #change name and water level so that 4 will be in final list test by setting N to 4 at the end

    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s1.latest_level = 2.5   #in list
    s1.relative_water_level()

    s2 = MonitoringStation(
    station_id=2,
    measure_id=2,
    label='label2',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s2.latest_level = 2.9   #in list
    s2.relative_water_level()   

    s3 = MonitoringStation(
    station_id=3,
    measure_id=3,
    label='label3',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s3.latest_level = 0.9 #not in list
    s3.relative_water_level()   

    s4 = MonitoringStation(
    station_id=4,
    measure_id=4,
    label='label4',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s4.latest_level = 25    #in list
    s4.relative_water_level()

    s5 = MonitoringStation(
    station_id=5,
    measure_id=5,
    label='label5',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s5.latest_level = None    #not in list
    s5.relative_water_level()

    s6 = MonitoringStation(
    station_id=6,
    measure_id=6,
    label='label6',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s6.latest_level = 2.9    #in list
    s6.relative_water_level()
      
    stations.append(s1)
    stations.append(s2)
    stations.append(s3)
    stations.append(s4)
    stations.append(s5)
    stations.append(s6)

    list_test_2C = stations_highest_rel_level(stations, 4)

    assert len(list_test_2C) == 4   # only ten stations in list 

    #should also test [0] is s4, [3] is s1 
    assert list_test_2C[0] == (s4.name, s4.relative_water_level())
    assert list_test_2C[3] == (s1.name, s1.relative_water_level())

    #also test s5 with no water level data excluded
    assert (s5.name, s5.relative_water_level()) not in list_test_2C

test_stations_highest_rel_level()