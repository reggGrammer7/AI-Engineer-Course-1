# This is used to transform the input of a
# a function. 
# It takes a function as a parameter
# 
from functools import wraps # preserves the meta data
def my_decorator(func):
    @wraps(func) # the function name gets changed without this
    # when the decorator is been used or wrapped around it 
    # without this line
    def wrapper():
        print("Before function runs")
        func() # execute your function here 
        print("After function runs")
    return wrapper    

@my_decorator
def greet():
    print("Hello from decorators class on chai code")

greet()
print(greet.__name__)