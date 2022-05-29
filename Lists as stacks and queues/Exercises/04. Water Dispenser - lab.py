from collections import deque

'''
2
Peter
Amy
Start
2
refill 1
1
End

'''
people_in_line = deque()
starting_quantity = int(input())
current_quantity = starting_quantity
while True:
    person_in_line = input()
    if person_in_line == "Start":
        break
    else:
        people_in_line.append(person_in_line)

while people_in_line:
    going_for_water = people_in_line[0]
    command = input().split()
    if command[0] == "End":
        break
    if command[0] == "refill":
        current_quantity += int(command[1])
    else:
        quantity_needed = int(command[0])
        if quantity_needed <= current_quantity:
            people_in_line.popleft()
            current_quantity -= quantity_needed
            print(f"{going_for_water} got water")
        else:
            people_in_line.popleft()
            print(f"{going_for_water} must wait")

print(f"{current_quantity} liters left")
