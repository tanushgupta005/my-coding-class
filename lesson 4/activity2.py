#1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount=int(input("enter the amount"))
 # 2) Find how many 100-rupee notes are needed:

# Divide `Amount` by 100 (floor division) and store it in `note_1`.
note100=amount//100
#print(amount,type(amount))
#print(amount+5)
# 3) Find the remaining amount after taking out 100-rupee notes:
amount=amount%100
# Use the remainder of `Amount` after dividing by 100.

# 4) From the remaining amount, find how many 50-rupee notes are needed:
note50=amount//50
# Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:
amount=amount%50
# Use the remainder after dividing by 50.

# 6) From the remaining amount, find how many 10-rupee notes are needed:
note10=amount//10
# Divide the remainder by 10 (whole number division) and store it in `note_3`.

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print("100 rs nots =",note100)
print("50 rs notes=",note50)
print("10 rs notes =",note10)