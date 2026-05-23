class chai:
    temperature = "hot"
    strength = "strong"

cutting = chai()
print(cutting.temperature)

cutting.temperature = "mild"

print(f"After changing, {cutting.temperature}")
print(f"Direct look into the class, {chai.temperature}")

del cutting.temperature 
print(cutting.temperature)

# if there is a fallback or if a variable you 
# you want to delete already exist in the class
# then even when you delete an inject one it will 
# fallback to the previous one in the class but 
# if it does not then it will give back an error 

cutting.cup = "small" # not in the class only been injected
print("Value before deleting an injected propery",cutting.cup)
del cutting.cup
print("Value after deleting an injected propery", cutting.cup)















