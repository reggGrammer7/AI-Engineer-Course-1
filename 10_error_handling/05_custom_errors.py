# Raise your own exceptions in Python by defining custom exception classes.
#  This allows you to create more specific error messages and handle errors in a way that is relevant to your application's logic.

# Custom exception class
class InvalidOrderError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        raise InvalidOrderError("Sorry that chai is not on menu")
    except TypeError:
        raise InvalidOrderError("Quantity must be a number")
    
# Another example of custom exception for handling insufficient stock
class InsufficientStockError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)    

def check_stock(item, quantity):
    stock = {"masala": 10}
    try:
        if item not in stock:
            raise InvalidOrderError("Sorry that chai is not on menu")
        elif quantity > stock[item]:
            raise InsufficientStockError("Sorry, we don't have enough stock for that order")
        else:
            print(f"Order for {quantity} {item} chai is accepted.")
    except InvalidOrderError as e:
        print("Invalid Order Error: ", e.message)
    except InsufficientStockError as e:
        print("Insufficient Stock Error: ", e.message)







