# using a walrus operator to assign and print in one line
# value = 10
# remainder = value % 3
# print(f"The remainder of {value} divided by 3 is: {remainder}")

# # Using walrus operator to assign and print in one line
# value = 10
# print(f"The remainder of {value} divided by 3 is: {(remainder := value % 3)}")

# if remainder := value % 3:
#     print(f"The remainder is {remainder}, which is not zero.")


# # Example 2 
# available_sizes = ["Small", "Medium", "Large"]
# if (requested_size := input("Enter the size you want (Small, Medium, Large): ")) in available_sizes:
#     print(f"{requested_size} is available.")





    # fruits = ["banana", "apple", "grapes", "guava"]
    # for fruit in fruits:
    #     if (requested_fruit := input("Enter your preferred flavor : ")) not in fruits:
    #         print(f"Sorry, we don't have {requested_fruit} flavor.")
    #         break
    #     else:
    #         print(f"Here we go! Wait while we serve you {requested_fruit}")
    #         break
    
fruits = ["banana", "apple", "grapes", "guava"]
while (requested_fruit := input("Enter your preferred flavor : ")) not in fruits:
        print(f"Sorry, we don't have {requested_fruit} flavor.")
        break
else:
        print(f"Here we go! Wait while we serve you {requested_fruit}")










