'''
You have an empty stack. You will receive an integer – N. On the next N lines you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from the top to the bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
Input:
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

'''
stack = []
n = int(input())
for i in range(n):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        push_element = command[1]
        stack.append(push_element)
    elif command[0] == 2 and stack:
        stack.pop()
    elif command[0] == 3:
        print(max(stack))
    elif command[0] == 4:
        print(min(stack))
reverse = reversed(stack)
print(*reverse, sep=", ")
