class EDevice:
    def type(self):
        print("Electronic device")

class Computer(EDevice):
    def __init__(self, price, brand):
        self.__price = price
        self.brand = brand

    def buy(self):
        print("Buying computer")

    def exchange(self):
        print("Exchanging Computer")

    def getPrice(self):
        print(self.__price)


class Laptop(Computer):
    pass

class Desktop(Computer):
    pass

l1 = Laptop(90000, "HP")
d1 = Desktop(90000, "Asus")
c1 = Computer(1, "Sharma")

c1.getPrice()
print(c1._Computer.__price)


