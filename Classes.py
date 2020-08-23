class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name + self.age)


#p1 = Person("Zach", 23)

#print(p1.name)
#print(p1.age)
p1 = Person("Zach",str(23)) #An object 
#p1.myFunc() #Calls function with p1 parameters
p1.age = 25
print(p1.age)
