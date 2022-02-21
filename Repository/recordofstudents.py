l=list();
y=1;
while(y):
    d=dict();
    d["name"] = input("Enter name of student: ")
    d["age"] = input("Enter age of student: ");
    d["address"] =input("Enter address of student: ")
    l.append(d)
    choice = input("Do you wish to enter more student records? (y/n): ");
    if(choice=='n'):
      y=0;
print("Student Record: ")
for i in l:
  print(i);