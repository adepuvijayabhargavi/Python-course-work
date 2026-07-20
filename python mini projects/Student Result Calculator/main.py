name = input("Enter student's name: ")
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))

total = sub1 + sub2 + sub3
average = total/3
percentage = (total / 300) + 100

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")

if percentage >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")