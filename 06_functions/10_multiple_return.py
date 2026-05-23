# Handling multiple return valies from a fucntion

def calculate_bill(price, tax_rate):
    tax_amount = price * tax_rate
    total_bill = price + tax_amount
    return total_bill, tax_amount

total, tax = calculate_bill(100, 0.1)
print(f"Total bill: {total}, Tax amount: {tax}")


# Using a dictionary to return multiple values
def chai_report():
    report = {
        "total_sales": 1500,
        "total_customers": 100,
        "average_sale": 15
    }
    return report

report = chai_report()
print(f"Total Sales: {report['total_sales']}, Total Customers: {report['total_customers']}, Average Sale: {report['average_sale']}")

def chai_rep():
    return 100, 20, 30
sold, remaining, _ = chai_rep() # Using underscore to ignore the third value
print(f"Sold: {sold}, Remaining: {remaining}")













