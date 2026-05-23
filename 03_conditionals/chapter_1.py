# Condtionals
kettle_boiled = True
if kettle_boiled:
    print("Kettle done! Time to make chai.")
else:
    print("Go ahead and boil the kettle.")

# Build a snack recommendation system
user = input("What snack do you want?").lower()
if user == "cookies" or user == "samosa":
    print("Order confirmed!")
else:
    print("Sorry, not available.")

# Build a Chai price calculator 
cup = input("What cup size of chai do you want(small/medium/large)").lower()
if cup == "small":
    print("Small cup price is 10")
elif cup == "medium":
    print("Medium cup price is 15")
elif cup == "large":
    print("Large cup price is 20.")
else :    print("Unknown cup size")




