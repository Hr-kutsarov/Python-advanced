from collections import deque

'''
George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End
'''

d = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(d)} people remaining.")
        break
    elif command == "Paid":
        while d:
            print(d.popleft())
    else:
        d.append(command)
















