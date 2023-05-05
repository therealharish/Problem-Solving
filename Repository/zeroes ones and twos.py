l=[0,0,0,0,1,1,2,2,0,1,1,2,2,0,0]

x=0;
for i in range(len(l)):
  if(l[i]==0):
    l[x], l[i] = l[i], l[x]
    x+=1
    print(l)
for i in range(len(l)):
  if(l[i]==1):
    l[x], l[i] = l[i], l[x]
    x+=1
    print(l)
for i in range(len(l)):
  if(l[i]==1):
    l[x], l[i] = l[i], l[x]
    x+=1
    print(l)
print(l)