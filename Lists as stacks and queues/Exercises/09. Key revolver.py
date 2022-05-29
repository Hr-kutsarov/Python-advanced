from collections import deque
'''
Our favorite super-spy action hero Sam is back from his vacation and it is time to go on a mission.
 He needs to unlock a safe locked by several locks in a row, which all have varying sizes.
The hero possesses a special weapon though, called the Key Revolver, with special bullets. 
Each bullet can unlock a lock with a size equal to or larger than the size of the bullet. 
The bullet goes into the keyhole, then explodes, completely destroying it. 
Sam doesn't know the size of the locks, so he needs to just shoot at all of them, until the safe runs out of locks.
What's behind the safe, you ask? Well, intelligence! It is told that Sam's sworn enemy – Nikoladze, 
keeps his top secret Georgian Chacha Brandy recipe inside. It's valued differently across different times of the year, 
so Sam's boss will tell him what it's worth over the radio. One last thing, 
every bullet Sam fires will also cost him money, which will be deducted from his pay from the price of the intelligence. 
Good luck, operative.
Input
•	On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
•	On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
•	On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
•	On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
•	On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
After Sam receives all of his information and gear (input), he starts to shoot the locks front-to-back, 
while going through the bullets back-to-front.
If he successfully destroyed a lock, print "Bang!", then remove the lock. If not, print "Ping!", 
leaving the lock intact. The bullet is removed in both cases.
If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. 
If there aren't any bullets left, don't print it.
The program ends when Sam either runs out of bullets, or the safe runs out of locks.

Input:
50
2
11 10 5 11 10 20
15 13 16
1500
'''


def print_solution(bullets, locks, profits):
    profits = profits
    if bullets == 0 and locks == 0:
        print(f"0 bullets left. Earned ${profits}")
    elif bullets == 0:
        print(f"Couldn't get through. Locks left: {locks}")
    elif locks == 0:
        print(f"{bullets} bullets left. Earned ${profits}")


bullet_price, gun_barrel_size = int(input()), int(input())
bullets_sequence = [int(x) for x in input().split()] # stack
locks_sequence = deque([int(x) for x in input().split()]) # queue
intelligence_value = int(input())
expenses = 0
shots_fired = 0
while bullets_sequence and locks_sequence:
    bullet = bullets_sequence.pop()
    lock = locks_sequence[0]
    expenses += bullet_price
    shots_fired += 1

    if bullet > lock:
        print("Ping!")
    else:
        destroyed_lock = locks_sequence.popleft()
        print("Bang!")

    if shots_fired == gun_barrel_size:
        print("Reloading!")
        shots_fired = 0

profit = intelligence_value - expenses
print_solution(len(bullets_sequence), len(locks_sequence), profit)









