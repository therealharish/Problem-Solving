class Parrot:
  counter=7001
  def __init__(self, name, color):
    self.__name = name;
    self.__color = color;
    self.__id = Parrot.counter
    Parrot.counter+=1;

  def getName(self):
    print(self.__name)

  def getColor(self):
      print(self.__color)

  def setName(self, name):
    def.__name = name;

  def setColor(self, color):
    def.__color = color;

