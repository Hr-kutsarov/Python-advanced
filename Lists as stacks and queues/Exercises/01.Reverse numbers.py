# Write a program which reads from the console a string with N integers, separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

input_data = input().split()   # 1 2 3 4 5
stack = []
for i in input_data:
    stack.append(i)
while stack:
    top = stack.pop()
    if stack:
        print(top, end=", ")
    else:
        print(top)
