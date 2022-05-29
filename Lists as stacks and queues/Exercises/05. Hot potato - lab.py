from collections import deque

deq = deque()
'''
Hot Potato is a game in which children form a circle and start tossing a hot potato. The counting starts with the 
first kid. 
Every nth toss the child who is holding the potato leaves the game. When a kid leaves the game, it passes the potato to 
the next kid. This continues until there is only one kid left.
Create a program that simulates the game of Hot Potato. On the first line you will receive names of kids, separated by 
a single space. On the second line you will receive the nth toss (integer) in which a child leaves the game.
Print every kid which is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in
the format "Last is {kid}".

George Peter Michael William Thomas
10

'''
kids = input().split()
# kids = "Tracy Emily Daniel".split()

iterations = int(input())
# iterations = 2
for el in kids:
    deq.append(el)

counter = 0
while len(deq) > 1:
    counter += 1
    if counter != iterations:
        deq.append(deq.popleft())
    else:
        kid = deq.popleft()
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {''.join(deq)}")
