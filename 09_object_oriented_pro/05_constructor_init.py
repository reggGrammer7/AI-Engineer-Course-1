class CarOrder:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def summary(self):
        return f"Hola {self.name}, you bought a benz {self.brand}"
    

order1 = CarOrder("Jane","F450") 
print(order1.summary())


order2 = CarOrder("Bryan","Z890") 
print(order2.summary())









