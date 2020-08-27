from callMe import callFunction
number = int(input("Enter a number:"))
callFunction(number)
print("Going to while loop now")
while(number < 0 or number > 10):
   callFunction(number)
   #if(number > 0 and number < 10):
   # print("Ending program loop now...")
       #break
print("program ending.")