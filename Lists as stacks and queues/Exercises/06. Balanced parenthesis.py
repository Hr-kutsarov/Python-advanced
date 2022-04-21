# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former.
# There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].

sequence = input()      # {{{((([])))}}}
stack = []
condition = True
for s in sequence:
    if s in "({[":
        stack.append(s)
    elif not stack:
        condition = False
    elif s in ")]}":
        opening_bracket = stack.pop()
        if f"{opening_bracket}{s}" not in "{}[]()":
            condition = False
            break

if condition and not stack:
    print(f"YES")
else:
    print(f"NO")
