from collections import deque
'''
You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis
that occurs after the former.
There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
Input:
{[()]}
{[(])}
{{[[(())]]}}
'''
stack = []
pattern = input()
balanced = True
for item in pattern:
    if item in "([{":
        stack.append(item)
    else:
        if stack:
            top_element = stack.pop()
            if f"{top_element}{item}" in "()[]{}":
                continue
            else:
                balanced = False

if len(stack) == 0 and balanced:
    print("YES")
else:
    print("NO")
