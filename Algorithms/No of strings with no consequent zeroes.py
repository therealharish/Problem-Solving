num = 6
zerocount = 0
onecount = 0
for i in range(num+1):
  if(i == 0):
    continue
  elif(i==1):
    zerocount = 1
    onecount = 1
  else:
    temp = onecount
    onecount = zerocount+onecount
    zerocount = temp

print(zerocount+onecount)
    