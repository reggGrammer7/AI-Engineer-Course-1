# Main goal of a class is to a be able to create multiple 
# objects by calling the method in the class.
# This makes it easier than writing the same code repeatedly

class chaicup:
    size = 150
    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup1 = chaicup()    
print(cup1.describe())
cup2 = chaicup()
cup2.size = 100
print(chaicup.describe(cup2))
cup3 = chaicup()
print(cup3.describe())