l=list();
y=1;
while(y):
  print("Menu")
  print("---------------------")
  print("Input Record: 1")
  choice = int(input())
  if(choice == 1):
      d=dict();
      d["name"] = input("Enter name of student: ")
      d["roll"] = input("Enter roll number: ")
      d["age"] = input("Enter age of student: ");
      d["address"] =input("Enter address of student: ")
      l.append(d)
  elif(choice=='10'):
      y=0;
  print("Student Record: ")
  for i in l:
    print(i);