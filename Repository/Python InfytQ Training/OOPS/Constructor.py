class Student:
    species = 'Canis '

    def init(self, name):
        print('inside constructor')
        self.name = name
        print('instance variable initialised')

    def show(self):
        print('my name is ', self.name)


o = Dog('Harry')
o.show()
