# A function to that adds a value of 10% for every order and returns final price 

def add_vat(price, vat_rate):
	bill = price*(1+ vat_rate)
	return bill

Garry = add_vat(10,0.2)
Sally = add_vat(20,0.2)
print("Garry's total bill is", Garry)   
print("Sally's total bill is", Sally)


orders = [10, 20, 30, 40]
for price in orders:
	final_price = add_vat(price, 0.2)
	print("The final price is", final_price)

