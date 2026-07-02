#: Find the number of digits in a given number

number = int(input("Enter any number: "))
no_of_digits=0
while number>0:
    number=number//10
    no_of_digits=no_of_digits+1
print("number of digits=",no_of_digits)



string=input("enter any thing-")
print(len(string))