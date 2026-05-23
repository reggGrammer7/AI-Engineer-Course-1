# Advanced data types in python
# Comes mostly when you are working with someone's 

# datetime
from datetime import datetime
current_time = datetime.now()
print(f"Current date and time: {current_time}")

# calenda 
import calendar
year = 2024
month = 6
print(f"Calendar for {month}/{year}:\n{calendar.month(year, month)}")




print(calendar.month(year,month))

## Arrow
# import arrow
# current_time_arrow = arrow.now()
# print(f"Current date and time using Arrow: {current_time_arrow}")


# Collections
from collections import Counter
data = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
counter = Counter(data)
print(f"Count of each fruit: {counter}")













