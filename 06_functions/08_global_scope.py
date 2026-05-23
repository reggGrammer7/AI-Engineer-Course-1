chai_type = "plain chai"  
def front_desk():
    print("At front desk:", chai_type)  # Accessing global variable
    def kitchen():
        global chai_type  # Referring to the global variable
        chai_type = "Masala Chai"  # Modifying the global variable
    kitchen()
    print("At front desk after kitchen update:", chai_type)  # Accessing the modified global variable



front_desk()
# Global is designed in such a way that 
# it is only accesses variables outside 
# function

# Nonlocal is to look just above that current 
# function and access the variable which is there.
# thus nonlocal should be used when we have 
# nested functions and we want to access the variable
# which is in the enclosing function.

# Enclosing variable is the variable 
# which is in the outer function

# Be very careful while using global variables 
# as they can lead to bugs and make code harder to understand.
#  Always try to limit the use of global variables and prefer
#  passing parameters to functions instead.