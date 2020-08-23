fruits = ["Apple", "Orange", "Grape"];
input = int(input("Enter a number: "))
for x in fruits:
    print(x)
    if x == "Orange":
        ##print(x)
        print("Hit Orange in loop")
        break

for x in range(input,10):
    print(x)
    if x == 5:
        break;