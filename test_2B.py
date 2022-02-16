
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():

    stations = []

    #s1 level under threshold
    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(2,3),
    river='river',
    town='town')
    s1.latest_level = 2.5
    s1.relative_water_level()
    
    #s2 level over threshold
    s2 = MonitoringStation(
    station_id=2,
    measure_id=1,
    label='Long way away',
    coord=(float(2.2053), float(10.1218)),
    typical_range=(1,5),
    river='river',
    town='town')
    s2.latest_level = 4.9
    s2.relative_water_level()

    #s3 level on threshold so not in test list
    s3 = MonitoringStation(
    station_id=3,
    measure_id=1,
    label='label3',
    coord=(float(52.2153), float(0.1318)),
    typical_range=(2,3),
    river='river',
    town='town')
    s3.latest_level = 2.8
    s3.relative_water_level()

    #s4 level over threshold
    s4 = MonitoringStation(
    station_id=4,
    measure_id=1,
    label='label4',
    coord=(float(52.2153), float(0.1318)),
    typical_range=(0,1),
    river='river',
    town='town')
    s4.latest_level = 2.8
    s4.relative_water_level()

    #s5 no data
    s5 = MonitoringStation(
    station_id=5,
    measure_id=1,
    label='label5',
    coord=(float(52.2153), float(0.1318)),
    typical_range=None,
    river='river',
    town='town')
    s5.latest_level = None
    s5.relative_water_level()

    #s6 inconsistent range
    s6 = MonitoringStation(
    station_id=5,
    measure_id=1,
    label='label5',
    coord=(float(52.2153), float(0.1318)),
    typical_range=(3,2),
    river='river',
    town='town')
    s6.latest_level = 3
    s6.relative_water_level()


    stations.append(s1)
    stations.append(s2)
    stations.append(s3)
    stations.append(s4)
    stations.append(s5)
    stations.append(s6)


    list_test_2B = stations_level_over_threshold(stations, 0.8)

    assert len(list_test_2B) == 2   # only two stations in list 

    # should also test [0] is s4, [1] is s2 
    assert list_test_2B[0] == (s4.name, s4.relative_water_level())
    assert list_test_2B[1] == (s2.name, s2.relative_water_level())


test_stations_level_over_threshold()