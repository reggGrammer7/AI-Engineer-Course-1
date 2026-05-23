# Generators ( uses the same syntax as lists, dict and sets but only uses parenthes)
# This concept saves memory usage as it does
# not run everything and save it in the memory
# rather it only shows you what it has at each stage 
# Its like a stream


# Getting sales greater than 5
daily_sales = [5,10,12,7,3,8,9,15]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)