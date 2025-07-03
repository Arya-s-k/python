def due_amt(amount_paid, cost_price):
    rmt = amount_paid - cost_price
    return rmt


amount_paid = float(input("enter the amount paid to the shopkeeper :"))
cost_price = float(input("enter the costprice :"))
res = due_amt(amount_paid, cost_price)
print(f"the due amount from the shopkeeper is {res}, if the amt paid is {amount_paid} and the cost price is {cost_price}")