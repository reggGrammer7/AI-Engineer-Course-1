# We pass parameters to functions when defining them,
# and we provide arguments when calling the function.
# Parameters are the variables that are defined in the function definition,



def make_chai(tea, milk, sugar):
    print(f"Making {tea} with {milk} and {sugar} sugar.")

make_chai("Green Tea", "Almond Milk", "Honey") # positional arguments(you already know the order 
# of the parameters and you are passing the arguments in that order
make_chai(milk="Oat Milk", tea="Black Tea", sugar="Brown Sugar") # keyword arguments (you are explicitly mentioning the parameter names while passing the arguments, so the order does not matter)



# *args and **kwargs are used to handle variable number of arguments in a function.
# *args allows you to ass a variable number of positional arguments to a function,
#  and it
# collects them into a tuple. **kwargs allows you to pass a variable number of keyword arguments to a function, and it collects them into a dictionary.
def special_chai(*ingredients, **extras): #def special_chai(*args, **kwargs):
    print("Ingredients:", ingredients)  # This will be a tuple of all positional arguments
    print("Extras:", extras)  # This will be a dictionary of all keyword arguments

special_chai("Green Tea", "Almond Milk", "Honey", flavor="Mint", size="Large")

# Default traps 
def chai_order(order=[]):
    order.append("Chai")
    print("Current order:", order)
chai_order()  # Output: Current order: ['Chai']
chai_order()  # Output: Current order: ['Chai', 'Chai']




def chai_order(order= None):
    if order is None:
        order = []
    print("Current order:", order)

chai_order()

