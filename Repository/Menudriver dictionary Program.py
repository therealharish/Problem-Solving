rc= {"12/04/2022": {"Apple":120, "Orange":200},
    "13/04/2022": {"Apple":220, "Orange":300},
    "15/04/2022": {"Apple":320, "Orange":400},             
    "16/04/2022": {"Apple":420, "Orange":500},
    "17/04/2022": {"Apple":520, "Orange":600},            
    }

print("Rate Chart -----")
for x,y in rc.items():
  print(x, ":", y)

while(True):
  print("1: Update")
  print("2: Add data")
  print("3: Remove Data")
  print("4: Search")
  ch = int(input("Enter your choice: "))

  if(ch==1):
    date = input("Enter date in dd/mm/yyyy format: ")
    for x,y in rc.items():
      if(x==date):
        for i,j in y.items():
          print("Enter new price of",i,": ")
          y[i] = int(input())
    print("Updated Rate Chart ----")
    for x,y in rc.items():
      print(x, ":", y)

  elif(ch==2):
    date = input("Enter date in dd/mm/yyyy format: ")
    if date in list(rc.keys()):
      print("Date Already Exists")
    else:
      app = int(input("Enter price of Apple: "))
      ora = int(input("Enter price of Orange: "))
      rc[date] = {"Apple": app, "Orange": ora}
    print("Updated Rate Chart ----")
    for x,y in rc.items():
      print(x, ":", y)

  elif(ch==3):
    date = input("Enter date in dd/mm/yyyy format: ")
    if date not in list(rc.keys()):
      print("Date does not exist")
    else:
      del rc[date]
    print("Updated Rate Chart ----")
    for x,y in rc.items():
      print(x, ":", y)

  elif(ch==4):
    date = input("Enter date in dd/mm/yyyy format: ")
    if date not in list(rc.keys()):
      print("Date does not exist")
    else:
      for x,y in rc.items():
        if(x==date):
          for i,j in y.items():
            print("Price of", i, ": ", j)

  s = int(input("Do you wish to continue? 0/1: "))
  if s:
    continue
  else:
    break

  
      
      


                