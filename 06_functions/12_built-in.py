# Using inbuilt functions in Python
def chai_flavor(flavor="Masala Chai"):
    """"Returns the flavor of chai"""
    chai = "ginger"
    return flavor
print(chai_flavor())

print(chai_flavor.__doc__) # Accessing the docstring of the function    
print(chai_flavor.__name__) # Accessing the name of the function    

# The tripple quote should always be the first line of the code 
def generate_bill(chai=0, samosa =0):
    """Generates the bill for 
    the given quantity of chai 
    and samosa. 
    param chai: number of cups of chai
    param samosa: number of samosas
    return: total bill amount
    """
    total = (chai * 10) + (samosa * 5)
    return total
    

 
 
 
print(generate_bill(2, 3))





