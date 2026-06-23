#find if seller made profit or loss
actual_cost = float(input(" Please Enter the Actual Product Price: "))

sale_amount = float(input(" Please Enter the Sales Amount: "))
if sale_amount>actual_cost:
    print("seller made a profit")
    print( sale_amount-actual_cost)
else:
    print("seller is in a loss")
