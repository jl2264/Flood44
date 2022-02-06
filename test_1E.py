
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

def test_rivers_by_station_number():
    
    stations = []

    s1 = MonitoringStation(river='river1', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s2 = MonitoringStation(river='river1', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s3 = MonitoringStation(river='river1', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s4 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s5 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s6 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s7 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s8 = MonitoringStation(river='river3', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s9 = MonitoringStation(river='river3', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s10 = MonitoringStation(river='river4', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    
    stations.append(s1)
    stations.append(s2)
    stations.append(s3)
    stations.append(s4)
    stations.append(s5)
    stations.append(s6)
    stations.append(s7)
    stations.append(s8)
    stations.append(s9)
    stations.append(s10)

    list_test_1E = rivers_by_station_number(stations, 3)

    assert len(list_test_1E) == 3   # only three rivers should be returned
    assert list_test_1E[0] == ('river2', 4)
    assert list_test_1E[1] == ('river1', 3)   
    assert list_test_1E[2] == ('river3', 2)   

def test_rivers_by_station_number_large_N():
    
    stations = []

    s1 = MonitoringStation(river='river1', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s2 = MonitoringStation(river='river1', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s3 = MonitoringStation(river='river1', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s4 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s5 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s6 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s7 = MonitoringStation(river='river2', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s8 = MonitoringStation(river='river3', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s9 = MonitoringStation(river='river3', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    s10 = MonitoringStation(river='river4', station_id=1, measure_id=1, label='label1', coord=(float(52.2053), float(0.1218)), typical_range='typical_range', town='town')
    
    stations.append(s1)
    stations.append(s2)
    stations.append(s3)
    stations.append(s4)
    stations.append(s5)
    stations.append(s6)
    stations.append(s7)
    stations.append(s8)
    stations.append(s9)
    stations.append(s10)

    list_test_1E = rivers_by_station_number(stations, 10)

    assert len(list_test_1E) == 4   # all four rivers should be returned
    assert list_test_1E[0] == ('river2', 4)
    assert list_test_1E[1] == ('river1', 3)   
    assert list_test_1E[2] == ('river3', 2)   
    assert list_test_1E[3] == ('river4', 1)   

