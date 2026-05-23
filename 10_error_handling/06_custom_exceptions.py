# Custom exception class
class InvalidOrderError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Another example of custom exception for handling insufficient stock
class InsufficientStockError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class OutofIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk ==0 or sugar == 0:
        raise OutofIngredientsError("Sorry, we are out of ingredients to make chai")
    print("Chai is ready....")

make_chai(0, 1)

# Custom exceptions crash the program gracefully with a clear error message,
#  and they can be caught and handled just like built-in exceptions. 
# This allows you to create more specific error handling logic that is 
# tailored to your application's needs.