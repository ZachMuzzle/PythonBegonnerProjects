import random
from pip._vendor.distlib.compat import raw_input
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))
randomNum2 = random.randint(1,100)

reRandom = int(input("How many times do you want to randomize the random number?:"))

for x in range(reRandom):
    randomNum = random.randint(1,100)
    print(randomNum)
    if(number1 < randomNum):
        print("Number1 is less than the random number")
    if(number2 < randomNum):
        print("Number2 is less than the random number")
    if(number1 > randomNum):
        print("Number1 is greater than the random number")
    if(number2 > randomNum):
        print("Number2 is greater than the random number")

while number1 != randomNum2:
    if(number1 < randomNum2):
        print("Number is less then the random number")
        number1 = int(input("Enter a number:"))
    elif(number1 > randomNum2):
        print("Number is greater than random number")
        number1 = int(input("Enter a number:"))
    else:
        print("You guessed it! ")
        break
        print
