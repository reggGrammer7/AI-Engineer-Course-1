# Tea menu loop
tea_menu = ["Green Tea", "Black Tea", "Oolong Tea", "White Tea"]
for tea in tea_menu:
    print("Today's tea selection includes:", tea)



 # Enumerating tea menu with index
tea_menu = ["Green Tea", "Black Tea", "Oolong Tea", "White Tea"]
for index, tea in enumerate(tea_menu, start=1):
    print(f"{index}. {tea}")   