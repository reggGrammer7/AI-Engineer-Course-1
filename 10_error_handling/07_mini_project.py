class InvaidInputError(Exception):
    """Custom exception for invalid input."""
    pass

# def bill(flavor, quantity):
#     menu = {"masala": 20, "ginger": 15}
#     try:
#         if flavor not in menu:
#             raise InvaidInputError("Sorry, we don't have that flavor.")
#         if not isinstance(quantity, int) or quantity <= 0:
#             raise InvaidInputError("Quantity must be a positive integer.")
#         price = menu[flavor]
#         total_cost = price * quantity
#         print(f"The total cost for {quantity} {flavor} chai is: {total_cost}")
#     except InvaidInputError as e:
#         print(f"Error: {e}")
#     finally:       
#         print("Thank you for visiting our chai shop!")

# bill("masala", 3)  # Valid case
# bill("unknown", 2)  # Invalid flavor


# How will the code look if we had the menu 
# outside the function and we want to use it 
# in multiple functions?
menu = {"masala": 20, "ginger": 15}

def bill(flavor, quantity):
    try:
        if flavor not in menu:
            raise InvaidInputError("Sorry, we don't have that flavor.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise InvaidInputError("Quantity must be a positive integer.")
        price = menu[flavor]
        total_cost = price * quantity
        print(f"The total cost for {quantity} {flavor} chai is: {total_cost}")
    except InvaidInputError as e:
        print(f"Error: {e}")
    finally:       
        print("Thank you for visiting our chai shop!")

bill("masala", 3)  # Valid case
bill("unknown", 2)  # Invalid flavor
