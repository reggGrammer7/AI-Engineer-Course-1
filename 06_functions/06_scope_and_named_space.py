# Defining global variable, local variable and enclosiing variable  

def outer_function():
    x = "enclosing variable"
    
    def inner_function():
        y = "local variable"
        print("Inside inner function:", x)  # Accessing enclosing variable
        print("Inside inner function:", y)  # Accessing local variable
    
    inner_function()
    print("Inside outer function:", x)  # Accessing global variable

outer_function()












