# Used mostly for looping over sets 
favorite_fruit = ["grapes","apple","guava","banana","strawberry","banana","mango"]

unique_fruit = { fruit for fruit in favorite_fruit }
print(unique_fruit)



recipes = {
    "masala chai" : ["ginger","cardamon","clove"],
    "Elachai chai" : ["cardmon","milk"],
    "spicy chai" : ["ginger","black pepper","clove"]
                    
}

arr = set()
for ing in recipes.values():
    arr.update(ing)
print(arr)    

# Using come
unique_spices = { spice for ing in recipes.values() for spice in ing}

print(unique_spices)

