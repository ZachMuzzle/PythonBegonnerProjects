max = int(input(" Enter a max number: "))
even_total = 0
odd_total = 0

for number in range(1, max + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
print("The sum of even numbers from 1 to " + str(number) + " = " + str(even_total))
print("The sum of odd numbers from 1 to " + str(number) + " = " + str(odd_total))