is_boiling = True 
stri_count = 5
total_actions = stri_count + is_boiling # upcasting TRUE to 1

milk_present = 1 # change values to see result 
print(f"Is there milk? {milk_present}")


is_tea = True
is_coffee = False
is_mixed_with_milk = is_tea and milk_present
print(f"Is the drink mixed with milk? {is_mixed_with_milk}")

