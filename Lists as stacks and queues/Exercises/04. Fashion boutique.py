stack_clothes = [int(x) for x in input().split()]
capacity = int(input())
rack_counter = 1    # coat hangers
current_rack = capacity
while stack_clothes:    # if the stack has items in it
    top_item = stack_clothes[-1]    # this is the item on top of the stack
    if top_item <= current_rack:    # if this statement fits the fits the argument
        stack_clothes.pop()     # pick up the item from the stack
        current_rack -= top_item    # complete the argument
    else:
        rack_counter += 1   # if the argument is false, create new argument
        current_rack = capacity     # reset the argument

print(rack_counter)