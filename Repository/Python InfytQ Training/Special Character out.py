s = "19@a42&516"
count = 0
newstr = ""
lo=[]
le=[]
for i in s:
  if not i.isnumeric():
    count+=1
  elif (i.isnumeric() and int(i)&1):
    lo.append(i)
  else:
    le.append(i)

if count&1==0:
  while(len(le) and len(lo)):
    newstr+= le.pop(0)
    newstr+= lo.pop(0)
else:
  while(len(le) and len(lo)):
    newstr+= lo.pop(0)
    newstr+= le.pop(0)
    
print(newstr)
      
      
    
    