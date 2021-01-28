class test:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def introDuc(self):
        print("Hello my name is: " + self.name + " and I weigh " + self.weight)

def returnNum(x):
    print("Value passed: " + str(x))
    x = x + 10
    return x

class complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

person1 = test("Ralph", str(205)) #object made

person1.introDuc() #object called then function


value = returnNum(20)

print("Value returned is now: " + str(value))

num1 = complex(3, 5)
num1.attr2 = 20
num1.get_data()

num2 = complex(5)
num2.attr = 10 #create another attribute

print(num2.real, num2.imag, num2.attr)
print(num1.attr2)