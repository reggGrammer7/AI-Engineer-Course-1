# Pydantic tries to convert and its only 
# when it's unable that it returns an error

from pydantic import BaseModel

class Product(BaseModel):
    id : int 
    name : str 
    price = float 
    in_stock : bool = True




product_one = Product(id=1, name="Laptop", price =99.99)
product_two = Product(id=2, name="Mouse", price = 24.3 )
product_three = Product(id=2, name="Mouse", price = 24.3 )




















