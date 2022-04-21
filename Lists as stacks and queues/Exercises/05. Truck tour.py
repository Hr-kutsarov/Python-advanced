from collections import deque
number_of_stations = int(input())
stations = deque()

for _ in range(number_of_stations):
    stations_data = [int(x) for x in input().split()]   # 1 5 10 3 3 4
    stations.append(stations_data)

for attempt in range(number_of_stations):
    tank = 0
    failed = False

    for fuel, distance in stations:
        tank += fuel

        if distance > tank:
            failed = True
            break

    if failed:
        stations.append(stations.popleft())
    else:
        print(attempt)
        break

