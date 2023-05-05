class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    # def __str__(self):
    #     return '(self.name, self.age)'
    def __repr__(self):
        return {"name": self.name,
        "age": self.age
        }

    
p = Person("Genny", 34)
print(p)
# print(p.__str__())
print(p.__repr__())