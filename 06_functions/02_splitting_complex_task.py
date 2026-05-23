# Creating a monthly report for a cafe
# that will call three other functions to be executed
from calendar import month


def fetch_sales(month, year):
	print("I fetch the sales data")
def filter_valid_orders(month, year):
	print("I only fetch valid orders")
def summarize_data(month, year):
	print("I will give you a summary of your data")

def generate_report(month,year):
    fetch_sales(month, year)
    filter_valid_orders(month, year)
    summarize_data(month, year)
    print("Here is your final report for this month")
	



generate_report("June", 2024)