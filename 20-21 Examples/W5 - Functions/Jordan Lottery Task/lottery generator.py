import random
from random import randint

def lottery(numbers):
    count = 0
    ticket = randint(1,20) , randint(1,20) , randint(1,20) , randint(1,20), randint(1,20), randint(1,20)
    while ticket != numbers:
        count += 1
        ticket = randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)
        print("Ticket # {} : {}".format(count,ticket))
    return count

tries = lottery([15, 20, 10, 5, 2, 4])

print("It took {} tries to get the winning lottery numbers".format(lottery))