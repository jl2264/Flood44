
from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation

def test_rivers_with_station_no_duplicate():
    
    stations = []

    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(52.2053), float(0.1218)),
    typical_range='typical_range',
    river='river1',
    town='town')

    s2 = MonitoringStation(
    station_id=2,
    measure_id=1,
    label='label2',
    coord=(float(2.2053), float(10.1218)),
    typical_range='typical_range',
    river='river2',
    town='town')

    s3 = MonitoringStation(
    station_id=3,
    measure_id=1,
    label='label3',
    coord=(float(52.2153), float(0.1318)),
    typical_range='typical_range',
    river='river3',
    town='town')

    stations.append(s1)
    stations.append(s2)
    stations.append(s3)

    list_test_1D = rivers_with_station(stations)

    assert len(list_test_1D) == 3   # all of the station rivers


def test_rivers_with_station_with_duplicate():
    
    stations = []

    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(52.2053), float(0.1218)),
    typical_range='typical_range',
    river='river1',
    town='town')

    s2 = MonitoringStation(
    station_id=2,
    measure_id=1,
    label='label2',
    coord=(float(2.2053), float(10.1218)),
    typical_range='typical_range',
    river='river2',
    town='town')

    s3 = MonitoringStation(
    station_id=3,
    measure_id=1,
    label='label3',
    coord=(float(52.2153), float(0.1318)),
    typical_range='typical_range',
    river='river1',
    town='town')

    stations.append(s1)
    stations.append(s2)
    stations.append(s3)

    list_test_1D = rivers_with_station(stations)

    assert len(list_test_1D) == 2   # all of the station rivers with one duplicate
    assert list_test_1D[0] == s1.river
    assert list_test_1D[1] == s2.river
    assert s1.river == s3.river
