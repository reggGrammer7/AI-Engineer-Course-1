from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class UseR(BaseModel):
    id: int
    name: str
    address: Address


# Create an Address instance
address = Address(
    street="123 something",
    city="Gase",
    postal_code="10993"
)

# Correct: just reuse the instance
user1 = address

# Correct: pass an Address instance, not the class
user = UseR(
    id=1,
    name="Jayande",
    address=address,
)

# Correct: Pydantic will parse nested dicts automatically
user_data = {
    "id": 1,
    "name": "Jayande",
    "address": {
        "street": "323 jam",
        "city": "Paris",
        "postal_code": "20023"
    }
}

print(UseR(**user_data))
