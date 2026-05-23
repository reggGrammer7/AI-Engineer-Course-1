import recipes.flavors
print(recipes.flavors.elachai_chai())



# Method 2
from recipes.flavors import elachai_chai, ginger_chai
print(ginger_chai())


# Relative imports
# used mostly when the file is in the same directory
from .recipes.flavors import ginger_chai


# Avoid 
from recipes.flavors import * # this can affect your program

### The dunder method __init__.py in a folder changes 
# the folder into a module but this usually does 
# not contain any code and is not useful to python 3.3 