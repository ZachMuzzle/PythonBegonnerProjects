import random
from pip._vendor.distlib.compat import raw_input

n = random.randint(1,99)
print(n)
guess = int(raw_input("Enter a number from 1 to 99: "))
while n != "guess": # keep looping until == n
    print
    if guess < n:
        print("guess is low")
        guess = int(raw_input("Enter a number from 1 to 99: "))
    elif guess > n:
        print("Guess is high")
        guess = int(raw_input("Enter a number from 1 to 99: "))
    else:
        print("You guessed it! ")
        break
        print