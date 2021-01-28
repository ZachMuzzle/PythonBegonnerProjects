test = 2

def add():
    global test
    test = test + 2
    print("inside function:", test)

add()
print("in main:", test)