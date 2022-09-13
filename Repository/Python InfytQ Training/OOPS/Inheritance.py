class Computer():
    def __init__(self, brand, price, ram, storage):
        self.brand = brand
        self.price = price
        self.ram = ram
        self.storage = storage

    def buy(self):
        print("Buying computer")

    def run(self):
        pass

    def sell(self):
        pass

    def compute(self):
        pass

class Laptop(Computer):

    # def __init__(self, battery, carry, brand, price, ram, storage):
    def __init__(self, battery, carry, c1):
        # super().__init__(brand, price, ram, storage)
        super().__init__(c1.brand, c1.price, c1.ram, c1.storage)
        self.battery = battery
        self.carry = carry

    def exchange(self):
        print("Want to exchange with a computer")

    def buy(self):
        print("Buying Laptop")    

c1 = Computer("XYZ", 90000, 4, 512)
l1 = Laptop("4000 mAH", "YES", c1)


print(l1.battery)
print(l1.carry)
l1.exchange()
l1.buy()


print(l1.brand, l1.price, l1.ram, l1.storage)

