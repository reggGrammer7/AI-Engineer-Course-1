# Mutable data 
### LIST OR ARRAYS
ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
ingredients[0] = "hot water"
ingredients[1:3] = ["steamed milk","chai leaves"]
ingredients.insert(2,"ginger")
print(ingredients)

last_ingredient = ingredients.pop() # removes the last ingredient
print(f"Last ingredient removed: {last_ingredient}")

# reverse the list
ingredients.reverse()
print(f"Reversed ingredients: {ingredients}")

# sorting the list
ingredients.sort()
print(f"Sorted ingredients: {ingredients}")

# Finding the max and min
sugar_levels = [1, 2, 3, 4, 5]
print(f"maximum sugar level : {max(sugar_levels)}")




















