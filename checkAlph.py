ch = input("Enter a character: ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z' )):
    print("The letter you entered: " + ch + " is within the alphabet")
else:
    print("The letter you entered: " + ch + " is  not in the alphabet")