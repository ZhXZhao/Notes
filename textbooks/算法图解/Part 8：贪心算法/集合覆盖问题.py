'''
Author: ZhXZhao
Date: 2020-12-02 17:12:46
LastEditors: ZhXZhao
LastEditTime: 2020-12-02 17:20:56
Description: file content
'''

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, state_for_stations in stations.items():
        covered = state_for_stations & states_needed
        if(len(covered) > len(states_covered)):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
