from collections import deque


def print_solution(queue):
    if len(queue) == 0:
        print("Orders complete")
    else:
        print("Orders left:", end=" ")
        print(*queue, sep=" ")
    return


total_food = int(input())
que = deque([int(x) for x in input().split()])
largest_order = max(que)
while que:

    current_order = que[0]

    if current_order > total_food:
        break

    total_food -= current_order
    que.popleft()

print(largest_order)
print_solution(que)