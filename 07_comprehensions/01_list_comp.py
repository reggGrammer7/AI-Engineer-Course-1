# We will be learning about comprehensions
# They are simpler ways to write loops and 
# complex functions 
# They are easy to execute and also consumes small space

menu = ["banana","guava","apple","grapes"]

# using comprehensions
iced_tea = [fruit for fruit in menu if "apple" in fruit]

print(iced_tea)
