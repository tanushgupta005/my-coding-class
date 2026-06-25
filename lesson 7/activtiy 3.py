marks1=int(input("enter you marks of maths="))
marks2=int(input("enter you marks of science="))
marks3=int(input("enter you marks of english="))
ave=(marks1+marks2+marks3)//3
if ave in range(90,101):
    print("A+")
elif ave in range(80,90):
    print("A")
elif ave in range(70,80):
    print("B+")
elif ave in range(60,70):
    print("B+")
elif ave in range(50,60):
    print("B")
elif ave in range(0,50):
    print("F")