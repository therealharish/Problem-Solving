class smallval(Exception):
  def __init__(self, arg):
    self.args = arg;

class unwell(Exception):
  def __init__(self, arg):
    self.args = arg;   


name = input("Enter name: ")
phone = input("Enter phone number: ")
age = int(input("Enter age: "))
fit = input("Is the applicant physically well? (y/n): ")
try:
  if(age <18):
    raise smallval("Underage")
  elif(fit == 'n'):
    raise unwell("Unfit")
  else:
    sub1 = name[0:3]
    sub2 = phone[-4:]
    print("Application Number: ", sub1+sub2)
except smallval as e:
  for i in e.args:
    print(i, end="")
except unwell as e:
  for i in e.args:
    print(i, end="")