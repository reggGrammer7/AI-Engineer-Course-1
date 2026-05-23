file = open("order.txt","w")
try:
    file.write("Masala Chai - 2 cups\n")
finally:
    file.close()


# Modern python way to handle files is using with statement which automatically takes care of closing the file
with open("order_anonymous.txt","w") as file:
    file.write("Masala Chai - 2 cups\n")












