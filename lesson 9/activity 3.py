# M2 L1 A3 - CUSTOMIZE YOUR FOOD DELIVERY ORDER

# 1) Display a menu asking the user to select a food category:
print("what do you want to order")
print("1.biryani")
print("2.pizza")

# - 1 for Biryani

# - 2 for Pizza

# 2) Take the user’s input and store it in `choice`.

choice1=int(input("ENTER 1 OR 2_"))
#if choice1 in range(3,9999999999999999999999999999999999999):
   # print("you have entered a wrong number")
if choice1==1:
    print("do you want veg or non veg biryani")
    choice2=int(input("press 1 for veg and 2 for non veg"))
    if choice2==1:
        print ("thanks for ordaring veg biryani")
    else:
        print("thanks for ordaring non veg biryani")
elif choice1==2:
    print("which pizza do you want veg or non veg pizza")
    print("type 1 for veg and 2 for non veg")
    choice3=int(input("enter your choice"))
    if choice3==1:
        print("thanks for ordaring veg pizze")
    else:
        print("thanks for ordaring non veg pizza")
else:
    print("you have entered the wrong choice")   
# 3) If `choice` is 1 (Biryani):

# a) Show Biryani options (Veg / Chicken)

# b) Take the user’s input for Biryani type and store it in `choice2`

# c) If `choice2` is 1, print "Your order is on the way: Veg Biryani"

# Else, print "Your order is on the way: Chicken Biryani"

# 4) Else if `choice` is 2 (Pizza):

# a) Show pizza options (Paneer / Chicken)

# b) Take the user’s input for pizza type and store it in `choice3`

# c) If `choice3` is 1, print "Your order is on the way: Paneer Pizza"

# Else, print "Your order is on the way: Chicken Pizza"

# 5) Else (if `choice` is not 1 or 2):

# Print "Wrong choice!"