
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def test_inconsistent_typical_range_stations():
    
    stations = []

    s1 = MonitoringStation(
    station_id=1,
    measure_id=1,
    label='label1',
    coord=(float(52.2053), float(0.1218)),
    typical_range=(3,2), #inconsistent
    river='river',
    town='town')

    s2 = MonitoringStation(
    station_id=2,
    measure_id=1,
    label='label2',
    coord=(float(2.2053), float(10.1218)),
    typical_range=(None),
    river='river',
    town='town')

    s3 = MonitoringStation(
    station_id=3,
    measure_id=1,
    label='label3',
    coord=(float(52.2153), float(0.1318)),
    typical_range=(1,2),
    river='river',
    town='town')

    stations.append(s1)
    stations.append(s2)
    stations.append(s3)

    list_test_1F = inconsistent_typical_range_stations(stations)

    assert len(list_test_1F) == 2   # only two inconsistent
    assert list_test_1F[0] == s1.name
    assert list_test_1F[1] == s2.name

