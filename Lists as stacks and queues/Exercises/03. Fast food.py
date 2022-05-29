from collections import deque
'''
Write a program which checks if you have enough food to serve lunch to all your customers. You also want to know who the
client with the biggest order for that day is. 
First, you will be given the quantity of the food that you have for the day (an integer number). Next, you will be given
a sequence of integers (separated by a single space), each representing the quantity of an order. Keep the orders
in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. 
Before each order, check if you have enough food left to complete it. If you have, remove the order from the queue and 
reduce the amount of food you have. Otherwise, stop serving.
Input
•	On the first line you will be given the quantity of your food - an integer in the range [0, 1000]
•	On the second line you will receive a sequence of integers, representing each order, separated by a single space
Output
•	On the first line, print the quantity of biggest order
•	On the second line:
o	If you succeeded in servicing all your clients, print: "Orders complete".  
o	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
Input:
348
20 54 30 16 7 9

'''

quantity = int(input())
sequence = deque([int(x) for x in input().split()])
# [20, 54, 30, 16, 7, 9] in deque
insufficient = []
largest_order = 0
sufficient = True
while sequence:
    next_order = sequence.popleft()
    if next_order > largest_order:
        largest_order = next_order
    if quantity > next_order and sufficient:
        quantity -= next_order
    else:
        sufficient = False
        insufficient.append(next_order)

print(largest_order)
if not sufficient:
    print(f"Orders left: {' '.join([str(x) for x in insufficient])}")
else:
    print(f"Orders complete")



