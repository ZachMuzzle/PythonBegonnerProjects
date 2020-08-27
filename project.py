
from callLoop import function
number = int(input("Enter a number: "))

#for x in range(number):
    #print("hello")

if (number <= 100 and number >= 0):
    print("Your number is " + str(number))
    function(number,20)

for x in range(number):
    if number > 0 :
        print("Greater than zero!")