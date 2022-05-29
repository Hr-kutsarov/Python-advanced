from collections import deque
'''
Write a program which reads from the console a string with N integers, separated by a single space, and reverses them
using a stack. Print the reversed integers on one line, separated by a single space.
Input:
1 2 3 4 5
'''
stack = []
data = input().split()
for item in data:
    stack.append(item)

while stack:
    print(*stack.pop(), end=" ")
