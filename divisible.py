number = int(input("Enter a integer: "))
while number > 0:
    print
    if((number % 5 == 0) and (number % 11 == 0)):
        print("Given number: " + str(number) + " is divisible by 5 and 11.")
        number = int(input("Enter a integer: "))

    else:
        print("The number given: " + str(number) + " is not divisible by 5 and 11.")
        number = int(input("Enter a integer: "))
