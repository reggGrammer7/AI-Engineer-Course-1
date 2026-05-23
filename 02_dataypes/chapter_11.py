# Dictionaries
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.
chai_order = dict(type="Masala Chai",size ="Large",sugar_level = "Medium"  )
print(f"Chai order: {chai_order}")  
# Accessing values using keys
print(f"Chai type: {chai_order['type']}")

chai_recipe = {
    "water": "2 cups",
    "tea leaves": "1 tsp",
    "milk": "1 cup"
}
print(f"Chai recipe: {chai_recipe}")

# Removing a key-value pair
del chai_recipe["tea leaves"]
# Adding a new key-value pair
chai_recipe["sugar"] = "1 tsp"
print(f"Updated chai recipe: {chai_recipe}")


## Membership testing
print(f"Is 'milk' an ingredient in the chai recipe? {'milk' in chai_recipe}")

print(f"All keys in the recipe :{chai_recipe.keys()}")

# All items 
print(f"All items in the recipe :{chai_recipe.items()}")

# Using the get method to access values 
print(f"Amount of water needed: {chai_recipe.get('water',"No water specified")}")







