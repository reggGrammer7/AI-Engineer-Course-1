# It stops or helps us to prevent data interchangeability of 
# its type. Thus you dont change a variable which is an integer to 
# string to avoid errors
# Pydantic is used for data validation and setting mgt
# use the pwd and add venv in the new path



# Pydantic is basically to check if the data 
# you're receiving matches what you expect 

# So you first give it a format in which you expect the data 
# then you pull the data and once it matches what you expect, 
# it will indicate no error

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

print("Start of pydantic journey")
print(User(name="Alice", age=30))


class user(BaseModel):
    id : int
    name : str
    is_active : bool


# input_data = {'id':101, 'name' : 'Jema' , 'is_active' :25}
# print(user(**input_data))
# Always unpack the dictionary

input_data = {'id':101, 'name' : 'Jema' , 'is_active' :True}
print(user(**input_data))



































