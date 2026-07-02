#find the sum of the digits in a given number
num=int(input("enter a number"))
sum=0
while num>0:
    sum=num%10+sum
    print(sum)
    num=num//10