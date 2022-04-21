def print_stack(stack):
    while stack:
        element = stack.pop()
        if stack:
            print(element, end=", ")
        else:
            print(element)


rotations = int(input())
stack = []
for _ in range(rotations):
    input_data = input().split()
    num = int(input_data[0])
    if num == 1:
        value = int(input_data[1])
        stack.append(value)
    elif num == 2 and stack:
        stack.pop()
    elif num == 3 and stack:
        print(max(stack))
    elif num == 4 and stack:
        print(min(stack))

print_stack(stack)
