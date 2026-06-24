#calcuate the grade of a student based on the given marks
a=int(input('ENTER YOUR MARKS'))
if a==100:
    print("A+")
elif a>90:
    print("A")
elif a>80:
    print("B+")
elif a>70:
    print("B")
elif a>60:
    print("C+")
elif a>50:
    print("C")
elif a>40:
    print("D")
#elif a>0:
else:
    print("F")
    