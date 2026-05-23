# Sets
essential_ingredients = {"flour", "eggs", "milk"}
optional_ingredients = {"sugar", "vanilla", "milk"}
# Using the union operator to combine two sets
all_ingredients = essential_ingredients | optional_ingredients
print(f"All ingredients: {all_ingredients}")

# Finding the common ingredients
common_ingredients = essential_ingredients & optional_ingredients
print(f"Common ingredients: {common_ingredients}")

# Only essential ingredients
only_essential = essential_ingredients - optional_ingredients
print(f"Only essential ingredients: {only_essential}")

# Membership testing
print(f"Is 'sugar' an essential ingredient? {'sugar' in essential_ingredients}")


####    Frozen Sets
# Frozen sets are immutable sets
frozen_essential = frozenset(essential_ingredients)
print(f"Frozen essential ingredients: {frozen_essential}")






















