# M2 L1 A1 : Exam Eligibility Check

# ACTIVITY 1: STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS:

# Take the required input for attendance
atttendence=float(input("ENTER YOU ATTENDECE PERCENTAGE"))
# - Student should have attendance >= 75%
if atttendence>=75:
    print("allowed to take exam")
else:
    med=input("enter you medical certificate yes or no-")
    if med=="yes":
        print("you are allowed to takee the exam")
    else:
        print("you are not allowed")
# - Check if attendance matches above criteria

# - Then Print "Allowed"

# - If attendance is low, Student should have a medical certificate

# - Take input for medical certificate

# - Check if student replied Yes or No

# - If Yes, Print "Allowed"

# - Else No, Print "Not Allowed"