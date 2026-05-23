# Create a function that returns the total bill for different orders

def calculate_bill(cups, price_per_cup):
	total_bill = cups * price_per_cup
	return total_bill

john = calculate_bill(6,1.50)
mark = calculate_bill(29,1.50)
print("John's total bill is", john)
print("Mark's total bill is", mark)