homework = int(input("Enter in your homework grade: "))
examNum = int(input("Enter in the number of exams: "))
examTotal = 0
exams = 0
def myFunction(average):
    if (average <= 100 and average >= 0):
        print("Correct average!")
    elif(average > 100 or average < 0):
        print("Wrong average!")

for x in range(examNum):
    exam = int(input("Enter exam grade: "))
    #print(exam)
    examTotal += exam # = examtotal + exam
exams = examTotal/examNum
lab = int(input("Enter in your lab grade: "))
part = int(input("Enter in your part grade: "))

homework = homework*.20
exams = exams*.50
lab = lab*.20
part = part*.10

average = homework+exams+lab+part
myFunction(average)
print("Your average grade was: " + str(average))
#myFunction(average)
#print(exams)

