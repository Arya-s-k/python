cost_price= float(input("enter cost price : "))
selling_price= float(input("enter selling price : "))
if cost_price< selling_price:
    print(f"the profit is {selling_price - cost_price}")
else:
    print(f"the loss is {cost_price- selling_price}")