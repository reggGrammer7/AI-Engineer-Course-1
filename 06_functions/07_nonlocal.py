# Using local and global variables
def update_order():
    chai_type = "Masala Chai"  # Local variable
    def kitchen():
        nonlocal chai_type  # Referring to the enclosing variable
        chai_type = "Ginger Chai"  # Modifying the enclosing variable
    kitchen()
    print("Inside kitchen:", chai_type)  # Accessing the modified variable


update_order()