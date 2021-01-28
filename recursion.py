def recur_factiorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factiorial(n-1)

num = 7

#check if number is negative
if num < 0:
    print("sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("factorial of", num, "is", recur_factiorial(num))