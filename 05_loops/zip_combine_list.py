# Combining two lists with zip
names = ["Alice", "Bob", "Charlie"]
bills = [25, 30, 35]
for name, bill in zip(names, bills):
    print(f"{name} is {bill} years old.")