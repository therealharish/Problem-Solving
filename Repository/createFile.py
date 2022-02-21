n = 1;
while(n):
  file = input("Enter File Name: ")
  drive = "Repository/txtfiles"
  s = drive+"/"+file;
  print(s)
  try:
    f = open(s, 'x');
    f.write("New File Created")
    f.close()
    f = open(s, 'r')
    print(f.read())
    f.close()
    n=0;
  except Exception as e:
    choice = input("File already exists, overwrite(y/n): ")
    if(choice == 'y'):
      f = open(s, 'w');
      f.write("Overwrote File!");
      f.close();
      f = open(s, 'r')
      print(f.read())
      f.close()
      n=0;
    else:
      continue;