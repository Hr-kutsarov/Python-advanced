expression = input()
'''
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
'''
stack = []
for index in range(len(expression)):
    char = expression[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        start_index = stack.pop()
        end_index = index
        print(expression[start_index:end_index+1])