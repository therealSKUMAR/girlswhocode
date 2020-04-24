#this is my guess a number program

import random
limit = 100

number = random.randint(1,limit)
guess = int(input("guess an number between 1 and " +str(limit)+ ": "))
count = 1

while guess != number:
    count = count + 1
    if guess < number:
        guess = int(input("too low! guess again: "))

    if guess > number:
        guess = int(input("too high! guess again: "))

    if guess == number:
        print("you're right! the number was " + str(number))
        if count == 1:
            print("it only took you 1 try")
        else:
            print("it only took you " + str(count) + " tries")
        break
