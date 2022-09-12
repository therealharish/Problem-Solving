class Computer:
    def __init__(self, price1, ver1):
        self.price = price1
        self.ver = ver1


c1 = Computer(90000, 4.2)
c2 = Computer(80000, 1.3)
c3 = Computer(50000, 2.9)
c4 = Computer(30000, 6.9)
c5 = Computer(250000, 58.2)

l1 = [c1, c2, c3, c4, c5]

d = dict()

for item in l1:
    d[item.ver] = item.price

for k, v in d.items():
    print(k, v)
