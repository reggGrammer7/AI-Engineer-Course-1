flavor = ["Ginger","Out of stock","lemon","Discontinued","Cardamom"]

for flavor in flavor:
    if flavor == "Out of stock":
        print("Sorry, we are out of stock for", flavor)
        continue
    if flavor == "Discontinued":
        print("Sorry, we have discontinued", flavor)
        break
    else:
        print("Preparing", flavor, "chai")