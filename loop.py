
def function():
    i = 1
    while i < 20:
        print(i)
        if (i == 20):
            break
        i += 2
def for_loop():
    fruits = ["Orange", "Banana", "Cherry"]
    for x in fruits:
        print(x)
        if x == "Banana":
            continue
def nameFunction(name):
    print(name + " Lastname")

def returnFunction(x):
    print("The value of x is before: " + str(x))
    return (5 * x)


function()
for_loop()
nameFunction("Zachary")
nameFunction("Jim")
num = int(2)
print(returnFunction(num))
