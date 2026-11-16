name = input("Enter Student Name: ")
n = int(input("Enter Number of Subjects: "))
total = 0
for i in range(1,n+1):
    mark = float(input("Enter Subject Mark{i}: "))
    total += mark
percentage = total / n

if percentage >= 90:
    grade = "A+"
    performance = "Oustanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "Needs Improvement"

print("Student name:",name)
print("Total marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)
print("Performance:",performance)