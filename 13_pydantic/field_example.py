# Pydantic does not have all the datatype conversions however
# you can use typing which is python's core input module 

from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items: List[str]
    quantities : Dict[str, int]



class BlogPost(BaseModel):
    title : str 
    content : str
    image_url : Optional[str] = None



car_data = {
    "user_id" : 123,
    "items" :["Laptop","Mouse","Keyboard"],
    "quantities" :{"laptop":1, "mouse":2,"keyboard":3}

}


print(Cart(**car_data))










































