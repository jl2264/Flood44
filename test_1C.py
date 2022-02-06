
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation

def test_stations_within_radius():
    
    stations = []

    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(52.2053), float(0.1218)),
    typical_range='typical_range',
    river='river',
    town='town')

    s2 = MonitoringStation(
    station_id=2,
    measure_id=1,
    label='Long way away',
    coord=(float(2.2053), float(10.1218)),
    typical_range='typical_range',
    river='river',
    town='town')

    s3 = MonitoringStation(
    station_id=3,
    measure_id=1,
    label='label3',
    coord=(float(52.2153), float(0.1318)),
    typical_range='typical_range',
    river='river',
    town='town')

    stations.append(s1)
    stations.append(s2)
    stations.append(s3)

    list_test_1C = stations_within_radius(stations, (52.2053, 0.1218),10)

    assert len(list_test_1C) == 2   # only two - s2 too far

    # should also test [0] is s1 and [1] is s3
    assert list_test_1C[0] == 'label1'
    assert list_test_1C[1] == 'label3'


