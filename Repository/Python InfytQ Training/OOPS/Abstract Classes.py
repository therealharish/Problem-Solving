class Product:
    def return_policy(self):
        pass

class Mobile(Product):
    def return_policy(self):
        print ("All mobiles must be returned within 10 days of purchase")

class Shoe(Product):
    def return_policy(self):
        print ("All shoes must be returned within 7 days of purchase")

      

m=Mobile()
m.return_policy()

s=Shoe()
s.return_policy()
                                                    