d = {"Robert": 36787,
    "Tina": 68721,
    "Jo":56389}
password = ""
for i in d:
  l = len(i)
  value = str(d[i])
  if (str(l) in value):
    password+=i[l-1]
  elif(str(l) not in value):
    maximum = -1
    for j in value:
      if(int(j)<l and int(j)>maximum):
        maximum = int(j)
    if(maximum!=-1):
      password+=i[maximum-1]
    else:
      password+="X"
        

print(password)
  
    