# Class inheritance: using other methods from another class
class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai.....") 


# Class inheritance adds a function parenthesis
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamon, ginger, and cloves.")


john = MasalaChai("green tea")
print(john.prepare())
print(john.add_spices())
# print(john.prepare())

# Composition
class ChaiShop:
    chai_cls  = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Regular")
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")



class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai_cls.add_spices()






























