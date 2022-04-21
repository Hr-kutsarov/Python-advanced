from collections import deque
number_of_stations = int(input())
stations = deque()

for _ in range(number_of_stations):
    stations_data = [int(x) for x in input().split()]       # split the data and convert into integers
    stations.append(stations_data)      # add the data to the deque

for attempt in range(number_of_stations):       # perform a check on every item in the queue
    tank = 0
    failed = False

    for fuel, distance in stations:     # unpack variables
        tank += fuel

        if distance > tank:
            failed = True
            break

    if failed:
        stations.append(stations.popleft())     # take the first item and add it to the back of the queue
    else:
        print(attempt)
        break

